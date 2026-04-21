---
services:
  - AWS CloudTrail
  - AWS IAM
  - AWS KMS
  - Amazon S3
tags: ['aws', 's3', 'security', 'encryption']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## S3 Security and Encryption
###  Active Recall
- Are there any critical limits or quotas to be aware of?
- How is data secured or encrypted in this context?

---

## Encryption
> [[AWS IAM#Resource-Based Policies|Bucket Policies]] are evaluated before Default Encryption (SS3-S3)

SSE-S3

- Handled managed and owned by AWS
- Server side encryption, AWS-256.
- The header should be set as "x-amz-Server-side-encryption: "AES256"
- Enabled by default for new buckets and objects

SSE-KMS:

- Handled by the users using KMS (Key Management System)
- User control and audit key usage using CloudTrail
- The header should be set as "x-amz-Server-side-encryption: "aws:kms"
- Access to the key stored in KMS is also required in addition to the access to the object stored in the bucket.
- **Limitations**: KMS has limits.
	- Upon upload, GenerateDataKey KMS API is called
	- Upon download, Decrypt KMS API is called.
	- KMS quota per second (5500, 10000, 30000 requests/second based on region)
- Quota increase can be requested using the Service Quota Console.

SSE-C:

- Customer Provided Keys
- User must upload the client-side key. HTTPS must be used and S3 will discard the key after use.

Client-Side Encryption:

- Encrypted objects are uploaded to S3.
- Objects are decrypted outside S3.

DSSE-KMS:

- Stands for - "Dual-Layer Server Side Encryption based on KMS"
- Not on the exam as of October 2025.