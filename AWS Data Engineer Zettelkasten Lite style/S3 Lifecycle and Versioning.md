---
services:
  - Amazon S3
tags: ['aws', 's3', 'lifecycle', 'versioning']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## S3 Lifecycle and Versioning
###  Active Recall
- How is data secured or encrypted in this context?

---

## Lifecycle Policy

![[Pasted image 20251008163033.png]]

## Versioning

It refers to keeping multiple variants of an object in the same bucket

- Allows to retrieve and restore every version of every object
- Recovery from unintended user actions and application failures.
## Replication

- Only works if [versioning](#versioning) is enabled on both origin and target buckets.
- SRR and CRR
- If [Encryption](#Encryption) is modified when versioning is enabled, a new object is created.