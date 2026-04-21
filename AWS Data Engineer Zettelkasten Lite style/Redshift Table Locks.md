---
services:
  - AWS IAM
  - Amazon Redshift
  - Amazon S3
tags: ['aws', 'redshift', 'locks']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Redshift Table Locks
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

## Locks

> Amazon Redshift uses table-level locks. You might experience locking conflicts if you perform frequent DDL statements on user tables or DML queries.

1. **AccessExclusiveLock:** During DDL operations, such as `ALTER TABLE`, `DROP`, or `TRUNCATE`. AccessExclusiveLock blocks all other locking attempts.
2. **AccessShareLock:** Acquired during `UNLOAD`, `SELECT`, `UPDATE`, or `DELETE` operations. AccessShareLock blocks only `AccessExclusiveLock` attempts. AccessShareLock doesn’t block other sessions that are trying to read or write on the table.
3. **ShareRowExclusiveLock:** Acquired during `COPY`, `INSERT`, `UPDATE`, or `DELETE` operations. `ShareRowExclusiveLock` blocks `AccessExclusiveLock` and other `ShareRowExclusiveLock` attempts but doesn’t block `AccessShareLock` attempts.