Fully managed data-protection service.

Consolidated management of backups in one place - across all **accounts and regions**

Point in time restore

Cron jobs supported

Life-cycles for transitioning to cold storage.

**Vaults** are the destination to store the backup.

	- Vault is a container and can be assigned a KMS key for encrypting the backup

	- **Lock**: Can/ store data for compliance. After a cooling period of 72 hours not even AWS can delete the data. However, it can still age out.

## Supported Services
- EC2
- EBS
- EFS, FSx
- [[RDS and Aurora]], [[DynamoDB]], Neptune, DocumentDB.
