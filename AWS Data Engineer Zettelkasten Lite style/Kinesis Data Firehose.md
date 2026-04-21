---
services:
  - AWS Lambda
  - Amazon Kinesis
  - Amazon Redshift
  - Amazon S3
tags: ['aws', 'kinesis', 'firehose']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Kinesis Data Firehose
### Active Recall
- What are the latency characteristics mentioned for this service/feature?
- What are the key cost drivers or pricing models for this service?

---

Kinesis Data Firehose is a fully-managed stream based delivery service that scales automatically capable of delivering high throughput streaming data to data lakes, data stores and analytics services in *near* real-time.

- Transformation can be handled on the fly using [[Lambda]] Functions.
- Is charged on the basis of the amount of data passing through the services.

It can deliver to [[Amazon S3 Fundamentals|S3]], [[Redshift Data Loading COPY|Redshift]], http endpoints (think of ClickHouse, Apache Druid, or any other http endpoints.)

> Kinesis Data Firehose is a near-real time service that can receive data in real-time but the consumers cannot use it in real-time.

Latency for Kinesis Data Firehose buffers the before delivery. Minimum buffer interval is 1 minute and minimum buffer size is 1 MB.