---
services:
  - AWS CloudTrail
  - AWS Glue
  - Amazon CloudWatch
tags: ['aws', 'glue', 'logging']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## AWS Glue Logging
###  Active Recall
- What is the interval for continuous logging in AWS Glue?
- What real-time Spark components can be viewed in CloudWatch logs?

---


## Glue in [[CloudWatch and CloudTrail]]

When you start an AWS Glue job, it sends the real-time logging information to CloudWatch (every 5 seconds and before each executor termination) after the [[Spark]] application starts running. You can view the logs on the AWS Glue console or the CloudWatch console dashboard.

The continuous logging feature includes the following capabilities:

- Continuous logging with a default filter to reduce high verbosity in the logs
- Continuous logging with no filter
- A custom script logger to log application-specific messages
- A console progress bar to track the running status of the current AWS Glue job