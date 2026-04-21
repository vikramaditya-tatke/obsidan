---
services:
  - AWS Backup
  - AWS IAM
  - Amazon Aurora
  - Amazon CloudWatch
  - Amazon RDS
  - Amazon S3
tags: ['aws', 'rds', 'aurora']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## RDS and Aurora Fundamentals
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

Hosted RDBS for the following databases - All offer ACID (

	*A*-> Atomic (Entire transaction succeeds or it all fails )

	*C*-> Consistent (All transactions written to the databases follow the rules)

	*I* -> Isolation (Each transaction must be independent, important for concurrency control)

	*D*-> Durability (All changes made to the databases must be permanent)

	) compliance

	
- [Amazon Aurora](#Amazon Aurora)
- MySQL
- PostgreSQL
- MariaDB - (Open Source MySQL)
- Oracle
- SQL Server

>  [[AWS IAM]] authentication only works with MariaDB, MySQL, and PostgreSQL.
## RDS
### Operational Guidelines

Use CloudWatch to monitor memory, CPU, storage, replica lag

Perform automatic backups during daily low in write IOPS - use cloud watch for this too

Insufficient I/O will make recovery after failure slow

- Migrate to DB instance with more I/O
- Move to General Purpose or Provisioned IOPS storage
- Set TTL on DNS for your DB instances to 30 seconds or less. Imagine a situation where a DNS entry needs to be changed so that the apps are automatically routed to the backup host, but the DNS is being cached for an hour.
- Provision sufficient RAM - Observe the Disk IOPS: If this number is low then the database is not hitting the disk very often and the working set is fully contained in-memory.