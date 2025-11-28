## Overview
Key resources for self-hosting a ClickHouse cluster with a focus on performance and fault tolerance.

## Key Areas & Resources

### 1. Deployment and Scaling
* Provides working deployment examples.
* **Resource:** [Manage and Deploy index](https://clickhouse.com/docs/guides/manage-and-deploy-index)

### 2. Sizing and Hardware Recommendations
* Discusses hardware, compute, memory, and disk configurations.
* **Resource:** [Manage and Deploy index](https://clickhouse.com/docs/guides/manage-and-deploy-index)

### 3. Replication and Fault Tolerance
* **ClickHouse Keeper:** Essential for managing replication.
    * **Resource:** [Configuring ClickHouse Keeper](https://clickhouse.com/docs/guides/manage-and-deploy-index)
* **Replication:** The `ReplicatedMergeTree` engine is fundamental.
    * Example Guide: [Replicating a single shard across two AWS regions using S3 Object Storage](https://clickhouse.com/docs/integrations/s3#replicating-a-single-shard-across-two-aws-regions-using-s3-object-storage) (Concepts apply even if not using S3).
    * FAQ: [Does ClickHouse support multi-region replication?](https://clickhouse.com/docs/guides/manage-and-deploy-index)
* **Zero-Copy Replication:** Note considerations mentioned in the S3 replication guide regarding `allow_remote_fs_zero_copy_replication`.

### 4. Sharding for Performance and Scalability
* **Resource:** [Re-balancing Shards](https://clickhouse.com/docs/guides/manage-and-deploy-index)
* The Uber case study discusses sharding (`Distributed` table engine) for scaling.

### 5. Performance Optimization
* **Resource:** [Usage Recommendations](https://clickhouse.com/docs/guides/manage-and-deploy-index)
* **Resource:** [Caches](https://clickhouse.com/docs/guides/manage-and-deploy-index)
* The Microsoft case study mentions custom optimizations (Joiner Optimizer, Condition Optimizer, Time Zone Optimizer).
* The Uber case study discusses schema design, adaptive indexing (materialized columns), and query optimization.

### 6. Storage Strategies
* Using S3 for tiered storage or as primary storage with MergeTree tables can impact performance and cost.
* **Resource:** [S3 Backed MergeTree](https://clickhouse.com/docs/integrations/s3#s3-backed-mergetree)
* **Resource:** [Separation of Storage and Compute](https://clickhouse.com/docs/guides/manage-and-deploy-index)

### 7. Monitoring
* Essential for understanding performance bottlenecks.
* **Resource:** [Monitoring](https://clickhouse.com/docs/guides/manage-and-deploy-index)

### 8. Backup and Restore
* Crucial for fault tolerance.
* **Resource:** [Backup and Restore](https://clickhouse.com/docs/guides/manage-and-deploy-index)
