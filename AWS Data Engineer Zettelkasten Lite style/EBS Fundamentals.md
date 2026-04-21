---
services:
  - AWS IAM
  - Amazon EBS
  - Amazon EC2
  - Amazon S3
tags: ['aws', 'ebs', 'storage']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon EBS Fundamentals
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---
## EBS
- *Elastic Block Storage*
- Like [[EC2]] instances, these are locked to a single AZ.
- Can only be attached to 1 [[EC2|EC2]] instance.
- Delete on Termination - If the [[EC2|EC2]] instance is terminated -
	- the root EBS volume is terminated by default.
	- other attached EBS volumes are NOT terminated by default.
- **Elastic Block Volumes**: Modify volumes without downtime.
	- Increase capacity
	- Modify IOPS