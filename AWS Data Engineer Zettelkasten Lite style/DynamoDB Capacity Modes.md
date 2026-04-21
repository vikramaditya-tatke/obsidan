---
services:
  - Amazon DynamoDB
tags: ['aws', 'dynamodb']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## DynamoDB Capacity Modes

![[DAX Elasticache]]

###  Active Recall
- What is the specific rounding rule for WCU vs RCU?
- How does the "Eventually Consistent" multiplier affect the final RCU count?
- When does a single item consume more than 1 unit?

---

## Provisioned Mode
- Capacity is dedicated to the table.
- **WCU Base** -> 1 write/sec -> 1 KB limit.
- **RCU Base (Strong)** -> 1 read/sec -> 4 KB limit.
- **RCU Base (Eventual)** -> 2 reads/sec -> 4 KB limit.

### Calculation Workflow
**Step 1** -> Round item size up to nearest 1 KB (WCU) or 4 KB (RCU).
**Step 2** -> Divide rounded size by the base limit (1 KB or 4 KB) -> Units per item.
**Step 3** -> Multiply by number of items per second.
**Step 4** -> If Eventually Consistent -> Divide result by 2.

### WCU Calculation Examples
- **Example 1** -> 10 items/sec -> 2 KB item.
    - (2 KB / 1 KB) * 10 -> **20 WCU**.
- **Example 2** -> 6 items/sec -> 4.5 KB item.
    - 4.5 rounds up to 5 -> (5 KB / 1 KB) * 6 -> **30 WCU**.

### RCU Calculation Examples
- **Example 1** -> 10 strongly consistent reads/sec -> 4 KB item.
    - (4 KB / 4 KB) * 10 -> **10 RCU**.
- **Example 2** -> 16 eventually consistent reads/sec -> 12 KB item.
    - (12 KB / 4 KB) * 16 -> 48 total.
    - Eventually consistent -> 48 / 2 -> **24 RCU**.

## On-demand Mode
- No capacity planning required.
- Cost -> Roughly 2.5x price per unit vs provisioned.
- Capacity -> Unlimited (bursts to 2x previous peak).
- **WRU (Write Request Unit)** -> Matches WCU logic.
- **RRU (Read Request Unit)** -> Matches RCU logic.
