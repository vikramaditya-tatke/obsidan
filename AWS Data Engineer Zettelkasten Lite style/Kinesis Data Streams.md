---
services:
  - Amazon Kinesis
  - Amazon SQS
tags: ['aws', 'kinesis', 'streaming']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Kinesis Data Streams

### Active Recall
- What are the throughput limits per shard for ingestion vs consumption?
- How do you calculate the minimum number of shards required for a stream?
- What is the specific payload unit size for billing?

---

## Key Concepts
- **IteratorAgeMilliseconds** -> High value means consumers are falling behind real-time.
- **Re-sharding** -> Manual process to scale shards up (Split) or down (Merge).
- **Kinesis Producer Library (KPL)** -> Aggregates smaller records into 25 KB chunks -> increases cost efficiency.
## Core Throughput Rules
- **Ingestion (Inbound)** -> 1 MB/s per shard OR 1,000 records/sec per shard.
- **Consumption (Outbound)** -> 2 MB/s per shard.
- **Billing Unit** -> 25 KB PUT Payload Unit.

### Shard Calculation Workflow
- **Step 1** -> Calculate total Inbound throughput (MB/s) -> divide by 1.
- **Step 2** -> Calculate total Outbound throughput (MB/s) -> divide by 2.
- **Step 3** -> Compare results from Step 1 and Step 2.
- **Step 4** -> The required number of shards is the **higher** of the two values.

### Applied Examples
- **Scenario 1** -> Inbound is 5 MB/s -> Outbound is 8 MB/s.
    - Step 1 -> 5 / 1 -> 5 shards.
    - Step 2 -> 8 / 2 -> 4 shards.
    - Result -> **5 shards required**.
- **Scenario 2** -> 3,000 records/sec (500 bytes each).
    - Step 1 -> (3000 * 500 bytes) / 1,000,000 -> 1.5 MB/s -> 2 shards (round up).
    - Step 2 -> Record limit -> 3000 / 1000 -> 3 shards.
    - Result -> **3 shards required**.

## SQS Vs KDS
- **SQS** -> Taking Action -> Decoupling -> Typically 1 consumer group.
- **KDS** -> Processing Data -> Streaming Analytics -> Supports 100s of simultaneous consumer groups.
