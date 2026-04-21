---
services:
  - Amazon SQS
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## SQS
###  Active Recall
- Are there any critical limits or quotas to be aware of?

---


## Types of SQS Queues
- **Standard Queues:**
- **FIFO Queues:**
- **Delay Queue:** These queues can add messages in an invisible state so as to delay these messages before they reach the consumers.
- **Dead Letter Queues:** Used to process problematic messages that appear more than `maxReceiveCount` number of times in the queue. A single dead letter queue can be used for multiple queues.

### Standard Vs FIFO Queues

| **Standard Queue** | **FIFO Queues** |
| ------------------ | --------------- |
|                    |                 |

## Concepts
### Visibility Timeout
- **Definition**: The period a message remains "invisible" to other consumers after being picked up by one consumer.
- **Goal**: Prevents multiple consumers from processing the exact same message simultaneously.
- **Limits**:
    - Default: 30 seconds.
    - Min: 0 seconds.
    - Max: 12 hours.
- **Behavior**:
    - If processing completes -> Consumer deletes message.
    - If processing fails/crashes -> Timeout expires -> Message becomes visible again.
- **Important**: If your application needs more time than the default, you must extend the visibility timeout using `ChangeMessageVisibility` or increase the queue default; otherwise, you'll get duplicate processing.

### maxReceiveCount
- **Definition**: The threshold for how many times a message can be "received" (picked up) before SQS gives up and moves it to a **Dead Letter Queue (DLQ)**.
- **Goal**: Handles "poison pill" messages (malformed data that causes consumer crashes) so they don't block the queue forever.
- **Relationship**:
    - Every time the Visibility Timeout expires and the message reappears, the `ReceiveCount` increments.
    - When `ReceiveCount > maxReceiveCount`, the message is moved to the DLQ.
- **Exam Tip**: Setting this too low (e.g., 1) prevents retries for transient errors. Setting it too high wastes resources on bad messages.

### Enqueue Timestamp
### SendMessage

Operation used to *put* the message in the queue.

### ReceiveMessage

Operation used to *pull* the message from the queue.

### Redrive Policy

Specifies the source queue, the dead-letter queue and the conditions under which the messages will be moved from the source queue -> dead letter queue.

> Retention period of a dead letter queue should be longer than the source queue. It should consider the Enqueue Timestamp as this **IS NOT** changed when the message is put into the dead letter queue.