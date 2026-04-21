---
services:
  - AWS IAM
  - Amazon EMR
  - Amazon S3
tags: ['aws', 'emr', 'scaling', 'serverless']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon EMR Scaling and Serverless
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[Apache Spark]]

## EMR Managed Scaling
- [[Spark]], Hive or YARN
- Support for instance groups and fleets
- Spot, on-demand, etc.

## Serverless

- No need for capacity planning - Just choose the runtime ([[Spark]], Hive, Presto, etc..)
- [[Spark]] adds a 10% overhead to memory requested for drivers and executors.
- The states need to be triggered via API calls and are not automatic - Create, Start, Stop, Shutdown Terminate, etc..

### EMR on EKS

- Submitting [[Spark]] job on EKS without provisioning clusters
- Fully managed, no need to provision any resources
- Shares resources between [[Spark]] and other apps on Kubernetes.