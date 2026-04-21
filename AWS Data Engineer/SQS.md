# Types of SQS queues
- **Standard Queues:**
- **FIFO Queues:**
- **Delay Queue:** These queues can add messages in an invisible state so as to delay these messages before they reach the consumers.  
- **Dead Letter Queues:** Used to process problematic messages that appear more than `maxReceiveCount` number of times in the queue. A single dead letter queue can be used for multiple queues.

## Standard Vs FIFO queues

| **Standard Queue** | **FIFO Queues** |
| ------------------ | --------------- |
|                    |                 |

# Concepts
##### Visibility Timeout
##### maxReceiveCount
##### Enqueue Timestamp
##### SendMessage 
Operation used to *put* the message in the queue.
##### ReceiveMessage 
Operation used to *pull* the message from the queue.
##### Redrive Policy
Specifies the source queue, the dead-letter queue and the conditions under which the messages will be moved from the source queue -> dead letter queue.

> Retention period of a dead letter queue should be longer than the source queue. It should consider the Enqueue Timestamp as this **IS NOT** changed when the message is put into the dead letter queue.