---
services:
  - AWS CloudTrail
  - AWS IAM
  - Amazon CloudWatch
  - Amazon Kinesis
  - Amazon S3
  - Amazon VPC
tags: ['aws', 'vpc', 'flow-logs']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## VPC Flow Logs
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[VPC.excalidraw]]

## VPC Flow Logs

Captures information about IP traffic going into your interfaces.

- VPC Flow Logs
- Subnet Flow Logs
- ENI Flow Logs
- Data Flow could be like follows for storing / processing the logs data
	- VPC Flow Logs -> [[Amazon S3 Fundamentals|S3]]
	- VPC Flow Logs -> [[CloudWatch and CloudTrail]]
	- VPC Flow Logs -> [[Kinesis# [[Kinesis Data Streams|Kinesis]] Data Firehose]]

### Log Fields Structure

The standard VPC Flow Log entry consists of the following fields in order:

interface-id

- srcaddr
- dstaddr
- srcport
- dstport
- protocol
- packets
- bytes
- start
- end
- action
- log-status

### Example Log Entries
#### Allowed Traffic (ACCEPT)

2 ACC-ID eni-ID 119.18.34.78 10.16.48.20 0 0 1   4 336 1432917027 1432917142 ACCEPT OK

                *srcaddr* *dstaddr* *ICMP* *Action*

#### Blocked Traffic (REJECT)

2 ACC-ID eni-ID 10.16.48.20 119.18.34.78 0 0 1 4 336 1432917094 1432917142 REJECT OK

                *srcaddr* *dstaddr* *ICMP* *Action*

### Protocol Reference

The `protocol` field uses standard IANA protocol numbers:

ICMP = 1

TCP = 6

UDP = 17

> VPC Flow logs DO NOT log the traffic to and from 169.254.169.254, 169.254.169.123, DHCP, Amazon DNS Server, Amazon Windows License Server.