---
services:
  - AWS Lambda
  - Amazon EC2
  - Amazon EFS
tags: ['aws', 'efs', 'storage']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon EFS Fundamentals
###  Active Recall
- How does this service integrate with other AWS components mentioned?

---
## EFS
 - Per as you go
 - No need to pre-allocate capacity and IOPS
 - Cross AZs
 - Can be connected to multiple [[EC2|EC2]] instances.
 - Only for Linux Instances.
 - Supports the NFSv4 protocol, which allows for seamless integration with existing application and workflows that rely on NFS.
 - [[Lambda]] can directly integrate with EFS, providing concurrent access to the shared data.