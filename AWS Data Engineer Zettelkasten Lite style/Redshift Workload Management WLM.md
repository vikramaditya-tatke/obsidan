---
services:
  - AWS IAM
  - Amazon Redshift
  - Amazon S3
tags: ['aws', 'redshift', 'wlm']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Redshift Workload Management (WLM)
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[RedShift]]

## Redshift Workload Management (WLM)

Query Queues -> Default 5; Up to 8. Prioritize fast, short queries vs slow, long running queries.

Concurrency Scaling ->	Automatically add cluster capacity to handle an increase in **read** queries

Manage which queries are sent to the concurrency scaling cluster.