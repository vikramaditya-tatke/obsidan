---
services:
  - AWS Lambda
  - Amazon S3
tags: ['aws', 's3', 'lambda']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Active Recall
- How does this service integrate with other AWS components mentioned?

- Why not just use standard AWS Lambda and point it towards the S3 object instead of using S3 Object Lambda?

	- **Client Compatibility**: Standard Lambda requires rewriting the client application to call an API Gateway or Lambda URL. S3 Object Lambda allows the client to keep making standard S3 `GET` requests, just pointing to a different ARN (Access Point).
	- **Coupling**: Standard Lambda tightly couples the retrieval logic with the transformation logic in a custom API layer. S3 Object Lambda abstracts this, keeping the interface as "Standard Storage".

---

S3 Access point is connected to [[Lambda]] Function, which redacts the object as it is being retrieved.

The Lambda functions has it's own access point called the **S3 object [[Lambda]] Access Point**.

![[Excalidraw/S3]]

![[Excalidraw/S3|S3]]

![[Excalidraw/S3]]

### S3 Object Lambda vs. Standard Lambda Proxy

| Feature | Standard Lambda (Proxy Approach) | S3 Object Lambda |
| :--- | :--- | :--- |
| **Invocation** | Client calls API Gateway / Lambda URL | Client calls S3 `GET` (via Access Point) |
| **Client Code Impact** | **High**: Must rewrite code to call new API endpoints instead of S3 SDK methods. | **Low**: Minimal change; just swap the Bucket Name for the Object Lambda Access Point ARN. |
| **Workflow** | Request -> API GW -> Lambda -> S3 -> Lambda -> Client | Request -> S3 OLAP -> Lambda -> Client |
| **Best For** | Complex business logic, async processing, non-S3 triggers. | Simple on-the-fly transformations (Redaction, Unzipping, Format conversion) without breaking existing S3 clients. |