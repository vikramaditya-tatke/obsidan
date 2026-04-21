---
services:
  - Amazon DynamoDB
  - Amazon S3
  - Amazon VPC
tags: ['aws', 'vpc', 'connectivity']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## VPC Connectivity (Peering and Endpoints)
###  Active Recall
- How does this service integrate with other AWS components mentioned?

---

![[VPC.excalidraw]]

## VPC Peering
- VPC Peering is used to *privately connect* VPCs using the AWS Network, then the VPCs will behave as if they were the same network.
- VPCs must not have overlapping IP ranges.
- VPC Peering is not transitive - needs to be established for EACH VPC that needs to communicate with another.
- **For Example**: `VPC A <-> VPC B, VPC A <-> VPC C: VPC  B <-X-> VPC C`

## VPC Endpoints

- Endpoints allow you to connect to [[AWS Services]] privately.
- All [[AWS Services]] are have an option to attach a default VPC which makes the resources publicly accessible by assigning them a public IPS address - The default VPC has an Internet Gateway attached to it.
- The AWS Control Plane is public, while the resources themselves are not (unless attached to the default VPC).

## VPC Endpoint Services (AWS PrivateLink)

- Most secure able scalable way to expose a service to 1000s of VPCs.
- Requires a NLB in the service VPC and an ENI in the Customer VPC
 
### VPC Endpoint Gateway: [[Amazon S3 Fundamentals|S3]] and [[DynamoDB Capacity Modes|DynamoDB]]
### VPC Endpoint Interface: Most AWS Services including [[Amazon S3 Fundamentals|S3]] and [[DynamoDB Capacity Modes|DynamoDB]]

## Site-to-Site VPN
- Connect an on-prem VPC to AWS.
- The connection is automatically encrypted.
- Goes over the public internet.
## Direct Connect

- Establishes a physical connection between on-prem and AWS.
- Connection is private, secure and fast.
- Goes over a private network.
- Takes a month to establish.