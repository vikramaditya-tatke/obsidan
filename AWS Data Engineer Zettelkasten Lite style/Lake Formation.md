---
services:
  - AWS Glue
  - AWS IAM
  - AWS Lake Formation
  - Amazon Aurora
  - Amazon EC2
  - Amazon RDS
  - Amazon S3
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Lake Formation
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

- Already use [[Amazon S3 Fundamentals|S3]] -> you typically begin by registering existing [[Amazon S3 Fundamentals|S3]] buckets that contain your data.
- AWS Lake Formation is integrated with AWS [[AWS Glue Fundamentals|Glue]], which can be used to create a data catalog.
- Lake Formation lets you define policies and control data access with simple “grant and revoke permissions to data” sets at granular levels.
- AWS Lake Formation also provides blueprints that you can run for loading and cataloging data.
- A blueprint allows you to import data from:
	- MySQL, Postgres, SQL Server, MariaDB, Oracle databases running in Amazon [[RDS and Aurora Fundamentals|RDS]] or hosted in Amazon [[EC2|EC2]] or JDBC on-prem

