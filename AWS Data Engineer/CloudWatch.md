## Metrics
- Metrics for Services in AWS, such as CPU Util, Networking, etc.
- Metrics belong to _namespaces_
- Up to 30 dimensions per metric.
- Creation of CloudWatch Custom Metrics
	> Extract RAM usage of an EC2 instance.
-  CloudWatch metrics can be streamed to multiple destinations 
	- Kinesis Data Firehose
	- Datadog, Sumo Logic, New Relic, Splunk, etc.

## Logs
- **Log Groups**: Typically representing an application.
- **Log Stream**: Instaces within the application or log files or containers, etc.
- Log Retention policy: Between 1 day to 10 years.
- CloudWatch Logs can send logs to 
	- Amazon S3 -> CreateExportTask -> Batch Export -> Up to 12 hours.
### CloudWatch Logs Subscription
Near real-time
- Kinesis Data Streams, Kinesis Data Firehose.
- AWS Lambda or OpenSearch.
Using subscription filters, log aggregation can be performed across multiple regions and accounts.

![[Excalidraw/CloudWatch]]