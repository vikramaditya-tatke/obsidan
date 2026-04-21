---
services:
  - AWS IAM
  - Amazon EC2
  - Amazon S3
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Compute
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---


## EC2 - Elastic Compute Cloud

![[EC2 Basics.png]]

- AMIs are required to launch EC2 instances. AMIs can be loosely compared to docker container images. AMIs are created from images that are from AWS / 3rd Party / custom image.
![[Excalidraw/EKS-ECS.excalidraw.md#^group=Re-9qBtZErFpzXSZqPKtd|EKS-ECS]]

## EC2 Instance Recovery

**Status Check**
Instance status check       -> Checks the EC2 VM.
System status check         -> Checks the underlying hardware  
Attached EBS status check   -> Checks the attached EBS volume

![[Excalidraw/EKS-ECS.excalidraw.md#^group=Ua3vQFqPGan9lFGCJSMvA|EC2 Recovery]]