## Kinesis Data Streams

![[Excalidraw/Kinesis Data Streams.md#^area=UgaPZmfgZ9D08UBV9benb]]

> Kinesis Data Streams is a real-time service that receives data in real-time and the consumers can use this data in real-time with *~200ms* latency.

# Concepts

- **IteratorAgeMilliseconds**: A high `IteratorAgeMilliseconds` implies that the last record that is read from the Kinesis data stream is increasing in age. A high `IteratorAgeMilliseconds` could mean that the data is not being processed in a timely manner.

- **Re-shard**: To re-shard is to increase the number of shards for Kinesis Data Streams.

# Provisioned Mode

- A PUT Payload Unit (chunk) is 25KB for Kinesis Data Streams, even if the record size is <25KB.
- The service **charges** by the number of PU utilized.

> [!NOTE]
> - [Kinesis Producer Library](https //github.com/awslabs/amazon-kinesis-producer) creates 25KB payloads and pre-aggregates the data on the fly to create cost-efficient ingestion pipelines. *This requires that the downstream consumer de-aggregates the records before using.*

# [[SQS]] Vs KDS

- A rough corollary would be - Taking Action (SQS) Vs Processing Data (KDS).
- Generally only 1 production group and 1 consumer group are related to an SQS queue, whereas multiple (100s or 1000s) can be related to KDS.

## Kinesis Data Firehose

Kinesis Data Firehose is a fully-managed stream based delivery service that scales automatically capable of delivering high throughput streaming data to data lakes, data stores and analytics services in *near*
real-time.

- Transformation can be handled on the fly using [[Lambda]] Functions.
- Is charged on the basis of the amount of data passing through the services. 

It can delivery to [[S3]], [[Redshift]], http endpoints (think of ClickHouse, Apache Druid, or any other http endpoints.)

> Kinesis Data Firehose is a near-real time service that can receive data in real-time but the consumers cannot use it in real-time.

Latency for Kinesis Data Firehose buffers the before delivery. Minimum buffer interval is 1 minute and minimum buffer size is 1 MB.


## Kinesis Data Analytics 

Kinesis Data Analytics is now known as Managed Service for Apache Flink. It is used to process real-time streaming data. This services uses SQL for data processing. It generates an output stream by applying the data processing logic described using SQL. 

- Creates in-application streams
- Can read from reference data.

![[Excalidraw/Kinesis Data Streams.md#^area=EE6dIdSO]]
