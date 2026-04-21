---
services:
  - Amazon AppFlow
  - Amazon Redshift
  - Amazon S3
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## AppFlow
###  Active Recall
- How does this service integrate with other AWS components mentioned?

---


- Fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications, such as Salesforce, and AWS services, such as Amazon Simple Storage Service (Amazon [[Amazon S3 Fundamentals|S3]]) and Amazon [[Redshift Data Loading COPY|Redshift]]. Examples-
	- Ingest contact records from Salesforce to Amazon [[Redshift Data Loading COPY|Redshift]]
	- Pull support tickets from Zendesk to an Amazon [[Amazon S3 Fundamentals|S3]] bucket.

### Trigger Types
A trigger determines how a flow runs. Amazon AppFlow supports the following trigger types:

| Trigger Type | Description | Primary Use Case | Key Features/Modes |
| :--- | :--- | :--- | :--- |
| **Run on Demand** | Manual initiation by the user. | Ad-hoc transfers, one-time imports, or full manual control. | Triggered via Console or `StartFlow` API. |
| **Run on Schedule** | Recurring execution based on a defined schedule. | Regular batch syncs (e.g., daily reports, hourly updates). | Supports **Incremental** (CDC/Timestamps) and **Full** transfers. |
| **Run on Event** | Automatic execution in response to source events. | Real-time or near-real-time data processing. | Uses webhooks/subscriptions. Supported by Salesforce, S3, etc. |

> [!INFO] Exam Tip
> If a question mentions "real-time data integration" or "triggering on new data arrival," choose **Run on Event**. For periodic batch transfers, use **Run on Schedule**. Manual control is **Run on Demand**.


> [!INFO] Exam Tip
> If a question mentions "real-time data integration" or "triggering on new data arrival," choose **Run on Event**. For periodic batch transfers, use **Run on Schedule**. Manual control is **Run on Demand**.

![[Pasted image 20251011194614.png]]

## Security
- Amazon AppFlow provides both AWS managed and customer managed keys for encrypting connection data and data stored in Amazon [[Amazon S3 Fundamentals|S3]] when it is a destination. 
- Customer managed keys are recommended, for full control over your encrypted data. When CMK, Amazon AppFlow attaches a resource policy to the KMS key that grants it access to the KMS key.