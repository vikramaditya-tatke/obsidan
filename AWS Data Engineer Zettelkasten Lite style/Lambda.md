---
services:
  - AWS IAM
  - AWS Lambda
  - Amazon Kinesis
  - Amazon S3
tags: ['aws', 'lambda']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Lambda
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?
- What is the difference between create_partition API and enableUpdateCatalog?

---

Lambda is *completely serverless* is used for executing code snippets and continuous scaling.

- Used as an intermediary between various data services.
- Transformation jobs, such as receiving data from [[Kinesis Data Streams]], transforming it and sending it back or to a data warehouse.
#### Example of a Serverless Website
![[Excalidraw/Lambda Serverless Website]]

> In the context of using Lambda with streaming services like [[Kinesis Data Streams]] and MSK, these services CANNOT write the data into Lambda. **Instead Lambda polls these services periodically.**
## Lambda Triggers

![[Pasted image 20251101200028.png]]