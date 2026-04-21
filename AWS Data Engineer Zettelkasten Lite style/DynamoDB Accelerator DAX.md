---
services:
  - AWS CloudTrail
  - AWS IAM
  - Amazon DynamoDB
tags: ['aws', 'dynamodb', 'dax']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## DynamoDB Accelerator (DAX)
###  Active Recall
- What are the latency characteristics mentioned for this service/feature?
- How is data secured or encrypted in this context?

---

![[DAX Elasticache]]

## DAX DynamoDB Accelerator

- Fully Managed highly, available in-memory cache.
- Microseconds latency for cached reads and queries
- Used to solve the **Hot Key** problem
- TTL: 5 minutes by default
- Up to 10 nodes in the cluster
- Multi-AZ (3 nodes recommended for production)
- Secure
	- Encryption at rest
	- VPN
	- [[AWS IAM]]
	- CloudTrail, etc.

![[DAX Elasticache]]