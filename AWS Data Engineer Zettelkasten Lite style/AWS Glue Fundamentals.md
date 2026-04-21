---
services:
  - AWS Glue
  - AWS IAM
  - Amazon CloudWatch
  - Amazon S3
tags: ['aws', 'glue']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## AWS Glue Fundamentals
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does Glue transform and deliver streaming data from MSK to S3?

---

![[Apache Spark]]

**AWS Glue** is a fully managed
 extract, transform, and load (ETL) service that makes it easy for customers to prepare and load data for analytics. It provides capabilities for schema detection, ETL jobs, and crawlers that make it useful for working with dynamic or changing schemas.

AWS Glue provides real-time, continuous logging for AWS Glue jobs. You can view real-time Apache [[Spark]] job logs in [[CloudWatch and CloudTrail| CloudWatch]], including driver logs, executor logs, and an Apache [[Spark]] job progress bar.

### Job Bookmarks
- Persists state from the job run.
- Prevents re-processing of old data.
- Works with S3 sources and relational Databases via JDBC - if PKs are in sequential order. 

### Metadata Management
- **Crawlers**: Discover schema and update Data Catalog.
- **Job-Integrated Updates**: Use `enableUpdateCatalog` within ETL scripts to update partitions without running a crawler. See [[AWS Glue Data Catalog#Updating Partitions API vs ETL Property|Comparison with create_partition API]].
