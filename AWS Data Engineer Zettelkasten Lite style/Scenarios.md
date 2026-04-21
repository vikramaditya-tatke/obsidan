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
## Scenarios
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---


1. Your application on [[EC2|EC2]] creates images thumbnails after profile photos are uploaded to Amazon [[Amazon S3 Fundamentals|S3]].These thumbnails can be easily recreated, and only need to be kept for 60 days. The source images should be able to be immediately retrieved for these 60 days, and afterwards, the user can wait up to 6 hours. How would you design this?

Source Images: Use the *Standard* tier with a lifecycle configuration to transition them to Glacier after 60 days.

Thumbnails: use the One-Zone IA tier with a lifecyle configuration to transition to expire them after 60 days.

2. A rule in your company states that you should be able to recover your deleted [[Amazon S3 Fundamentals|S3]] objects immediately for 30 days, although this may happen rarely. After this time, and for up to 365 days, deleted objects should be recoverable within 48 hours.

Standard - Enable versioning so that deleted objects are hidden by a *delete marker* and transition them (non-current versions) to Standard IA.

Deep Archive - Transition the non-current versions using the lifecycle configuration to [[Amazon S3 Fundamentals|S3]] Deep Archive.

> [[Amazon S3 Fundamentals|S3]] Analytics - Recommendation for Standard and Standard IA