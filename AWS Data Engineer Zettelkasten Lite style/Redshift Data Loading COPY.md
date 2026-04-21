---
services:
  - AWS DataSync
  - AWS IAM
  - Amazon Aurora
  - Amazon DynamoDB
  - Amazon EFS
  - Amazon EMR
  - Amazon FSx
  - Amazon Redshift
  - Amazon S3
  - Amazon VPC
tags: ['aws', 'redshift', 'etl']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Redshift Data Loading (COPY)
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[RedShift.excalidraw]]

## Data Flows and COPY

### Copy
- Used to load data _from the outside to_ Redshift.
- If data is within Redshift use the traditional _INSERT INTO ... SELECT ..._ syntax
- Allows to load data from [[Amazon S3 Fundamentals|S3]], [[EMR Fundamentals|EMR]], [[DynamoDB Capacity Modes|DynamoDB]]
- Very efficient, recommended and parallelized.
- COPY can decrypt and hardware backed SSL is supported.
- Compression is also supported and decides which compression to use within Redshift.
- **Enhanced [[VPC Networking Fundamentals|VPC]] Routing**: If [[VPC Networking Fundamentals|VPC]] Endpoints are not properly setup, Redshift will move data over the internet.
- Auto-copy from [[Amazon S3 Fundamentals|S3]]: Automatically replicates data from the bucket -> Like CDC
- Zero ETL with Aurora: Automatically replicates data from Aurora into Redshift -> Like CDC

### Unload
- Redshift can UNLOAD the data to S3.

> Redshift cannot unload data to S3 Glacier directly.
### DataSync

- Used to move large amounts of data to and from places
- On-premises / other clouds to AWS - _needs agent_
- Can synchronize to -
	- [[Amazon S3 Fundamentals|S3]]
	- EFS
	- FSx
- Replication tasks can be SCHEDULED daily, hourly, weekly.