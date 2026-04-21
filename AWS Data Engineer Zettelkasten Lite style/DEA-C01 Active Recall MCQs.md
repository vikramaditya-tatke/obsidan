---
tags:
  - exam/practice
  - AWS/DEA-C01
creation_date: 2026-01-03
---

# DEA-C01 Active Recall MCQs

This note contains scenario-based multiple-choice questions designed to mimic the AWS Certified Data Engineer - Associate (DEA-C01) exam. 

> [!TIP] How to use this note
> Attempt to answer the question mentally before expanding the **Answer & Explanation** block.

---

## Amazon AppFlow

**Question 1:**
A marketing company uses Salesforce to track customer interactions and wants to automatically ingest this data into an Amazon S3 data lake every night at midnight. The data contains some Personally Identifiable Information (PII) that must be masked before it is stored in S3. The solution must require the least amount of coding and operational overhead.

Which solution should the data engineer implement?

A. Create an AWS Glue Python Shell job that connects to Salesforce using the JDBC driver, fetches the data, masks the PII columns using a library, and writes to S3. Schedule the job using EventBridge.
B. Configure an Amazon AppFlow flow to transfer data from Salesforce to Amazon S3. Set the flow trigger to "Run on schedule". Use the "Map data" step to mask the PII fields using the built-in masking transformation.
C. Use AWS Lambda with a custom layer containing the Salesforce SDK to query the data. Use the Lambda function to mask the PII and write the result to S3. Schedule the function using EventBridge Scheduler.
D. Set up an Amazon EC2 instance with a cron job that runs a Python script to pull data from the Salesforce REST API, masks the PII locally, and uploads the files to Amazon S3.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between SaaS applications (like Salesforce) and AWS services (like S3).
> - **Operational Overhead:** It requires zero coding, unlike Glue (Option A), Lambda (Option C), or EC2 (Option D).
> - **Transformation:** AppFlow has built-in transformation capabilities, including the ability to mask sensitive data (PII) during the transfer.
> - **Scheduling:** It supports scheduled triggers natively.

---

## Amazon Athena

**Question 2:**
A data engineer has created an external table in Amazon Athena backed by 500 TB of log data stored in Amazon S3 in Apache Parquet format. The logs are partitioned by year, month, and day (`year=yyyy/month=mm/day=dd`). Analysts frequently run queries filtering by a specific date range, but the queries are taking longer than expected and scanning more data than necessary.

What should the data engineer do to optimize query performance and reduce costs?

A. Enable S3 Transfer Acceleration on the bucket to speed up data retrieval for Athena.
B. Run the `MSCK REPAIR TABLE` command every time a query is executed to ensure partitions are up to date.
C. Use partition projection in the Athena table properties to calculate partition values dynamically without managing the Glue Data Catalog partition metadata.
D. Compress the Parquet files using GZIP to reduce the data size scanned.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: C**
> 
> **Explanation:** 
> **Partition Projection** allows Athena to calculate partition values and locations from table configuration rather than retrieving metadata from the AWS Glue Data Catalog. This significantly reduces query planning time for highly partitioned tables.
> - **Option A** helps with upload speeds, not query scanning.
> - **Option B** is for updating metadata, not optimizing scan performance during query execution, and running it every time is inefficient.
> - **Option D** is good practice, but Parquet is often already compressed (Snappy), and Partition Projection is the specific fix for "high partition count" overhead.

---

## AWS Backup

**Question 3:**
A financial institution requires that all DynamoDB tables and Amazon EFS file systems be backed up daily. These backups must be copied to a different AWS Region for disaster recovery (DR) compliance. The DR region must have a distinct retention policy of 7 years, whereas the source region retention is only 30 days.

Which solution meets these requirements with the LEAST administrative effort?

A. Create a Lambda function triggered by EventBridge to create backups. Use the `copy-backup` API to copy the recovery points to the DR region and tag them with a new retention period.
B. Use AWS DataSync to synchronize the EFS volumes and DynamoDB table exports to an S3 bucket in the DR region. Set S3 Lifecycle policies for retention.
C. Create an AWS Backup plan. Define a backup rule with a copy configuration. Specify the destination Region and set a separate lifecycle (retention period) for the copy in the destination backup vault.
D. Enable Cross-Region Replication (CRR) on the underlying S3 buckets that back the EFS and DynamoDB storage layers.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: C**
> 
> **Explanation:** 
> **AWS Backup** provides a policy-based way to manage backups across services. 
> - It natively supports **Cross-Region Copy** within a Backup Plan.
> - You can specify a **different lifecycle (retention)** for the copy than the source, which exactly meets the requirement (30 days source vs 7 years DR).
> - Option A requires custom scripting. Option B is for data movement, not backup management. Option D is technically impossible as you don't access the underlying S3 buckets for managed DynamoDB/EFS directly.

---

## Amazon CloudWatch & CloudTrail

**Question 4:**
A data engineering team is troubleshooting a failed AWS Glue ETL job. The job failed with an "Access Denied" error when attempting to write to a specific S3 bucket. The team needs to confirm exactly which API call failed and which IAM principal was used to make the call.

Which combination of tools should the data engineer use?

A. Check the AWS Glue console for the error logs and use Amazon CloudWatch Metrics to see the `403ErrorCount` for the S3 bucket.
B. Review the AWS Glue driver logs in Amazon CloudWatch Logs for the error message, and query AWS CloudTrail Lake or Event History for the specific `PutObject` access denied event.
C. Use Amazon Inspector to analyze the IAM role attached to the Glue job and simulate the policy permissions.
D. Check the S3 Server Access Logs in the target bucket to find the failed request source IP address.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> - **AWS Glue Driver Logs (CloudWatch Logs):** These will contain the application-level error details showing *where* in the script the failure occurred.
> - **AWS CloudTrail:** This records API calls made on your account. An "Access Denied" on `PutObject` will appear here with the user identity (ARN) and the reason for the denial.
> - CloudWatch Metrics (A) give counts but not context. Inspector (C) is for vulnerability scanning. S3 Access Logs (D) show requests but CloudTrail is the standard for API auditing and permission troubleshooting.

---

## Amazon DynamoDB

**Question 5:**
An IoT application ingests sensor data into an Amazon DynamoDB table. The data is time-series in nature, and the access pattern involves heavy writes of current data and occasional reads of data older than 48 hours. The table size is growing rapidly, increasing storage costs. The business requirement states that data older than 7 days is rarely accessed but must be retained for 5 years for auditing.

Which strategy is the most cost-effective?

A. Use DynamoDB Streams to replicate data to a separate table. Delete data from the main table after 7 days using a scheduled Lambda function.
B. Enable DynamoDB Time to Live (TTL) on a timestamp attribute to automatically delete items older than 7 days. Enable DynamoDB Streams and use Amazon Kinesis Data Firehose to archive the deleted items to Amazon S3 for long-term storage.
C. Create a daily backup of the DynamoDB table using AWS Backup. Restore the backup to a new table for auditing when needed. Delete the original table every 7 days.
D. Use the DynamoDB Standard-Infrequent Access (Standard-IA) table class to reduce storage costs for the entire table.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> This is a classic pattern for "Hot/Cold" data in DynamoDB.
> - **TTL:** Automatically deletes items without consuming Write Capacity Units (WCU).
> - **Streams + Firehose:** When TTL deletes an item, it appears in the DynamoDB Stream with a specialized attribute. Kinesis Firehose can capture these deletes and archive them to S3 (cheapest storage) for the 5-year retention requirement.
> - Option D applies to the *whole* table, but the write workload is heavy, which would make Standard-IA more expensive (due to high write costs).

---

## Amazon EMR

**Question 6:**
A data engineer is designing an Amazon EMR cluster to process a large batch of clickstream data daily. The processing job takes about 4 hours. The workload is resilient to node failures and can be restarted if necessary. The priority is to minimize the total cost of compute.

Which cluster configuration should the engineer recommend?

A. Use On-Demand Instances for the Master node, Core nodes, and Task nodes to ensure stability.
B. Use On-Demand Instances for the Master node and Core nodes. Use Spot Instances for the Task nodes.
C. Use Spot Instances for the Master node, Core nodes, and Task nodes.
D. Use Reserved Instances for the Master node and Spot Instances for all Core and Task nodes.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> - **Master Node:** Manages the cluster. If it terminates, the cluster dies. Must be stable (On-Demand).
> - **Core Nodes:** Host HDFS data. If they terminate, data is lost (unless purely using EMRFS, but HDFS replication recovery is slow). Usually kept stable (On-Demand) for critical jobs.
> - **Task Nodes:** Only process data; they do not store HDFS data. If a Spot instance is reclaimed, the task is simply rescheduled on another node. This offers the **greatest cost savings** with minimal risk for a resilient workload.

---

## AWS Glue

**Question 7:**
A retail company has a strict data quality requirement. A data engineer needs to ensure that a Glue ETL job processing daily sales data does not insert records with null `customer_id` values into the target Redshift table. The solution should integrate directly into the existing Glue visual job.

What should the data engineer do?

A. Write a custom Python script in the Glue job to iterate through the DynamicFrame and drop rows where `customer_id` is null.
B. Add a "Data Quality" transform node to the Glue visual job. Define a rule `IsComplete "customer_id"` and configure the data quality action to fail the job or drop the records if the rule fails.
C. Use AWS Glue Crawlers to infer the schema and set the `customer_id` column to "NOT NULL" in the Data Catalog.
D. Use Amazon Macie to scan the dataset for null values before starting the Glue job.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> **AWS Glue Data Quality** is a native feature that allows you to define rules (like `IsComplete`, `Uniqueness`) directly in the ETL pipeline.
> - It is integrated into the Visual Editor.
> - It allows you to stop the job or quarantine data based on the results, meeting the requirement without writing custom Python iteration code (which is inefficient in distributed processing).

---

## Amazon Kinesis

**Question 8:**
A media company needs to convert raw JSON log files being streamed from their application servers into Apache Parquet format before storing them in Amazon S3 for analytics. The stream has a throughput of 5 MB/sec. The solution must handle the conversion and delivery with the minimum amount of custom code.

Which solution meets these requirements?

A. Use Amazon Kinesis Data Streams to ingest the logs. Create a Lambda function to read batches, convert JSON to Parquet, and write to S3.
B. Use Amazon Data Firehose to ingest the logs. Enable "Record Format Conversion" in the Firehose configuration, specifying an AWS Glue Table schema for the conversion to Parquet.
C. Use Amazon Kinesis Data Streams to ingest the logs. Use Kinesis Client Library (KCL) on EC2 to process and convert the files.
D. Use Amazon Data Firehose to deliver JSON files to S3. Configure an S3 Event Notification to trigger a Glue Crawler to convert the files later.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> **Amazon Data Firehose** supports **Record Format Conversion** out of the box.
> - By defining a schema in the Glue Data Catalog, Firehose can convert JSON to Parquet/ORC on the fly before writing to S3.
> - This requires **zero custom code** (unlike Lambda or KCL) and is a fully managed feature.

---

## AWS Lake Formation

**Question 9:**
A healthcare organization is building a data lake and needs to enforce fine-grained access control. They want to restrict access to a specific column named `ssn` in a Glue table for a group of data analysts. The analysts should be able to see all other columns.

Which combination of steps is required to achieve this using AWS Lake Formation?

A. Create an IAM policy that explicitly denies `glue:GetTable` on the `ssn` column and attach it to the analysts' IAM role.
B. In Lake Formation, register the S3 location. Create a Data Filter that excludes the `ssn` column. Grant `SELECT` permission on the table to the analysts' IAM role using this Data Filter.
C. Create a view in Amazon Athena that excludes the `ssn` column. Grant the analysts access only to the Athena view and not the underlying Glue table.
D. Enable S3 Object Lock and encryption on the data files to prevent reading the `ssn` field.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> **Lake Formation Data Filters** allow for Column-Level, Row-Level, and Cell-Level security.
> - By creating a filter that *excludes* the sensitive column and granting permissions via that filter, the analysts will simply not see the `ssn` column when they query via Athena or Redshift Spectrum.
> - Option A is incorrect because IAM does not support column-level granularity for Glue tables (only Lake Formation does).

---

## AWS Lambda

**Question 10:**
A data engineer has written a Lambda function to insert processed records into an Amazon RDS for PostgreSQL database. During peak traffic, the Lambda function scales out to hundreds of concurrent executions, causing the RDS database to become unresponsive due to "Too many connections" errors.

What is the most effective solution to resolve this connection issue?

A. Increase the memory of the Lambda function to allow it to process records faster.
B. Implement exponential backoff and jitter in the Lambda function code to retry failed connections.
C. Deploy an Amazon RDS Proxy between the Lambda function and the RDS database instance. Update the Lambda function to connect to the Proxy endpoint.
D. Convert the RDS instance to Amazon Aurora Serverless v2 to handle the connection load.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: C**
> 
> **Explanation:** 
> **Amazon RDS Proxy** is designed specifically for this use case. 
> - Lambda creates a new database connection for every concurrent execution (container). This quickly exhausts the `max_connections` limit of a database.
> - RDS Proxy pools and shares connections, allowing thousands of Lambda functions to interact with the DB using a much smaller number of actual DB connections.

---

## Amazon RDS & Aurora

**Question 11:**
A business intelligence team runs complex analytical queries on an Amazon Aurora MySQL production database every Monday morning. These queries degrade the performance of the transactional application. The data engineer needs to isolate the analytical workload from the production traffic.

What should the data engineer do?

A. Enable Aurora Parallel Query on the production instance.
B. Create an Aurora Read Replica. Configure the BI tools to connect to the Read Replica endpoint.
C. Export the Aurora snapshot to Amazon S3 and use Athena to query the data.
D. Increase the instance class of the Writer node during the Monday morning window.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> - **Read Replicas** are designed to offload read-heavy traffic (like BI/Analytics) from the primary writer instance.
> - This isolates the compute resources used for analytics from the transactional application.
> - Option C is a valid pattern (Data Lake) but involves moving data and changing tooling (SQL dialect changes), whereas a Read Replica allows the same MySQL queries to run natively with minimal friction.

---

## Amazon Redshift

**Question 12:**
A company stores 2 PB of historical sales data in Amazon S3. The data science team needs to join this historical data with current sales data stored in an Amazon Redshift cluster (RA3 nodes) for a one-time analysis. Loading the 2 PB of data into Redshift would take too long and exceed the cluster's storage capacity.

Which approach allows the team to perform the analysis with the LEAST effort and cost?

A. Resize the Redshift cluster to add more nodes, copy the S3 data using the `COPY` command, run the query, and then resize the cluster back down.
B. Use Amazon Redshift Spectrum to create an external table pointing to the S3 data. Join the external table with the local Redshift tables in the query.
C. Use AWS Glue to transform the S3 data and load only the relevant aggregated subsets into Redshift.
D. Use Amazon Athena to query the S3 data and use the Athena Query Federation connector to join with Redshift.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> **Redshift Spectrum** allows you to query data directly in S3 without loading it into Redshift storage.
> - It extends the analytical power of Redshift to the Data Lake.
> - It is perfect for accessing massive datasets (2 PB) that are rarely queried or too big to load, enabling joins between "hot" local data and "cold" S3 data.

---

## Amazon S3

**Question 13:**
A media company stores high-resolution images in an S3 bucket. A legacy application requires these images to be in PNG format, but the raw images are stored as high-quality JPEGs. The company wants to avoid storing duplicate copies of converted images to save on storage costs.

Which feature should the data engineer use to fulfill this request?

A. Use S3 Batch Operations to convert all JPEGs to PNGs and store them in a separate prefix.
B. Use S3 Object Lambda. Create a Lambda function that converts JPEG to PNG on the fly when the application requests the object.
C. Use Amazon CloudFront with a Lambda@Edge function to convert the images and cache them at the edge.
D. Trigger a Lambda function on S3 `PutObject` to convert the image and overwrite the original file.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> **S3 Object Lambda** allows you to add your own code to S3 `GET` requests to modify and process data as it is returned to an application.
> - This meets the requirement to *avoid storing duplicate copies*. The conversion happens dynamically during retrieval.
> - Option A creates duplicates. Option C is a valid architectural pattern but S3 Object Lambda is more specific to the "storage view" requirement and internal applications.

---

## AWS Step Functions

**Question 14:**
A data pipeline consists of three sequential AWS Glue jobs. If Job A succeeds, Job B should run. If Job B fails, the pipeline should wait 5 minutes and retry twice before failing. If Job B eventually succeeds, Job C should run.

Which AWS service is best suited to orchestrate this logic?

A. AWS Glue Workflows
B. Amazon EventBridge Rules
C. AWS Step Functions
D. AWS Lambda functions chaining each other

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: C**
> 
> **Explanation:** 
> **AWS Step Functions** is a serverless orchestration service ideal for coordinating distributed applications.
> - It has native support for **Retry** policies (Interval, MaxAttempts, BackoffRate) and **Catch** logic.
> - While Glue Workflows (A) can chain jobs, Step Functions provides much more granular control over error handling, wait states, and conditional branching.

---

## Amazon SQS

**Question 15:**
A data ingestion system receives messages in an Amazon SQS queue. A Lambda function processes these messages. Occasionally, a malformed message causes the Lambda function to fail. The Lambda retry policy causes the bad message to be processed repeatedly, blocking new messages and wasting compute resources.

What should the data engineer configure to handle this scenario effectively?

A. Increase the Visibility Timeout of the SQS queue.
B. Configure a Dead Letter Queue (DLQ) for the source SQS queue and set a `maxReceiveCount`.
C. Configure the Lambda function to delete the message immediately upon receipt.
D. Use a FIFO queue to ensure the message is processed exactly once.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> - A **Dead Letter Queue (DLQ)** is the standard pattern for handling "poison pill" messages.
> - By setting a `maxReceiveCount` (e.g., 3), SQS will move the message to the DLQ after it has failed processing 3 times. This unblocks the queue and allows you to analyze the failed message separately.

---

## AWS Database Migration Service (DMS)

**Question 16:**
A company needs to migrate a large on-premises Oracle database to Amazon Aurora PostgreSQL. The migration involves heterogenous schema conversion and continuous data replication with minimal downtime.

Which combination of tools should the data engineer use?

A. Use the AWS Schema Conversion Tool (SCT) to convert the schema and AWS DMS to migrate the data.
B. Use AWS DMS for both schema conversion and data migration.
C. Use native Oracle tools to export schema/data to S3 and use Aurora `aws_s3.table_import_from_s3` to load it.
D. Use AWS Glue to crawl the Oracle database and write the data to Aurora PostgreSQL.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: A**
> 
> **Explanation:** 
> - **SCT (Schema Conversion Tool):** Required for **heterogeneous** migrations (e.g., Oracle to PostgreSQL) to convert schema objects (views, stored procedures).
> - **DMS (Database Migration Service):** Handles the data movement (full load + CDC). DMS alone cannot handle complex schema conversions (like stored procedures).

---

## Amazon MWAA

**Question 17:**
A data engineer is using Amazon Managed Workflows for Apache Airflow (MWAA) to orchestrate an ETL pipeline. The Airflow DAG requires a specific Python library (`pandas`) that is not included in the default Airflow image.

How should the engineer install this dependency?

A. SSH into the MWAA worker nodes and run `pip install pandas`.
B. Add `pandas` to a `requirements.txt` file, upload it to the environment's S3 bucket, and update the MWAA environment configuration to point to this file.
C. Use the `PythonVirtualenvOperator` in the DAG and install pandas at runtime.
D. Create a custom Docker image with pandas installed and upload it to ECR for MWAA to use.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> - MWAA is a managed service, so you cannot SSH into workers (Option A) or bring custom Docker images (Option D - this is a feature of Airflow on ECS/EKS, not standard MWAA).
> - The standard way to manage dependencies in MWAA is via a **`requirements.txt`** file stored in S3.

---

## AWS IAM

**Question 18:**
An AWS Glue job running in Account A needs to read data from an S3 bucket in Account B.

Which set of permissions is required to allow this cross-account access?

A. The IAM Role in Account A needs `s3:GetObject` on the bucket. The S3 Bucket Policy in Account B must allow the IAM Role ARN from Account A to perform `s3:GetObject`.
B. The IAM Role in Account A needs `s3:GetObject` on the bucket. No changes are needed in Account B if the object is public.
C. The S3 Bucket Policy in Account B must allow `Principal: *`.
D. Create an IAM User in Account B and embed the access keys in the Glue job script in Account A.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: A**
> 
> **Explanation:** 
> **Cross-Account Access** requires permission on BOTH sides:
> 1.  **Identity-based policy (Account A):** The Glue Role must have permission to call the API.
> 2.  **Resource-based policy (Account B):** The S3 Bucket Policy must explicitly trust the principal (Role ARN) from Account A.

---

## Amazon EventBridge

**Question 19:**
A data engineer wants to trigger an AWS Glue job immediately whenever a new file lands in a specific S3 bucket prefix `s3://data-lake/landing/`.

Which solution offers the lowest latency and operational overhead?

A. Create an EventBridge Rule with an event pattern matching `source: aws.s3` and `detail-type: Object Created`. Set the Glue Job as the target.
B. Configure S3 Event Notifications to send a message to SQS. Poll the SQS queue with a Lambda function that triggers the Glue job.
C. Create a CloudWatch Alarm based on S3 `PutRequests` metrics and trigger the Glue job via SNS.
D. Schedule the Glue job to run every 5 minutes and check for new files.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: A**
> 
> **Explanation:** 
> **EventBridge** (formerly CloudWatch Events) provides a near real-time, event-driven architecture.
> - S3 natively sends events to EventBridge (must be enabled on the bucket).
> - This is cleaner than chaining SQS+Lambda (Option B) and faster than polling (Option D).

---

## Amazon Macie

**Question 20:**
A company stores sensitive financial records in Amazon S3. A data engineer needs to automatically scan all new objects in the bucket to identify any accidental exposure of credit card numbers or private keys.

Which service should be used?

A. AWS Glue DataBrew
B. Amazon GuardDuty
C. Amazon Macie
D. AWS Shield

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: C**
> 
> **Explanation:** 
> **Amazon Macie** is a data security service that uses machine learning and pattern matching to discover sensitive data (PII, credentials) in **Amazon S3**.
> - GuardDuty (B) is for threat detection (network/account activity). Shield (D) is for DDoS.

---

## Amazon MSK

**Question 21:**
A company is migrating an on-premises Apache Kafka cluster to AWS. They have existing applications written in Java that use the Kafka APIs. They want to migrate to a managed service with minimal code changes.

Which service should they choose?

A. Amazon Kinesis Data Streams
B. Amazon Managed Streaming for Apache Kafka (Amazon MSK)
C. Amazon SQS
D. Amazon SNS

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> - **Amazon MSK** is fully managed Apache Kafka. Since the applications are already written for Kafka, moving to MSK requires changing only the connection string (bootstrap servers).
> - Moving to Kinesis (A) would require rewriting the application code to use the Kinesis SDK.

---

## AWS Secrets Manager

**Question 22:**
An AWS Glue job connects to an Amazon RDS database using a username and password. The security policy requires that database credentials be rotated every 30 days. The data engineer must ensure the Glue job always uses the valid credentials without manual updates.

What should the data engineer do?

A. Store the credentials in an S3 file and update the file manually every 30 days.
B. Store the credentials in AWS Systems Manager Parameter Store as a SecureString. Use a CloudWatch Event to remind the admin to update it.
C. Store the credentials in AWS Secrets Manager. Configure automatic rotation using the appropriate Lambda rotation function. Update the Glue job to retrieve the secret at runtime.
D. Hardcode the credentials in the Glue script and redeploy the script every 30 days.

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: C**
> 
> **Explanation:** 
> **AWS Secrets Manager** supports **automatic rotation** of credentials for RDS.
> - It uses a helper Lambda function to update the password in the database and the secret value simultaneously.
> - Glue jobs can call the `GetSecretValue` API to fetch the current valid password.

---

## Amazon VPC

**Question 23:**
An AWS Glue ETL job is running in a private subnet and needs to read data from Amazon S3. For security compliance, the data traffic must not traverse the public internet.

Which VPC resource must be configured?

A. Internet Gateway
B. NAT Gateway
C. VPC Gateway Endpoint for S3
D. VPC Interface Endpoint for S3

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: C**
> 
> **Explanation:** 
> **VPC Gateway Endpoints** are the standard, free way to connect private subnets to Amazon S3 (and DynamoDB) without using public IPs or NAT Gateways.
> - It modifies the route table to route S3 traffic internally within the AWS network.
> - Interface Endpoints (Privatelink) (Option D) are also possible but Gateway Endpoints are the "classic" and cost-effective answer for S3 specifically in exam scenarios unless on-prem access is needed.

---

## AWS CloudFormation

**Question 24:**
A data team wants to deploy an identical data pipeline (Glue Jobs, S3 buckets, Redshift cluster) across three environments: Dev, Test, and Prod. The deployment process should be automated, repeatable, and version-controlled.

Which AWS service is the best choice?

A. AWS Elastic Beanstalk
B. AWS CodeDeploy
C. AWS CloudFormation
D. AWS Systems Manager

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: C**
> 
> **Explanation:** 
> **AWS CloudFormation** allows you to model infrastructure as code (templates).
> - You can reuse the same template with different parameters (e.g., instance sizes, bucket names) to deploy identical stacks across multiple environments.

---

## AWS Glue DataBrew

**Question 25:**
A team of business analysts wants to clean and normalize a dataset in Amazon S3 (e.g., removing duplicates, masking PII, converting formats). They do not have Python or SQL coding skills and prefer a visual interface.

Which tool should they use?

A. AWS Glue Studio
B. AWS Glue DataBrew
C. Amazon EMR Studio
D. Amazon Athena

> [!SUCCESS]- Answer & Explanation
> **Correct Answer: B**
> 
> **Explanation:** 
> **AWS Glue DataBrew** is a visual data preparation tool specifically designed for analysts and data scientists to clean and normalize data **without writing code**.
> - Glue Studio (A) is visual but geared more towards ETL developers.

