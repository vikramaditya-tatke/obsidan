
- Fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications, such as Salesforce, and AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Redshift. Examples-
	- Ingest contact records from Salesforce to Amazon Redshift
	- Pull support tickets from Zendesk to an Amazon S3 bucket.

- A trigger determines how a flow runs. The following are the supported flow trigger types:
	**Run on demand** — Users manually run the flow as needed.
	**Run on event** — Amazon AppFlow runs the flow in response to an event from an SaaS application.
	**Run on schedule** — Amazon AppFlow runs the flow on a recurring schedule

![[Pasted image 20251011194614.png]]

Amazon AppFlow provides both AWS managed and customer managed keys for encrypting connection data and data stored in Amazon S3 when it is a destination. We recommend that you use a customer managed keys, as it puts you in full control over your encrypted data. When you choose a customer managed keys, Amazon AppFlow attaches a resource policy to the KMS key that grants it access to the KMS key.