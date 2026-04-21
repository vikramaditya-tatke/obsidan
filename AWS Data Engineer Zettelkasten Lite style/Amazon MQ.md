---
services:
  - AWS IAM
  - Amazon MQ
  - Amazon S3
  - Amazon VPC
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon MQ
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

It is an open-source message broker based on Apache ActiveMQ that supports protocols such as AQMP, MQTT, OpenWire, STOMP, etc.

- Provides *Queues* and *Topics*
- Message broker servers can be in a Test/Dev setup or a HA pair for production-grade setup.

> It is a [[Public vs Private AWS Services|private service]] meaning it is [[VPC Networking Fundamentals|VPC]] based and requires private networking.
