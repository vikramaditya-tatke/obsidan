---
services:
  - AWS IAM
  - Amazon CloudWatch
  - Amazon EC2
  - Amazon EMR
  - Amazon Managed Service for Apache Flink
  - Amazon S3
  - Amazon VPC
tags: ['aws', 'emr']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon EMR Fundamentals
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[Apache [[Spark]] 2025-10-10 16.35.14.excalidraw]]

- Managed Hadoop Framework, running on [[EC2]]
- [[Spark]], HBase, Presto, Flink, Hive.
	- **Since these are installed on [[EC2|EC2]], we can get down and dirty by customizing the installation of any of the installed services**
- EMR Notebooks for running code.
- Transient Cluster - Terminates after all steps are complete.
- [[VPC Networking Fundamentals|VPC]] is used to launch the cluster of [[EC2|EC2]] instances (EMR)
- Integrates with CloudWatch
- AWS [[AWS IAM]] to configure permissions for EMR
- AWS Data Pipeline can be used to orchestrator. Useful when creating transient clusters as a part of a larger pipeline.