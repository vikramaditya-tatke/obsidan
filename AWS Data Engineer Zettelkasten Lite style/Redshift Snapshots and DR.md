---
services:
  - AWS Backup
  - AWS CloudTrail
  - AWS IAM
  - AWS Lambda
  - Amazon EventBridge
  - Amazon Redshift
  - Amazon S3
  - Amazon VPC
tags: ['aws', 'redshift', 'dr', 'snapshots']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Redshift Snapshots and DR
###  Active Recall
- What are the key cost drivers or pricing models for this service?
- How is data secured or encrypted in this context?

---

![[RedShift]]

## Snapshots and Cross-Region Replication

### Automated Snapshots
- Taken automatically every 8 hours or after 5 GB of changes per node
- Default retention period: 1 day (configurable up to 35 days)
- Stored internally in Amazon [[Amazon S3 Fundamentals|S3]] (no additional storage charges)
- Cannot be manually deleted - lifecycle managed by Redshift
- Incremental backups capturing only changed blocks since last snapshot
- Automatically deleted when cluster is deleted (unless final snapshot taken)
- [[Backup]] window can be configured to minimize performance impact

## Manual Snapshots
- User-initiated snapshots retained indefinitely until explicitly deleted
- Storage charges apply (standard [[Amazon S3 Fundamentals|S3]] rates)
- Common use cases:
	- Long-term backup retention beyond 35 days
	- Pre-migration or pre-upgrade backups
	- Dev/test environment creation
	- Compliance and audit requirements
- Can be taken at any time without affecting cluster availability
- Support for snapshot scheduling using AWS [[Lambda]] or EventBridge
- Final snapshot option available when deleting a cluster

## Cross-Region Snapshot Copy
- Automated or manual snapshots can be copied to different AWS regions
- Primary use cases:
	- Disaster recovery and business continuity
	- Regional compliance and data residency requirements
	- Multi-region analytics and reporting
- Configuration options:
	- Source region and destination region selection
	- Retention period for copied snapshots (independent from source)
	- Copy grant for KMS-encrypted snapshots
	- Automated copy vs. manual copy
- Data transfer charges apply for cross-region copies
- Copied snapshots are independent and can be restored separately
- Supports cascading copies to multiple regions

## Snapshot Restoration
- Restore creates a new cluster with snapshot data
- Restoration options:
	- Full cluster restore from snapshot
	- Table-level restore (without full cluster restore)
	- Restore to different node type or cluster configuration
- Restored cluster considerations:
	- Must have same or greater number of nodes
	- Network configuration ([[VPC Networking Fundamentals|VPC]], subnet, security groups)
	- Parameter groups and cluster settings
- Restoration time varies based on data volume and cluster size
- Can restore across AWS accounts (with proper sharing)

## Snapshot Sharing
- Manual snapshots can be shared with other AWS accounts
- Sharing process:
	- Authorize target AWS account to access snapshot
	- Target account can restore to new cluster
	- Both accounts must be in the same region
- Encryption requirements:
	- Unencrypted snapshots can be shared directly
	- Encrypted snapshots require KMS key sharing
	- Create snapshot copy grant for cross-account KMS access
- Use cases:
	- Dev/test environment provisioning
	- Data sharing with partners or subsidiaries
	- Multi-account architectures

## Snapshot Security and Encryption
- Automated snapshots inherit cluster encryption configuration
- KMS encryption for snapshots at rest
- Manual snapshots can be encrypted during copy operation
- Encryption key management:
	- AWS-managed keys or customer-managed keys (CMK)
	- Key policies control snapshot access
	- Cross-region copies require key in destination region
- [[AWS IAM]] policies control snapshot operations:
	- Create, delete, copy, restore, share permissions
	- Resource-level permissions for granular control
- Audit trail via CloudTrail for snapshot operations

## [[Backup]] And Recovery Best Practices
- Cost optimization:
	- Manual snapshots incur [[Amazon S3 Fundamentals|S3]] storage costs
	- Cross-region transfer and storage charges
	- Implement retention policies to manage costs
	- Delete obsolete snapshots regularly
- [[Backup]] strategy:
	- Automated snapshots for short-term recovery (≤35 days)
	- Manual snapshots for long-term retention
	- Cross-region copies for disaster recovery
	- Test restore procedures regularly
- Recovery Time Objective (RTO) considerations:
	- Snapshot restoration time depends on data volume
	- Consider Redshift Serverless for faster scaling
	- Multi-AZ deployments for high availability
- Compliance and governance:
	- Document retention policies
	- Implement automated snapshot scheduling
	- Tag snapshots for cost allocation and lifecycle management