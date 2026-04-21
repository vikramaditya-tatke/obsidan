---
services:
  - Amazon S3
tags: ['aws', 's3', 'storage-classes']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Active Recall
- What are the key cost drivers or pricing models for this service?

---

## S3 Storage Classes

| Feature                          | Standard               | Intelligent-Tiering    | Standard-IA             | One Zone-IA             | Glacier Instant Retrieval | Glacier Flexible Retrieval | Glacier Deep Archive   | [[S3 Express One Zone]]     |
| -------------------------------- | ---------------------- | ---------------------- | ----------------------- | ----------------------- | ------------------------- | -------------------------- | ---------------------- | --------------------------- |
| **Durability**                   | 99.999999999% (11 9’s) | 99.999999999% (11 9’s) | 99.999999999% (11 9’s)  | 99.999999999% (11 9’s)  | 99.999999999% (11 9’s)    | 99.999999999% (11 9’s)     | 99.999999999% (11 9’s) | 99.95%                      |
| **Availability**                 | 99.99%                 | 99.9%                  | 99.9%                   | 99.5%                   | 99.9%                     | 99.99%                     | 99.99%                 | 99.95%                      |
| **Availability SLA**             | 99.9%                  | 99%                    | 99%                     | 99%                     | 99%                       | 99.9%                      | 99.9%                  | 99.9%                       |
| **Availability Zones**           | ≥ 3                    | ≥ 3                    | ≥ 3                     | 1                       | ≥ 3                       | ≥ 3                        | ≥ 3                    | 1                           |
| **Min. Storage Duration Charge** | None                   | None                   | 30 Days                 | 30 Days                 | 90 Days                   | 90 Days                    | 180 Days               | None                        |
| **Min. Billable Object Size**    | None                   | None                   | 128 KB                  | 128 KB                  | 128 KB                    | 40 KB                      | 40 KB                  | None                        |
| **Retrieval Fee**                | None                   | None                   | Per GB retrieved        | Per GB retrieved        | Per GB retrieved          | Per GB retrieved           | Per GB retrieved       | None                        |
| **Data Retrieval Time**          | Milliseconds           | Milliseconds           | Milliseconds to seconds | Milliseconds to seconds | Milliseconds              | Minutes to hours           | Hours (up to 12 hours) | **Sub-millisecond (<1 ms)** |
