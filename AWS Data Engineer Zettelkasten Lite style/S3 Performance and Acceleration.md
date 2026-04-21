---
services:
  - Amazon S3
tags: ['aws', 's3', 'performance']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## S3 Performance and Acceleration

###  Active Recall
- What are the hard limits for requests per second per prefix?
- How does adding "entropy" to a prefix help performance?
- When is Multi-part upload mandatory?

---

## Prefix Throughput Rules
- S3 performance scales automatically by **Prefix**.
- **PUT/COPY/POST/DELETE Limit** -> 3,500 requests/sec per prefix.
- **GET/HEAD Limit** -> 5,500 requests/sec per prefix.

### Performance Optimization Workflow
- **Step 1** -> Evaluate if aggregate request rate exceeds limits (3500/5500).
- **Step 2** -> Redistribute keys across more prefixes.
- **Step 3** -> Add randomized prefixes (e.g., hexadecimal hash) if data has natural "hot prefixes" like dates.

### Example
- **Problem** -> 10,000 GET requests/sec targeting `s3://bucket/2024-12-24/*`.
- **Logic** -> Aggregate rate exceeds 5,500 limit for that single prefix.
- **Solution** -> Distribute data into sub-prefixes -> `s3://bucket/folder1/*` and `s3://bucket/folder2/*` -> each now supports 5,500 GETs.

## S3 Transfer Acceleration
- Uses **AWS Edge Locations** to route data over the private AWS network.
- Path -> Source -> Edge Location -> AWS Private Backbone -> Target S3 Bucket.
- **Use Case** -> Fast long-distance uploads (e.g., cross-continent).

## Multi-part Upload
- **Mandatory** -> Files greater than 5 GB.
- **Recommended** -> Files greater than 100 MB.
- **Workflow** -> Break file into parts -> Upload in parallel -> S3 consolidates on completion.
- **Benefit** -> Higher throughput and resilience to network failure.
