---
services:
  - Amazon DynamoDB
  - Amazon Kinesis
tags:
  - aws
status: atomic
topic: AWS Data Engineering
domain:
created_at: 2026-01-01T20:45:00
---
## DynamoDB Streams

DynamoDB Streams are ordered streams of [[DynamoDB Fundamentals#Items|item-level]] CRUD operations.

### Active Recall
1. What are the use-cases for DynamoDB Streams?
---

![[DynamoDB.excalidraw]]

### Key Characteristics

### Implementation & Features
*Tip: Link to other services inline (e.g., [[S3]]) to power your Linked Mentions.*

### Use Cases
1. React to changes in real-time. Example - Send welcome email to users.
2. Analytics
3. Insert into derivative tables.
4. Insert into OpenSearch for indexing and providing search functionality over data in DynamoDB.
5. Implement Global tables or Cross Region Replication.

> [!INFO] Exam Tip: Comparison
> *Use this section to distinguish this service from its closest relative or to highlight a critical performance/cost limit.*
