 ![[Kinesis Data Streams 2025-10-10 19.23.13.excalidraw]]

## IteratorAgeMilliseconds

A high IteratorAgeMilliseconds implies that the last record that is read from the Kinesis data stream is increasing in age. A high IteratorAgeMilliseconds could mean that the data is not being processed in a timely manner. 
- One way to increase throughput when you use Kinesis Data Streams and Lambda is to increase the parallelization factor. This solution can cause multiple Lambda function invocations to concurrently process one shard. Therefore, this solution could increase performance.
- One way to increase throughput when you use Kinesis Data Streams and Lambda is to register the Lambda function as a consumer with enhanced fan-out. This solution would give the Lambda function dedicated throughput capacity for the Kinesis data stream.
- One way to increase throughput when you use Kinesis Data Streams and Lambda is to reshard. To reshard is to increase the number of shards for Kinesis Data Streams. More shards = more lambda functions.