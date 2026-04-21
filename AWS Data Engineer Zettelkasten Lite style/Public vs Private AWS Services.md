---
services:
  - AWS IAM
  - AWS Lambda
  - Amazon Aurora
  - Amazon DynamoDB
  - Amazon EC2
  - Amazon EMR
  - Amazon Kinesis
  - Amazon MQ
  - Amazon RDS
  - Amazon Redshift
  - Amazon S3
  - Amazon SQS
  - Amazon VPC
tags: ['aws', 'networking', 'security', 'architecture']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Public Vs Private AWS Services

In AWS, services are generally categorized as either **Public** or **Private** based on how they are accessed and where they reside within the AWS network architecture. Understanding this distinction is crucial for security and connectivity design.

###  Active Recall
- What is the primary difference between a public and a private AWS service?
- How can a resource in a private subnet access a public AWS service without using the public internet?
- Which services are "Public" by default but can be accessed privately?

---

###  Public AWS Services

Public services are those that are accessed via **public endpoints**. They are managed by AWS and exist outside of your VPC.

- **Access**: Accessed over the public internet via HTTPS (by default).
- **Endpoint**: Usually follows the pattern `service.region.amazonaws.com`.
- **Examples**:
    - [[3 Fundamentals|S3]]
    - [[DynamoDB Capacity Modes|Amazon DynamoDB]]
    - [[IAM Policies and Principals|AWS IAM]] (Global)
    - [[AWS Lambda for Data Engineering|AWS Lambda]] (Control plane/API)
    - [[SQS|Amazon SQS]]
    - [[Kinesis Data Streams|Amazon Kinesis]]

###  Private AWS Services

Private services (or VPC-based services) are those that you launch **into your own Virtual Private Cloud (VPC)**.

- **Access**: They have private IP addresses from your VPC's CIDR range.
- **Placement**: They reside within specific subnets.
- **Security**: Controlled via Security Groups and Network ACLs.
- **Examples**:
    - [[EC2|Amazon EC2]] instances
    - [[RDS and Aurora Fundamentals|Amazon RDS]] / [[RDS and Aurora Fundamentals|Amazon Aurora]]
    - [[Redshift Data Loading COPY|Amazon Redshift]] clusters
    - [[EMR Fundamentals|Amazon EMR]] clusters
    - [[Amazon MQ]] brokers

###  Connectivity Patterns

1. **Private -> Public**:
    - To allow a private resource (like an EC2 instance in a private subnet) to reach a public service:
        - **Gateway VPC Endpoints**: Specifically for [[Amazon S3 Fundamentals|S3]] and [[DynamoDB Capacity Modes|DynamoDB]]. (Free).
        - **Interface VPC Endpoints (PrivateLink)**: Uses an ENI with a private IP for most other services. (Paid).
        - **NAT Gateway**: Allows outbound internet access to reach the public endpoint.

2. **Public -> Private**:
    - Generally not possible directly. Requires a Bastion Host, VPN, Direct Connect, or a Load Balancer (ALB/NLB) with a public-facing configuration.

> [!INFO] Exam Tip: Security
> Always prefer **VPC Endpoints** over NAT Gateways for data engineering workloads when accessing S3 or DynamoDB to keep traffic within the AWS backbone and reduce costs.
