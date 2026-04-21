---
services:
  - AWS IAM
  - AWS Lambda
  - AWS Step Functions
  - Amazon EventBridge
  - Amazon Kinesis
  - Amazon S3
  - Amazon SNS
  - Amazon SQS
tags: ['aws', 's3', 'events']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## S3 Event Notifications
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[S3.excalidraw]]

## Event Notifications

- Advanced filtering options with JSON rules (metadata, object size, name ... )
- Multiple Destinations - ex Step Functions, [[Kinesis Data Streams|Kinesis]] Streams / Firehose, [[SQS]], SNS, [[Lambda]]
- EventBridge Capabilities - Archive, Replay Events, Reliable delivery

![[S3_1#^area=IgilCou7ofyOwe5EwgPqJ]]