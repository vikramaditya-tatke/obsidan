---
services:
  - AWS CloudTrail
  - AWS Lake Formation
  - Amazon AppFlow
  - Amazon DynamoDB
  - Amazon Kinesis
  - Amazon Redshift
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Revision
---


- [ ] [[Lake Formation]] - In detail 
- [x] [[DynamoDB Capacity Modes|DynamoDB]] - In detail
- [ ] [[AppFlow]] Flow Triggers
	- Event-triggered flows
	- Incremental transfer schedule-triggered flows
	- On-demand flows
	- Full transfer schedule-triggered flows
- [ ] CloudTrail
	- [ ] Data Events Vs Management Events.
- [ ] [[Redshift Data Loading COPY|Redshift]]
	- [ ] VACUUM types
	- [ ] PARTITIONING AND KEY
- [ ] Encryption and various keys
- [x] Firehose vs [[Kinesis Data Streams|Kinesis]]

---

### Depth Gaps in Existing Notes

#### IAM (35 lines - Insufficient)
**Missing Critical Topics:**
- Service-linked roles and use cases
- Cross-account access (assume role vs resource-based policies)
- Identity federation (SAML 2.0, OIDC, web identity)
- IAM conditions and policy variables
- Boundary policies and permissions boundaries
- IAM Access Analyzer
- IAM roles for services (EC2, Lambda, Glue, etc.)

#### [[AWS Data Engineer Zettelkasten Lite style/CloudWatch and CloudTrail|CloudWatch and CloudTrail]] (31 lines - Insufficient)
**Missing Critical Topics:**
- CloudWatch Alarms (thresholds, composite alarms, anomaly detection)
- Metric filters and patterns
- CloudWatch dashboards and widgets
- CloudWatch Events (EventBridge evolution)
- CloudTrail data events (S3 object-level, Lambda)
- CloudTrail Lake (data lake integration)
- CloudTrail event selectors and logging options
- CloudTrail encryption

#### Kinesis (49 lines - Good but incomplete)
**Missing Critical Topics:**
- On-demand mode vs Provisioned mode
- Enhanced fan-out with Kinesis Client Library (KCL)
- Shard splitting vs merging (resharding details)
- Consumer lag metrics and monitoring
- Kinesis Video Streams (not exam-critical but good context)

#### Glue (51 lines - Good but incomplete)
**Missing Critical Topics:**
- Glue Studio notebooks and development endpoints
- Glue Python shell jobs
- Job bookmarks for incremental processing
- ETL job types (Spark, Python shell, Ray)
- Glue triggers and dependencies
- Crawler configuration and classifiers
- Glue security (IAM roles, VPC)

#### EMR (52 lines - Good but incomplete)
**Missing Critical Topics:**
- EMR on EKS detailed architecture
- Security groups configuration and networking
- Instance fleet (mixed node types, spot/on-demand)
- Cluster states and bootstrap actions
- EMRFS consistent view and S3Guard
- EMR steps and step dependencies

#### Lambda (12 lines - CRITICAL GAP)
**Missing Critical Topics:**
- Concurrency limits (reserved vs provisioned)
- Lambda layers (shared dependencies)
- Aliases and versions
- Event source mapping (stream processing)
- Lambda VPC configuration (ENI, subnet selection)
- Lambda@Edge (CloudFront)
- Destinations (async invocation)

#### SageMaker (1 line - CRITICAL GAP)
**Missing Critical Topics:**
- SageMaker Studio notebooks
- Training jobs (hyperparameters, distributed training)
- Model endpoints (real-time vs batch transform)
- Processing jobs for data preparation
- Model registry and model packages
- Feature Store
- Pipelines and MLOps

#### Athena (9 lines - CRITICAL GAP)
**Missing Critical Topics:**
- Query optimization (partition pruning, predicate pushdown)
- Data formats and compression (Parquet, ORC, CSV)
- Partition projection vs Athena-managed partitions
- Workgroup configuration and cost controls
- Athena query history and recent queries
- CTAS and INSERT INTO statements
- Federated query connectors details

#### Timestream (1 line - CRITICAL GAP)
**Missing Critical Topics:**
- Time series database concepts
- Timestream tables and databases
- Measures and dimensions
- Data retention policies
- Scheduled queries and materialized views
- Timestream SDK and query syntax


### Immediate Action Plan (Next 7 Days)

**Week 1 - Critical Gaps (Domain 1 & 2):**
1. Create note: **AWS KMS** (encryption keys, KMS vs SSE-KMS)
2. Create note: **AWS Secrets Manager** (rotation, comparison with Parameter Store)
3. Create note: **AWS DMS** (CDC, replication tasks)
4. Create note: **AWS Step Functions** (state machines, service integrations)
5. Create note: **AWS CloudFormation** (stacks, templates, drift detection)
6. Expand IAM (cross-account, federation, conditions)
7. Expand CloudWatch (alarms, metric filters, dashboards)

**Week 2 - High Priority Gaps:**
1. Create note: **MSK (Managed Kafka)** (topics, consumer groups)
2. Create note: **AWS Batch** (job queues, compute environments)
3. Create note: **AWS Systems Manager** (Parameter Store, Run Command)
4. Expand Lambda (concurrency, layers, VPC)
5. Expand SageMaker (notebooks, training, endpoints)
6. Expand Athena (optimization, formats, workgroups)

**Week 3 - Medium Priority:**
1. Create note: **AWS DataSync** (tasks, scheduling)
2. Create note: **AWS Transfer Family** (SFTP, users)
3. Create note: **AWS Storage Gateway** (file/volume/tape)
4. Create note: **AWS Snow Family** (edge migration)
5. Add 30+ practice questions categorized by domain
6. Create note: **Amazon OpenSearch** (domains, ingestion)
7. Create note: **Amazon QuickSight** (SPICE, dashboards)

**Week 4 - Complete Gaps:**
1. Create note: **Amazon ElastiCache** (Redis vs Memcached)
2. Create note: **Amazon FSx** (Windows, Lustre, NetApp)
3. Create note: **Amazon DocumentDB** (MongoDB-compatible)
4. Create note: **Amazon Neptune** (graph databases)
5. Add 20+ more practice questions
6. Review all notes for completeness
7. Final revision with mock exams

##  Completed Gaps (Created Notes)

### Week 1 - Critical Gaps (Domain 1 & 2)
- [x] **AWS KMS** - Encryption keys, envelope encryption, KMS vs SSE-KMS
- [x] **AWS Secrets Manager** - Secret rotation, vs Parameter Store, cross-account
- [x] **AWS DMS** - CDC, replication instances, heterogeneous migration
- [x] **AWS Step Functions** - State machines, workflows, service integrations
- [x] **AWS CloudFormation** - Templates, stacks, change sets, drift detection

### Remaining Critical Gaps
- [ ] **AWS Batch** (P0)
- [ ] **MSK (Managed Kafka)** (P0)
- [ ] **AWS X-Ray** (P1)
- [ ] **AWS Systems Manager** (P0)
- [ ] **Developer Tools** - CodeBuild, CodeDeploy, CodePipeline (P1)
- [ ] **AWS DataSync** (P1)
- [ ] **AWS Transfer Family** (P1)
- [ ] **AWS Snow Family** (P1)
- [ ] **Amazon FSx** (P1)
- [ ] **Amazon ElastiCache** (P1)
- [ ] **Amazon OpenSearch** (P1)
- [ ] **Amazon QuickSight** (P1)

### Depth Expansion Needed
- [ ] **IAM** - Cross-account, federation, conditions, boundary policies
- [ ] **CloudWatch & CloudTrail** - Alarms, metric filters, dashboards, data events
- [ ] **Lambda** - Concurrency, layers, VPC, destinations
- [ ] **SageMaker** - Notebooks, training, endpoints, pipelines
- [ ] **Athena** - Optimization, formats, workgroups
- [ ] **Timestream** - Time series concepts, queries, retention
- [ ] **EMR** - On EKS, security groups, instance fleets
- [ ] **Glue** - Studio, Python shell, job bookmarks, triggers

### Practice Questions
- [ ] Add 82+ practice questions (currently have 6)
- [ ] Categorize by exam domain
- [ ] Add scenario-based questions
- [ ] Add comparison questions