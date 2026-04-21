---
services:
  - AWS Backup
  - AWS IAM
  - Amazon Aurora
  - Amazon DynamoDB
  - Amazon EBS
  - Amazon EC2
  - Amazon EFS
  - Amazon FSx
  - Amazon RDS
  - Amazon S3
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Backup
###  Active Recall
- Describe the encryption options available for Backup.
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

Fully managed data-protection service.

Consolidated management of backups in one place - across all **accounts and regions**

Point in time restore

Cron jobs supported

Life-cycles for transitioning to cold storage.

**Vaults** are the destination to store the backup.

	- Vault is a container and can be assigned a KMS key for encrypting the backup

	- **Lock**: Can/ store data for compliance. After a cooling period of 72 hours not even AWS can delete the data. However, it can still age out.

## Supported Services
- [[EC2|EC2]]
- EBS
- EFS, FSx
- [[RDS and Aurora]], [[DynamoDB Capacity Modes|DynamoDB]], Neptune, DocumentDB.