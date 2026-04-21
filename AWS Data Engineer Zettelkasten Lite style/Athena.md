---
services:
  - AWS Glue
  - AWS Lambda
  - Amazon Athena
  - Amazon S3
tags: ['aws', 'athena']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Athena
- Athena is a interactive query service that allows ad-hoc queries on data stored in multiple sources.
- It is completely serverless and only charges for the data consumed.
- Athena uses [[Schema on Read]].

### Supported Formats

Athena supports structured and unstructured data

- **Open Source**: CSV, JSON, XML, CSV, TSV, ORC, Avro, Parquet.
- **AWS**: VPC Flow Logs, ELB Logs, CloudTrail.

### S3 Storage Class Compatibility
- **Supported (Direct Query)**:
    - S3 Standard
    - S3 Intelligent-Tiering
    - S3 Standard-IA
    - S3 One Zone-IA
    - S3 Glacier Instant Retrieval
- **Not Supported (Direct Query)**:
    - S3 Glacier Flexible Retrieval
    - S3 Glacier Deep Archive
- **Restoration Requirement**: To query objects in **Glacier Flexible Retrieval** or **Deep Archive**, you must first **restore** them to a standard storage class. Athena ignores archived objects by default unless `read_restored_glacier_objects` is set to `true`, in which case it queries the *restored* copy.

##  Active Recall
- How does this service integrate with other AWS components mentioned?

---

![[Excalidraw/Athena]]

## Athena Federated Queries
- Query data from sources other than [[Amazon S3 Fundamentals|S3]].
- Data source connectors translate between source and Athena - Data source connectors run on [[Lambda]]
- Views can be created that are stored in [[AWS Glue Fundamentals|Glue]].
- AWS Secrets Manager can be used to manage the credentials for the external data sources.
- Cross account federated queries
- Pass through queries - Using query language native to the data source.

## Query Examples

### ORC Files for Open Street Maps from S3 Bucket in US-East-1 Region
**Create Table**

```sql
CREATE EXTERNAL TABLE planet (
  id BIGINT,
  type STRING,
  tags MAP<STRING,STRING>,
  lat DECIMAL(9,7),
  lon DECIMAL(10,7),
  nds ARRAY<STRUCT<ref: BIGINT>>,
  members ARRAY<STRUCT<type: STRING, ref: BIGINT, role: STRING>>,
  changeset BIGINT,
  timestamp TIMESTAMP,
  uid BIGINT,
  user STRING,
  version BIGINT
)
STORED AS ORCFILE
LOCATION 's3://osm-pds/planet/';
```

---
**Run Query**

```sql
SELECT * FROM planet
WHERE type = 'node'
    AND tags['amenity'] IN ('veterinary')
    AND lat BETWEEN -27.8 AND -27.3
    AND lon BETWEEN 152.2 AND 153.5;
```

**Query Stats**
Time in queue: 87 ms
Run time: 19.744 sec
Data scanned: 72.59 GB

---
