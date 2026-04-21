---
services:
  - AWS CloudTrail
  - AWS IAM
  - AWS Lambda
  - Amazon CloudWatch
  - Amazon EC2
  - Amazon Kinesis
  - Amazon OpenSearch Service
  - Amazon S3
tags: ['aws', 'cloudwatch']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## CloudWatch and CloudTrail
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[CloudWatch]]

## Metrics
- Metrics for Services in AWS, such as CPU Util, Networking, etc.
- Metrics belong to _namespaces_
- Up to 30 dimensions per metric.
- Creation of CloudWatch Custom Metrics
	> Extract RAM usage of an [[EC2|EC2]] instance.
- CloudWatch metrics can be streamed to multiple destinations
	- [[Kinesis Data Firehose]]
	- Datadog, Sumo Logic, New Relic, Splunk, etc.
### Alarms
CloudWatch Alarms operate on a single Metric.
CloudWatch Alarms can also be created on [[CloudWatch and CloudTrail#Logs|CloudWatch Logs]] Metrics Filters.
- Alarms are used to trigger notifications for any metric. It supports various options such as sampling, %, min, max, avg, etc.
- **Alarm States:** 
	1. OK
	2. INSUFFICIENT_DATA
	3. ALARM
- **Period:** Length of time in seconds to evaluate the metric. 
	- High Resolution custom metrics: 10 sec, 30 sec or multiples of 60 seconds.
#### Alarm Targets
- Stop, Terminate, Reboot or Recover an EC2 instance.
- Trigger Auto Scaling Action.
- Send notification to SNS
- Example: [[EC2#EC2 Instance Recovery| EC2 Instance Recovery]]
### Composite Alarms
Composite Alarms are used to monitor the states of multiple other alarms.
Can use AND/OR conditions. For example - *Don't alert if* the CPU is low and network is high but *alert if* the CPU is low and the network is high.

## Logs
- **Log Groups**: Typically representing an application.
- **Log Stream**: Instances within the application or log files or containers, etc.
- Log Retention policy: Between 1 day to 10 years.
- CloudWatch Logs can send logs to
	- Amazon [[Amazon S3 Fundamentals|S3]] -> CreateExportTask -> Batch Export -> Up to 12 hours.
### CloudWatch Logs Subscription

Near real-time

- [[Kinesis Data Streams]], [[Kinesis Data Firehose]].
- AWS [[Lambda]] or OpenSearch.
Using subscription filters, log aggregation can be performed across multiple regions and accounts.

![[Excalidraw/CloudWatch]]

## CloudTrail

You can have CloudTrail deliver log files from multiple AWS accounts into a single Amazon [[Amazon S3 Fundamentals|S3]] bucket.

AWS CloudTrail records actions taken by a user, role, or an AWS service in AWS. If a bucket is designated as a CloudTrail log bucket, CloudTrail logs API calls made on this bucket.