---
services:
  - Amazon DynamoDB
  - Amazon S3
tags:
  - aws
status:
  - atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-25T17:45:00
---
## DynamoDB Fundamentals

- DynamoDB is a highly resilient, DBaaS (Database as a Service).
- It is a [[Public vs Private AWS Services|Public Service]].
- DynamoDB is backed by SSDs.
- Tables are the base entity within DynamoDB.
- [[DynamoDB Capacity Modes|Capacity]] in DynamoDB refers to the performance it can provide and not to the actual storage used by the service.

### Active Recall

1. What are the differences between LSI and GSI? What is the need to implement them?
## Key Characteristics

### Primary Keys

Primary Keys must be unique within DynamoDB. They can be either of the two following types:

1. Simple Partition Key (PK): The PK must be unique
2. Composite Key (PK + Sort Key): The PK + SK, combination must be unique.

### Items
1. A table can have an infinite number of items.
2. Each item can be up to 400KB.
3. It can have either *all*, *mixture*, *none* or different attributes.

### IO Operations

| **PutItem** | **UpdateItem** | **GetItem** |
| ----------- | -------------- | ----------- |
|             |                |             |

**BatchWriteItem**
- Up to 25 `PutItem` and/or `DeleteItem` in each call
- Up to 16 MB of data written, 400KB max per item.

**BatchGetItem**
- Returns items from one or more tables.
- Up to 100 items - up to 16MB of data.
- Items are retrieved parallelly.

> Incase there are any UnprocessedKeys for failed read operations - could be due to insufficient RCU capacity, exponential backoff strategy is used to read those keys again.

> [!INFO] Exam Tip
> *If NoSQL/Key-Value mentioned in DynamoDB always default to answering `DynamoDB` unless there is a strong reason not to.*

## PartiQL
- PartiQL is SQL-compatible query language for DynamoDB.
- Instead of using DynamoDB API calls, we use PartiQL - *joins are not supported*.

## Indexes

| Local Secondary Index (LSI)                                                                                         | Global Secondary Index (GSI)                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Must be defined at table creation time.                                                                             | Can be added or modified after table creation.                                                                                               |
| Alternative sort key with the same primary key as the base table.                                                   | Alternative Primary Key (HASH / HASH + Range) from the base table.                                                                           |
| **Attribute Projection**: Can contain some or all of the attributes of the base table.<br>- KEYS_ONLY, INCLUDE, ALL | **Attribute Projection**: Can contain some or all of the attributes of the base table.<br>- KEYS_ONLY, INCLUDE, ALL                          |
| Maximum 5 per table.                                                                                                |                                                                                                                                              |
| Uses existing RCUs and WCUs of the base table.                                                                      | Need to provision additional RCUs and WCUs for the GSI specifically.                                                                         |
| No throttling considerations.                                                                                       | If the GSI throttles due to less RCUs or WCUs, the base table throttles as well - ** even if the RCUs and WCUs on the base table are fine.** |
