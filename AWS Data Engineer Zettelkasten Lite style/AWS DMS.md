---
services:
  - AWS DMS
  - Amazon RDS
  - Amazon Aurora
  - Amazon S3
  - Amazon Redshift
  - Amazon DocumentDB
  - Amazon Neptune
  - AWS KMS
tags: ['aws', 'dms', 'migration', 'cdc']
status: atomic
topic: AWS Data Engineering
domain: Data Ingestion and Transformation
created_at: 2025-12-29
---
## AWS Database Migration Service (DMS)

###  Active Recall
- What's the difference between full load and CDC?
- How does DMS handle schema conversion?
- What are the source and target options for DMS?
- When should you use homogeneous vs heterogeneous migration?

---

## Core Concepts

**AWS DMS** is a managed service that helps migrate databases to AWS quickly and securely. It supports **both one-time migration** and **ongoing replication** (CDC).

### Migration Types

| Migration Type | Description | Duration | Use Case |
|--------------|-------------|----------|-----------|
| **Full Load** | Migrates all data at once | Initial migration, bulk transfer |
| **CDC (Change Data Capture)** | Ongoing replication of changes | Continuous sync, zero downtime cutover |
| **Full Load + CDC** | Full load then CDC | Most common, minimizes cutover time |

### Homogeneous vs Heterogeneous Migration

| Type | Source | Target | Schema Conversion |
|-------|---------|---------|-------------------|
| **Homogeneous** | Oracle → Oracle | No schema conversion needed |
| **Heterogeneous** | Oracle → Aurora PostgreSQL | **AWS SCT (Schema Conversion Tool)** required |

> [!INFO] **What Does DMS Migrate?**
>  Schema (via AWS SCT for heterogeneous)
>  Data (tables, indexes)
>  Ongoing changes (CDC)
>  Stored procedures, triggers, views (manual effort)

## DMS Architecture

### Components

```
Source DB → Replication Instance → Target DB
   ↓              ↓                  ↓
 CDC Stream     Storage (logs)     Data write
```

**Key Components:**
1. **Source Endpoint:** Connection info to source database
2. **Target Endpoint:** Connection info to target database
3. **Replication Instance:** The DMS engine that performs migration
4. **Task:** The migration job (full load, CDC, or both)

### Replication Instance Sizing

| Instance Class | RAM | Use Case |
|---------------|-----|----------|
| **dms.t3.small** | 2GB | Testing, low throughput |
| **dms.t3.medium** | 4GB | Small migrations (< 1TB) |
| **dms.r5.large** | 16GB | Medium migrations (1-10TB) |
| **dms.r5.2xlarge** | 64GB | Large migrations (>10TB) |

> [!TIP] **Instance Sizing**
> - **CPU-bound:** Many tables, parallel tasks
> - **Memory-bound:** Large tables, complex queries
> - **Network-bound:** Cross-region, high-throughput CDC

## Change Data Capture (CDC)

### How CDC Works

1. **Transaction Logs:** DMS reads transaction logs (binlog, WAL, etc.)
2. **Capture Changes:** Detects INSERT, UPDATE, DELETE operations
3. **Queue Changes:** Changes queued in replication instance
4. **Apply Changes:** Applied to target in transaction order

### CDC Support by Database

| Source | CDC Method | Supported? |
|---------|-------------|-------------|
| **Oracle** | LogMiner |  Yes |
| **Microsoft SQL Server** | CDC feature |  Yes |
| **MySQL** | Binary log |  Yes |
| **PostgreSQL** | WAL (Logical Replication) |  Yes |
| **Amazon Aurora** | Binary log |  Yes |
| **MongoDB** | Oplog |  Yes |
| **DocumentDB** | Oplog |  Yes |

> [!WARNING] **CDC Requirements**
> - **Primary key required** on all tables for CDC
> - **Transaction logging must be enabled** on source
> - **Sufficient permissions** to read logs

### Latency Monitoring

**Metrics to monitor:**
- **CDCLatency:** Time between change in source and DMS capture
- **ApplyLatency:** Time between DMS capture and target apply
- **TargetLatency:** Target database write performance

> [!EXAM] **High CDC Latency Causes**
> 1. Target database overloaded (slow writes)
> 2. Network bandwidth (cross-region)
> 3. Insufficient replication instance resources
> 4. Too many tables in single task (parallelize)

## Supported Sources and Targets

### Source Databases
- **Amazon RDS** (all engines)
- **Amazon Aurora**
- **On-premises Oracle**
- **On-premises SQL Server**
- **On-premises MySQL, PostgreSQL**
- **MongoDB**
- **Amazon DocumentDB**
- **Amazon S3** (as source for DMS)

### Target Databases
- **Amazon RDS** (all engines)
- **Amazon Aurora**
- **Amazon S3** (data lake export)
- **Amazon Redshift** (data warehouse)
- **Amazon DynamoDB** (NoSQL)
- **Amazon Kinesis Data Streams** (streaming)
- **Amazon ElastiCache**
- **Amazon Neptune** (graph database)

> [!INFO] **S3 as Target**
> - Parquet format (recommended)
> - Partitioned data (date, time)
> - Useful for data lake migration
> - Can use Lake Formation for governance

## Task Configuration

### Task Settings

**Full Load Settings:**
- **Batch size:** Records per batch (default: 10,000)
- **Max full load subtasks:** Parallel tables (default: 8)
- **Commit rate:** Frequency of commits (default: 10000 records)
- **LOB max size:** Limit for large objects

**CDC Settings:**
- **Max number of files:** Parallel CDC files
- **Transaction apply timeout:** Timeout for applying transactions
- **Control tables:** DMS tracking tables

### Task Types

| Task Type | Description | When to Use |
|-----------|-------------|---------------|
| **Migrate existing data** | Full load only | One-time migration, no ongoing sync |
| **Replicate data changes only** | CDC only | Initial data already migrated, only sync changes |
| **Migrate existing data and replicate ongoing changes** | Full + CDC | **Most common**, zero downtime |

## Data Transformation

### Supported Transformations
- **Column renaming:** Map source columns to target columns
- **Filtering:** Exclude certain tables/rows
- **Type conversion:** Data type mapping (e.g., VARCHAR → NVARCHAR)
- **Table mapping:** Schema transformation
- **LOB handling:** Handle large objects

### AWS Schema Conversion Tool (SCT)

**Purpose:** Convert database schema from one engine to another

**Supported Conversions:**
- Oracle → PostgreSQL/Aurora
- SQL Server → PostgreSQL/Aurora
- MySQL → PostgreSQL
- Oracle → MySQL

**Features:**
- **Assessment report:** What's compatible vs. needs manual changes
- **Automatic conversion:** Scripts for schema migration
- **Data type mapping:** Automatic type conversion

> [!WARNING] **SCT Limitations**
> - Stored procedures: Manual conversion
> - Triggers: Manual conversion
> - Views: Manual review and conversion
> - Complex business logic: May need application changes

## Security and Encryption

### Encryption at Rest
- **Source connection:** Encrypted using SSL/TLS
- **Target connection:** Encrypted using SSL/TLS
- **Replication instance:** EBS encrypted by default
- **Storage:** Encrypted using KMS

### IAM Permissions
**DMS service role requires:**
```json
{
  "Effect": "Allow",
  "Action": [
    "dms:*",
    "kms:Decrypt",
    "kms:GenerateDataKey",
    "ec2:CreateNetworkInterface",
    "ec2:DeleteNetworkInterface"
  ],
  "Resource": "*"
}
```

### VPC Configuration
- **Replication instance** in VPC (recommended)
- **Source/target connectivity:**
  - Same VPC: Direct connection
  - Different VPC: VPC peering or VPN
  - On-premises: VPN or Direct Connect
  - Internet: Security group + NACL for DMS ports

## Performance Optimization

### Parallelism

**Task-level parallelism:**
- **Full load:** Max subtasks (default: 8, up to 49)
- **CDC:** Parallel threads (default: 5, up to 8)

**Task parallelism:**
- **Multiple tasks** for different table groups
- **Each task** uses separate replication instance resources

> [!TIP] **Parallelism Strategy**
> - Partition tables by size (small vs. large)
> - Separate high-throughput tables into own tasks
> - Group related tables to maintain referential integrity

### Tuning Settings

**For high-throughput CDC:**
1. Increase `maxFileSizeMB` (default: 32MB, up to 128MB)
2. Increase `maxFileSize` for large transactions
3. Increase replication instance size (CPU/RAM)
4. Use **DMS Fleet Advisor** to optimize

## Monitoring and Troubleshooting

### CloudWatch Metrics

| Metric | What It Shows | Alarm Threshold |
|--------|----------------|-----------------|
| **CDCLatency** | Delay in capturing changes | > 5 minutes (check source) |
| **CDCLatency** | Delay in applying changes | > 10 minutes (check target) |
| **FullLoadProgressPercent** | Full load completion | Monitor for progress |
| **FreeStorageSpace** | Replication instance storage | < 10% (resize) |

### Common Issues

**Issue 1: High CDC Latency**
**Symptoms:** CDC falling behind real-time

**Solutions:**
- Scale up replication instance
- Increase CDC parallelism (threads)
- Optimize target database (indexes, maintenance)
- Reduce number of tables per task

**Issue 2: Full Load Slow**
**Symptoms:** Full load taking too long

**Solutions:**
- Increase `MaxFullLoadSubtasks`
- Increase commit rate
- Use multiple tasks for table groups
- Check network bandwidth (cross-region)

**Issue 3: Data Type Mismatch**
**Symptoms:** Transformation errors

**Solutions:**
- Review SCT assessment report
- Update task table mappings
- Use type transformation rules
- Manually adjust target schema

## Common Exam Patterns

### Pattern 1: Zero Downtime Migration
**Question:** "Migrate 10TB Oracle database to Aurora PostgreSQL with zero downtime."

**Answer:**
1. Run AWS SCT for schema conversion
2. Create DMS replication instance
3. Start **Full Load + CDC task**
4. Monitor until full load completes
5. Verify CDC replication (near real-time)
6. Cut over application to Aurora
7. Monitor CDC latency during cutover

### Pattern 2: Data Lake Migration
**Question:** "Migrate on-premises SQL Server to S3 data lake."

**Answer:**
- Source: SQL Server
- Target: S3
- Use **Parquet format** for S3
- Enable partitioning (date, time)
- Full load only (CDC not applicable to S3)

### Pattern 3: Cross-Region Migration
**Question:** "Migrate RDS MySQL from us-east-1 to us-west-2 with ongoing sync."

**Answer:**
- Replication instance in source region (us-east-1)
- DMS handles cross-region data transfer
- Monitor network bandwidth (bottleneck)
- Consider AWS Direct Connect for consistent throughput

### Pattern 4: Heterogeneous Migration
**Question:** "Migrate Oracle to Aurora PostgreSQL with stored procedures."

**Answer:**
1. Use AWS SCT for schema conversion
2. Review assessment report for incompatible objects
3. Manual conversion of stored procedures, triggers
4. DMS for data migration (Full + CDC)
5. Application testing after migration

##  Use Cases

### When to Use DMS
1. **Database migrations** (one-time or ongoing)
2. **Zero downtime migrations** using CDC
3. **Continuous replication** for disaster recovery
4. **Heterogeneous migrations** (Oracle → PostgreSQL)
5. **Data lake export** (database → S3/Redshift)
6. **Development/testing** copy of production data

### When DMS is NOT Ideal
1. **Real-time streaming** (< 1 second) → Use Kinesis
2. **Small, frequent migrations** (daily) → Use custom ETL
3. **Complex transformations** → Use AWS Glue
4. **Non-database data sources** (files, APIs) → Use Glue/Step Functions

> [!EXAM] **DMS vs. Glue vs. Native Replication**
> - **DMS:** Database → Database (with/without CDC)
> - **Glue:** Any source → Any target (ETL, complex transforms)
> - **Native (RDS/Aurora):** Same engine → Same engine, fastest

---
## Related Services
- [[AWS Glue Fundamentals]] (ETL, complex transformations)
- [[RDS and Aurora Fundamentals]] (native replication, read replicas)
- [[Amazon S3 Fundamentals]] (data lake target)
- [[Redshift Data Loading COPY]] (data warehouse target)
- [[AWS KMS]] (encryption)
- [[AWS SCT]] (schema conversion - separate service)
