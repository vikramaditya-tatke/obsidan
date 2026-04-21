---
services:
  - AWS CloudTrail
  - Amazon Athena
tags:
  - aws
  - cloudtrail
  - security
  - sql
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2026-01-09
---
## CloudTrail Lake
- **Definition**: A managed data lake for capturing, storing, accessing, and analyzing user and API activity on AWS.
- **Storage Format**: Converts logs from JSON to **Apache ORC** (columnar format) for optimized SQL querying.
- **Event Data Stores**: Immutable collections of events. Can store:
    - Management Events
    - Data Events (S3, Lambda)
    - Configuration Items (AWS Config)
    - **Non-AWS Events**: Can ingest audit logs from hybrid or SaaS applications via `PutAuditEvents` API.

### Querying
- Uses a SQL dialect (Trino-based) to run complex queries across multiple fields.
- **Federation**: Can use [[AWS Lake Formation]] to federate event data stores to **Amazon Athena** for zero-ETL analysis (joining CloudTrail data with other S3 data).

### Retention
- **Seven-Year Retention**: Fixed retention for audit compliance.
- **One-Year Extendable**: Flexible retention (up to 10 years).

> [!INFO] Exam Tip
> CloudTrail Lake allows you to run SQL queries on your audit logs *without* setting up a separate Athena table or S3 bucket pipeline. It is the built-in "SQL over Logs" solution.
