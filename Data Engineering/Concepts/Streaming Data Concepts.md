---
tags:
  - data-engineering
  - streaming
  - spark
  - concepts
status: atomic
topic: Stream Processing
domain: Data Engineering
created_at: 2026-01-07T09:25:00
---
## Streaming Data Concepts

**Streaming Data Concepts** refer to the fundamental mechanisms used in modern stream processing frameworks (like [[Data Engineering/Technologies/Spark#Spark Structured Streaming|Spark Structure Streaming]], Flink, and [[AWS Glue Fundamentals | AWS Glue]]) to handle continuous data, ensuring fault tolerance, correctness, and time-based aggregation.

### Active Recall
*   What mechanism allows a streaming job to recover from failure without losing data? -> [[Streaming Data Concepts#Checkpointing|Checkpointing]]
*   How does a stream processor handle data that arrives late (out of order)? -> [[Streaming Data Concepts#Watermarking|Watermarking]]
*   What is the difference between Event Time and Processing Time?
          -> **Event Time** is when the action occurred **Processing Time** is when the system received it.
*   Which Output Mode rewrites the entire result table every trigger? -> [[Streaming Data Concepts#Output Modes|Complete Mode]]
*   Which aggregation window type has overlapping intervals? -> [[Streaming Data Concepts#4. Windowing Strategy|Sliding Window]]

---

### Key Concepts

#### 1. Checkpointing
*   **Definition:** The process of saving the current application state (progress, offsets, and aggregation buffers) to reliable durable storage (e.g., [[S3]], HDFS).
*   **Purpose:** **Fault Tolerance**. If a node fails or the job crashes, the system restarts from the last successful checkpoint rather than from the beginning.
*   **Semantics:** Enables **Exactly-Once** (or At-Least-Once) processing guarantees.

#### 2. Watermarking
*   **Definition:** A threshold that tells the system how long to wait for "late" data before finalizing a window aggregation.
*   **Problem Solved:** Handling **Late Data** (Out-of-Order events).
*   **Logic:** "I will accept data up to 10 minutes older than the current max event time. Anything older is dropped."
*   **Crucial For:** Accurate aggregations on **Event Time**.

#### 3. Event Time vs. Processing Time
*   **Event Time:** The timestamp generated at the source (e.g., when the user clicked the button).
*   **Processing Time:** The timestamp when the data actually hit the ingestion server.
*   **Gap:** Network lag or offline devices cause a gap between these two. Robust systems aggregate on *Event Time* but use *Watermarks* to bound the wait time.

#### 4. Windowing Strategy
How data is grouped into time buckets for aggregation.
*   **Tumbling Window:** Fixed size, non-overlapping (e.g., [12:00-12:05], [12:05-12:10]). Every event belongs to exactly one window.
*   **Sliding Window:** Fixed size, overlapping (e.g., 5-minute window starting every 1 minute). An event can belong to multiple windows.
*   **Session Window:** Dynamic size based on activity. Closes after a period of inactivity (gap).

#### 5. Delivery Semantics
The "guarantee" of how many times a record will be processed.
*   **At-Most-Once:** "Fire and forget." Data might be lost, but never duplicated. High performance, low reliability.
*   **At-Least-Once:** Data is never lost, but might be re-processed (duplicated) if an acknowledgment fails. Requires downstream deduplication (idempotency).
*   **Exactly-Once:** Data is processed effectively once. Achieved via checkpoints and idempotent sinks (like Glue writing to S3 with transactional logic).

#### 6. Backpressure
*   **Definition:** The mechanism where a system slows down data ingestion when the downstream processing cannot keep up.
*   **Purpose:** Prevents Out-Of-Memory (OOM) errors and system crashes during traffic spikes.

#### 7. Dead Letter Queue (DLQ)
*   **Definition:** A separate storage location (S3 bucket, SQS queue) where "bad records" (that fail parsing or validation) are sent.
*   **Purpose:** Prevents a single bad record from blocking the entire pipeline. Allows for post-mortem analysis of failures.

### Spark Structured Streaming Specifics

#### Output Modes
Determines *what* gets written to the sink (destination) after each trigger:
1.  **Append Mode:** Only **new rows** that are finalized (will not change) are written. Use for simple ETL/Ingestion.
2.  **Update Mode:** Only rows that were **updated** in the last trigger are written. Use for maintaining running counts.
3.  **Complete Mode:** The **entire table** is rewritten every time. Use for small aggregations; **avoid** for large unbounded streams.

#### Triggers (Micro-batching)
*   Defines the timing of streaming data processing.
*   **Default:** Run the next batch as soon as the previous one finishes.
*   **Fixed Interval:** Process data every X seconds (e.g., `trigger(processingTime='10 seconds')`).

### Exam Tips (AWS DEA-C01)

> [!INFO] Exam Tip: Glue & MSK
> *   If a **Glue Streaming Job** fails, it uses **Checkpoints** stored in S3 to resume reading from the correct Kafka/Kinesis offset.
> *   If you need to query a stream with **SQL** logic (joins, windows), use **Spark Structured Streaming** (via Glue or EMR).
> *   **Small File Problem:** Streaming jobs often create many small files in S3. Use **S3 Compaction** or a daily batch job to merge them for Athena performance.
