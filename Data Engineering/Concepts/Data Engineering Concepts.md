# Priority Queues
Heaps are the most efficient way to implement a priority queue.
 - *insert(element)*: O(logN)
 - *extract_min()*: O(logN)
 - *peek_min()*: O(1)

This can also be done using -
 - *sorted arrays*: insert(element) - O(n), extract(highest priority element) - O(1)
 - *unsorted arrays*: insert(element) - O(1), extract(highest priority element) - O(n)

# Hashmap collision resolution strategies
| **Area**                                | **Collision Impact**                                  | **Mitigation Strategies**                                                                                                    |
| --------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **ETL Deduplication**                   | Dropping valid records (false positives)              | - Use strong, non-truncated hashes (e.g., SHA-256)  <br>- Store and compare full records <br>- Validate duplicates post-hash |
| **Stream Processing**                   | Incorrect state updates, duplicate suppression errors | - Use full unique keys when tracking state <br>- Validate event IDs directly, not just hashes                                |
| **Partitioning**                        | Hot partitions, load imbalance, bottlenecks           | - Use high-quality hash functions<br>- Monitor for partition skew <br>- Implement custom partitioners                        |
| **Window Aggregations / Joins**         | Aggregated metrics may mix data from unrelated keys   | - Ensure strong key uniqueness <br>- Avoid short or lossy hashes <br>- Validate joined keys with secondary checks            |
| **Bloom Filters / Probabilistic Dedup** | False positives due to hash collisions                | - Use with awareness of trade-offs <br>- Tune filter size and hash functions <br>- Combine with exact filters if possible    |

