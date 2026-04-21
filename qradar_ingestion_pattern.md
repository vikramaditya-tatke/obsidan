# The Batch Manifest Pattern: Reliable QRadar Ingestion in ClickHouse

This document outlines a robust architectural pattern for ingesting high-volume, potentially duplicate log data from IBM QRadar into ClickHouse.

## The Problem
We are ingesting data from the QRadar Ariel API with the following constraints:
1.  **No Unique IDs:** Records lack a generic UID.
2.  **Legitimate Duplicates:** Identical events (same text, same millisecond) occur and must be counted in analysis.
3.  **Unstable Results:** We cannot use `ORDER BY` in QRadar (too heavy), so result order is not guaranteed across requests.
4.  **Crash Risk:** Scripts using `stream=True` might be interrupted (`Ctrl+C`), leaving partial data in the database.
5.  **Accuracy:** Analysis queries must provide exact sums matching QRadar, regardless of retries or crashes.

## The Solution: Decoupling Storage from Validity

Instead of trying to deduplicate row-by-row, we use a **Manifest** approach. We write *everything* to a storage table, but we only "activate" valid batches using a separate control table.

### 1. Database Schema

#### A. The Data Table (`qradar_logs`)
This table acts as a "Dump" or "Sink". It accepts all data—successful runs, crashed runs, and retries.

```sql
CREATE TABLE qradar_logs
(
    -- Log Data Columns
    timestamp DateTime64(3),
    start_time DateTime64(3),
    source_ip String,
    destination_ip String,
    source_port UInt16,
    destination_port UInt16,
    event_name String,
    event_id String,
    domain_id UInt32,
    domain_name String,
    event_count UInt8, -- Always 1, per AQL query
    username String,
    
    -- Ingestion Metadata
    run_id UUID, -- The unique batch identifier
    
    -- Partitioning Helper
    ingestion_date Date DEFAULT toDate(timestamp)
)
ENGINE = MergeTree()
PARTITION BY ingestion_date
ORDER BY (timestamp); -- Primary sort key for fast range queries
```

#### B. The Manifest Table (`qradar_manifest`)
This table acts as the "Source of Truth". It defines which `run_id` is the **currently valid** version for a specific slice of data.

```sql
CREATE TABLE qradar_manifest
(
    -- The Composite Identity of a "Batch"
    range_start DateTime,
    range_end DateTime,
    domain String,
    aql_query_name String,
    event_processor String,

    -- The Pointer
    valid_run_id UUID,
    
    -- Metadata
    created_at DateTime DEFAULT now()
)
ENGINE = ReplacingMergeTree(created_at)
ORDER BY (range_start, range_end, domain, aql_query_name, event_processor);
```
*   **`ReplacingMergeTree(created_at)`**: This engine automatically keeps only the latest row for a unique combination of the sorting key. If you re-run a batch, the new entry supersedes the old one.

#### C. The Analysis View (`view_qradar_clean`)
This view presents the clean, accurate data to analysts. It filters out crashed runs and superseded retries instantly.

```sql
CREATE VIEW view_qradar_clean AS
SELECT 
    l.timestamp,
    l.start_time,
    l.source_ip,
    l.destination_ip,
    l.source_port,
    l.destination_port,
    l.event_name,
    l.event_id,
    l.domain_id,
    l.domain_name,
    l.event_count,
    l.username,
    l.run_id
FROM qradar_logs AS l
INNER JOIN (
    -- Subquery to get the authoritative list of valid run_ids
    SELECT valid_run_id
    FROM qradar_manifest
    FINAL -- Optional: Forces merge consistency at query time (usually fast for small tables)
) AS m ON l.run_id = m.valid_run_id;
```

---

### 2. Ingestion Workflow (Python)

The logic shifts from "Checking if data exists" to "Blindly writing and committing."

```python
import uuid
import clickhouse_connect
from datetime import datetime

def ingest_qradar_batch(client, qradar_params):
    """
    qradar_params: dict containing range_start, range_end, domain, etc.
    """
    
    # 1. Generate Identity
    # This UUID is the glue between the logs and the manifest.
    this_run_id = uuid.uuid4()
    
    print(f"Starting Batch Run: {this_run_id}")
    
    try:
        # 2. Stream Data (The Heavy Lift)
        # Pseudocode for QRadar API call
        response = qradar_api.get_search_results(stream=True, **qradar_params)
        
        row_buffer = []
        for line in response.iter_lines():
            if line:
                # IMPORTANT: Attach the UUID to every single row
                record = parse_json(line)
                record['run_id'] = this_run_id
                row_buffer.append(record)
                
                if len(row_buffer) >= 10000:
                    client.insert('qradar_logs', row_buffer)
                    row_buffer = []

        # Flush remaining rows
        if row_buffer:
            client.insert('qradar_logs', row_buffer)

        # 3. The Atomic Commit
        # We only reach this line if the stream finished 100% successfully.
        # This insert makes the data "visible" in the View.
        manifest_entry = [
            qradar_params['range_start'],
            qradar_params['range_end'],
            qradar_params['domain'],
            qradar_params['aql_query_name'],
            qradar_params['event_processor'],
            this_run_id,
            datetime.now()
        ]
        
        client.insert('qradar_manifest', [manifest_entry])
        print("Batch Committed Successfully.")

    except KeyboardInterrupt:
        print(f"\nCRASH DETECTED! Run ID {this_run_id} was aborted.")
        print("Data was written to 'qradar_logs' but NOT committed to 'qradar_manifest'.")
        print("This data is invisible to analysts and safe to retry.")
    except Exception as e:
        print(f"Error: {e}")
        # Logic to handle other failures (same outcome: do not write manifest)
```

---

### 3. Pros & Cons

| Feature | Impact |
| :--- | :--- |
| **Crash Safety** | **High.** `Ctrl+C` or OOM crashes result in "Orphaned" data. Since no Manifest entry is created, the View returns 0 rows for that failed batch. |
| **Accuracy** | **100%.** Logic relies on "All or Nothing." You never get partial data or duplicates from retries. |
| **Performance** | **High.** ClickHouse joins on small right-side tables (Manifests) are extremely fast (Hash Join). |
| **Legitimate Duplicates** | **Preserved.** If QRadar sends two identical rows, we write two identical rows. |
| **Storage Overhead** | **Medium.** "Dead" data (crashed runs) stays on disk until cleaned up. |

---

### 4. Alternative Approach: The Window Function Strategy

An alternative approach often considered is "Deduplication at Query Time" using Window Functions.
**Strategy:** Dump all data (retries and all) into one table and run a query like:

```sql
SELECT * FROM (
    SELECT *,
           row_number() OVER (PARTITION BY [ALL_COLUMNS] ORDER BY timestamp DESC) as rn
    FROM qradar_logs
) WHERE rn = 1
```

#### Why this FAILS for this Use Case

| Feature | Batch Manifest (Recommended) | Window Function (`row_number`) |
| :--- | :--- | :--- |
| **Legitimate Duplicates** | **Preserved.** If QRadar sends 5 identical events, the View returns 5 events (as they share the same valid `run_id`). | **LOST.** The window function sees 5 identical rows (same content, same timestamp) and collapses them into 1. You cannot distinguish between "5 real events" and "1 event ingested 5 times." |
| **Crash Handling** | **Clean.** Crashed runs are ignored entirely. | **Messy.** A crashed run might insert 50% of the data. The next retry inserts 100%. You now have 1.5x copies of the first half. While deduplication *might* fix the first half, it cannot fix the "Legitimate Duplicate" issue mentioned above. |
| **Query Performance** | **O(1) Lookup.** The JOIN is an instant hash lookup against a small list of UUIDs. | **O(N log N) Sort.** Window functions force ClickHouse to sort the entire result set by the Partition key to calculate row numbers. For billions of rows, this is significantly slower and memory-intensive. |
| **Result Accuracy** | **Exact Match.** SUMs match QRadar exactly. | **Under-counting.** Will consistently under-report traffic volume by deduping high-frequency identical events (e.g., firewall deny logs). |

**Verdict:** The Window Function approach is **unacceptable** because it destroys data integrity for "Legitimate Duplicates" and incurs a massive performance penalty on large datasets.

---

### 5. Considerations & Optimizations

#### The "Orphaned Data" Cleanup
Over time, `qradar_logs` will accumulate data from crashed runs or old runs that were re-processed. This wastes disk space.

**Solution:** Schedule a monthly maintenance query.
```sql
-- Delete rows where the run_id is NOT in the current manifest
ALTER TABLE qradar_logs 
DELETE WHERE run_id NOT IN (
    SELECT valid_run_id FROM qradar_manifest
);
```
*Note: This is a heavy mutation. Run this during off-hours.*

#### ClickHouse v25.10 Specifics
*   **`JOIN` Memory:** Ensure your `max_rows_in_join` setting allows the Manifest table to fit in memory. Since Manifest rows are tiny (UUIDs + Timestamps), you can easily fit millions of batches in a few GB of RAM.
*   **Partitioning:** Ensure `qradar_logs` is partitioned by `toYYYYMM(timestamp)` or `toDate(timestamp)`. This allows ClickHouse to drop entire parts of data efficiently during cleanup if needed.

#### Gotchas
1.  **Manifest Granularity:** The columns in your Manifest `ORDER BY` key (`domain`, `range_start`, etc.) **MUST** match exactly how you slice your Python batches. If you change your slicing strategy (e.g., change from 15-min to 1-hour chunks), you might end up with overlapping ranges in the Manifest.
2.  **View Query Performance:** The `INNER JOIN` forces ClickHouse to read the Manifest. While fast, for ultra-low latency dashboards (sub-50ms), ensure `qradar_manifest` is kept reasonably small (e.g., standard housekeeping to remove manifest entries for data older than retention policy).