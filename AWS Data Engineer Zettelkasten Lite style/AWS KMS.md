---
services:
  - AWS KMS
  - Amazon S3
  - Amazon EBS
  - AWS Glue
tags: ['aws', 'kms', 'encryption', 'security']
status: atomic
topic: AWS Data Engineering
domain: Data Security and Governance
created_at: 2025-12-29
---
## AWS Key Management Service (KMS)

###  Active Recall
- What's the difference between AWS-managed CMKs and customer-managed CMKs?
- How does envelope encryption work with KMS?
- What's the difference between SSE-KMS and client-side encryption with KMS?
- What are the key usage limits for KMS?

---

## Core Concepts

**AWS KMS** is a managed service that makes it easy to create and control cryptographic keys used to encrypt data. It provides a centralized way to manage encryption keys across AWS services and applications.

### Customer Master Keys (CMKs)
KMS uses **Customer Master Keys** to encrypt and decrypt data keys. Two types:

| Key Type | Who Manages | Cost | Key Material | Key Policy | Can Be Disabled/Deleted | Rotated By |
|-----------|-------------|------|--------------|-------------|----------------------|-------------|
| **AWS-managed CMK** | AWS | Free | AWS generates | AWS manages | No (automatic) | AWS (every 3 years) |
| **Customer-managed CMK** | You | $1/month | You can import | You control | Yes | You (optional) or AWS (auto) |

### Symmetric vs Asymmetric Keys
- **Symmetric keys** (AES-256): Same key for encrypt/decrypt. Faster. Used for most data encryption.
- **Asymmetric keys** (RSA/ECDSA): Key pair (public/private). Used for signing, TLS, SSH.

### Key Policies
- **Resource-based policies** attached to CMKs
- Control who can use/manage the key
- Key administrators vs key users
- Can include IAM conditions (IP, time, MFA)
- **Cross-account access** possible via key policy

## Encryption Process: Envelope Encryption

1. **Generate Data Key:** Application requests KMS to generate a unique data key
2. **Encrypt Data:** Application uses plaintext data key to encrypt large amounts of data locally
3. **Encrypt Data Key:** KMS encrypts the data key using CMK
4. **Store:** Encrypted data + encrypted data key stored together
5. **Decrypt:** When needed, send encrypted data key to KMS → get plaintext data key → decrypt data

> [!INFO] Why Envelope Encryption?
> - KMS limits: 4KB/Request for direct encrypt/decrypt
> - Performance: Bulk encryption happens locally (faster)
> - Flexibility: Can rotate data keys without re-encrypting everything

## KMS vs SSE-S3 vs SSE-KMS

| Feature | SSE-S3 | SSE-KMS | Client-Side Encryption |
|---------|----------|-----------|---------------------|
| **Who manages keys** | AWS | AWS (KMS) | You |
| **Encryption location** | S3 service | S3 service | Before upload |
| **KMS API calls** | 0 | GenerateDataKey + Decrypt | 0 (unless using KMS) |
| **Cost** | Free | $0.002/GB + KMS costs | KMS costs only |
| **KMS limits** | No impact | Yes (5000-30000/sec/region) | No impact |

## Key Usage Limits (KMS Quotas)

**Per region limits:**
- **Cryptographic operations:** 5,000 requests/sec (default)
- **Can be increased to:** 10,000 or 30,000 requests/sec via support

**Why this matters for data engineering:**
- **S3 SSE-KMS:** Every upload/download calls KMS (GenerateDataKey/Decrypt)
- **High-throughput S3:** Can hit KMS limits → throttling → pipeline failures
- **Solution:** Use SSE-S3 for bulk operations, SSE-KMS for compliance

## Integration with AWS Services

### S3 Encryption
- **Default encryption:** Apply to bucket (SSE-S3 or SSE-KMS)
- **Bucket policies:** Evaluated BEFORE default encryption
- **KMS key:** Must have `kms:Decrypt` and `kms:GenerateDataKey` permissions

### EBS Encryption
- EBS volumes encrypted by default in new AWS accounts
- Snapshots inherit encryption from source volume
- **Cross-region snapshots:** Requires KMS key in destination region
- **Key policy:** Must allow EC2 service to use the key

### Glue Encryption
- Job bookmarks and temporary storage
- Data Catalog (optional)
- Connection credentials
- **Cross-account access:** KMS key sharing via key policy

### Lambda Environment Variables
- Can store secrets in environment variables (not recommended, use Secrets Manager)
- Encrypted at rest using KMS
- Requires `kms:Decrypt` permission for Lambda service role

## Key Rotation

### Automatic Rotation (Customer-managed keys)
- **AWS-managed rotation:** Every 3 years, cannot be disabled
- **Customer-managed rotation:** Optional, can be enabled/disabled
- **Rotation timeline:**
  - New key material created
  - Old key material still available for decryption
  - Applications automatically use new material
  - No re-encryption of data needed

> [!EXAM] **Key Rotation vs Key Version**
> - **Rotation:** Creates new key material for same CMK ID
> - **Key version:** Cryptographic material versions
> - Old versions still decrypt data encrypted with them
> - Only new encryptions use latest version

## Cross-Account Key Access

### Scenario: Account A encrypts S3 object, Account B needs to read

**Two approaches:**

**1. Resource-based policy on CMK (Recommended)**
```yaml
# Key policy in Account A
{
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::ACCOUNT_B:role/DataEngineer"},
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "*"
}
```

**2. IAM policy in Account B referencing key**
```yaml
# User/Role policy in Account B
{
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "arn:aws:kms:REGION:ACCOUNT_A:key/KEY_ID"
}
```

> [!WARNING] **Policy Conflict**
> If key policy denies, IAM policy cannot allow. Key policy is always evaluated first!

## KMS vs AWS Secrets Manager vs Parameter Store

| Feature | AWS KMS | Secrets Manager | Parameter Store |
|---------|-----------|-----------------|------------------|
| **Primary Use** | Encryption keys | Secrets (passwords, API keys) | Configuration + secrets |
| **Encryption** | Built-in | Uses KMS | Optional KMS encryption |
| **Rotation** | Key material only | Automatic secret rotation | No automatic rotation |
| **Cost** | $1/month per key | $0.40/month per secret + API calls | Free for standard tier |
| **Versioning** | Key versions | Secret versions | Version history |
| **Retrieval** | Encrypt/Decrypt APIs | GetSecretValue API | GetParameter API |

## Common Exam Patterns

### Pattern 1: S3 Upload Throttling
**Question:** "Company uploading 10TB/day to S3 with SSE-KMS. Getting throttling errors."

**Answer:** Switch to SSE-S3 or request KMS quota increase (10,000-30,000/sec).

### Pattern 2: Cross-Account Data Sharing
**Question:** "Account A encrypts S3 bucket, Account B needs access for analytics."

**Answer:**
1. Bucket policy allows Account B access
2. **KMS key policy** allows `kms:Decrypt` and `kms:GenerateDataKey` for Account B

### Pattern 3: EBS Snapshot Sharing
**Question:** "Need to share encrypted EBS snapshot across regions/accounts."

**Answer:**
- Cross-region: Need KMS key in destination region + copy grant
- Cross-account: Share snapshot + share KMS key via key policy

### Pattern 4: Glue Job Encryption
**Question:** "Glue job needs to access encrypted S3 data and store encrypted bookmarks."

**Answer:**
1. Create customer-managed CMK
2. Key policy allows Glue service role
3. IAM role has `kms:Decrypt` and `kms:GenerateDataKey`
4. Configure Glue job with KMS key

##  Use Cases

### When to Use AWS KMS
1. **Compliance requirements** (customer-managed keys, key rotation)
2. **Centralized key management** across multiple services
3. **Fine-grained access control** via key policies
4. **Envelope encryption** for large data volumes
5. **Cross-account data access** with controlled key permissions

### When to Use SSE-S3 Instead
1. **High-throughput S3 operations** (avoid KMS throttling)
2. **Cost optimization** (no KMS fees)
3. **Simple encryption** without audit requirements

### When to Use Client-Side Encryption
1. **Regulatory requirements** (keys never leave your premises)
2. **Encrypted before upload** to untrusted storage
3. **Custom encryption** using your own keys

> [!EXAM] **Critical Reminder**
> KMS is for **keys**, not secrets. Use AWS Secrets Manager for passwords/API keys that need automatic rotation.

---
## Related Services
- [[AWS IAM]] (key policies, IAM policies)
- [[S3 Security and Encryption|Amazon S3]] (SSE-S3, SSE-KMS)
- [[Amazon S3 Fundamentals|Amazon S3]] (default encryption)
- [[AWS Glue Fundamentals|AWS Glue]] (job encryption)
- [[Lambda]] (environment variable encryption)
- [[EBS Fundamentals|Amazon EBS]] (volume encryption)
- [[RDS and Aurora Fundamentals|Amazon RDS]] (database encryption)
