- Managed Hadoop Framework, running on [[EC2]]
- Spark, HBase, Presto, Flink, Hive.
	- **Since these are installed on EC2, we can get down and dirty by customizing the installation of any of the installed services**
- EMR Notebooks for running code.
- Transient Cluster - Terminates after all steps are complete.
- [[VPC]] is used to launch the cluster of EC2 instances (EMR)
- Integrates with CloudWatch
- AWS IAM to configure permissions for EMR
- AWS Data Pipeline can be used to orchestrator. Useful when creating transient clusters as a part of a larger pipeline.

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


## EMR Managed Scaling
- Spark, Hive or YARN
- Support for instance groups and fleets
- Spot, on-demand, etc.

## Serverless

- No need for capacity planning - Just choose the runtime (Spark, Hive, Presto, etc..)
- Spark adds a 10% overhead to memory requested for drivers and executors.
- The states need to be triggered via API calls and are not automatic - Create, Start, Stop, Shutdown Terminate, etc..  

#### EMR on EKS

- Submitting Spark job on EKS without provisioning clusters
- Fully managed, no need to provision any resources
- Shares resources between Spark and other apps on Kubernetes.