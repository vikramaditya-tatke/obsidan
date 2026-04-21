---
services:
  - Amazon VPC
tags: ['aws', 'vpc', 'networking']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## VPC Networking Fundamentals
###  Active Recall
- What components are required to make a subnet 'public'?
- How do NAT Gateways allow private instances to reach the internet?

---

![[VPC.excalidraw]]

- VPC is a regional resource.
- Subnets allow partitioning of network within the VPC.
- VPCs have a CIDR range like 10.0.0.128/16

![[VPC.excalidraw]]

## Gateways

## Internet Gateway

Public subnets have a direct route to the internet gateway.

## NAT

This allows instances in [[Public vs Private AWS Services|Private Subnets]] to access the internet while remaining private.

**NAT Gateways**: Managed by AWS.
**NAT Instances**: Self Managed.