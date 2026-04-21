---
services:
  - Amazon EBS
  - Amazon EMR
  - Amazon S3
tags: ['aws', 'emr', 'storage']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon EMR Storage Options
###  Active Recall
- What are the key cost drivers or pricing models for this service?

---
## Storage

### HDFS
- Multiple copies across cluster instances for redundancy.
- Files stored as blocks 128MB default.
- Ephemeral - HDFS data is lost when cluster is terminated.
	- Unlike Hadoop, it is not a good idea to keep the EMR cluster running forever as it is charged by the minute and as soon as the cluster is terminated the data is lost.

The `MSCK REPAIR TABLE` command is used to synchronize the metadata of a table with the actual data layout in the file system. When new data is added directly to HDFS, Hive is not aware of the new partitions. This is because Hive requires metadata about partitions to be updated in its metastore, which doesn’t happen when data is added directly to HDFS.

Running `MSCK REPAIR TABLE` scans the file system for new partitions that were added after the table was created. It then compares the partitions in the table metadata and the partitions in the file system. If new partitions are present in the file system that are not in the table metadata, it adds those partitions to the metadata and to the Hive table.

### EMRFS
- Uses [[AWS Data Engineer/S3]] as if it were HDFS
- Persistent Storage

### Local File System
- Ephemeral - Suitable for caching only.

### EBS
- Allows use of EMR on EBS-only type instances.
- Ephemeral
- EBS volumes can only be attached when launching a cluster, resize not possible.
- Detaching a volume while it is running - **EMR will replace it and is resilient to this**