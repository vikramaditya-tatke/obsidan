---
services:
  - AWS IAM
  - AWS IoT Core
  - Amazon Kinesis
  - Amazon S3
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## IoT Core
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

AWS IoT Core is a purpose built solution to integrate with low-power low memory IoT devices, which provides a message broker to publish and subscribe to messages using *MQTT and MTQQ over WSS* protocols.

## IoT Rules

IoT rules can be used to point the data stream (per MQTT topic ) to various AWS services such as [[Kinesis Data Firehose]], [[Kinesis Data Streams]] and [[MSK]].