---
services:
  - AWS Secrets Manager
  - AWS KMS
  - AWS Lambda
  - Amazon RDS
  - Amazon Aurora
tags: ['aws', 'secrets-manager', 'security', 'rotation']
status: atomic
topic: AWS Data Engineering
domain: Data Security and Governance
created_at: 2025-12-29
---
## AWS Secrets Manager

###  Active Recall
- What's the difference between Secrets Manager and Parameter Store?
- How does automatic secret rotation work for databases?
- What happens when a secret is deleted?
- How do you share secrets across AWS accounts?

---

## Core Concepts

**AWS Secrets Manager** helps you protect secrets needed to access your applications, services, and IT resources. It provides **automatic rotation**, audit logging, and fine-grained access control.

### What is a Secret?

A secret can be:
- **Database credentials** (username, password)
- **API keys** and tokens
- **OAuth tokens**
- **Any binary secret** (up to 64KB)
- **Multi-value secrets** (JSON with multiple fields)

> [!INFO] **Secret Structure**
```json
{
  "username": "admin",
  "password": "secure-password-123",
  "host": "db.example.com",
  "port": "5432"
}
```

## Secrets Manager vs Parameter Store

| Feature                | Secrets Manager                                                     | Parameter Store (Standard)   | Parameter Store (Advanced)           |
| ---------------------- | ------------------------------------------------------------------- | ---------------------------- | ------------------------------------ |
| **Purpose**            | [[AWS Secrets Manager#Automatic Secret Rotation\|Secrets Rotation]] | Configuration + secrets      | Configuration + secrets              |
| **Secret size**        | Up to 64KB                                                          | Up to 4KB                    | Up to 8KB                            |
| **Automatic rotation** | Yes (built-in for RDS, DocumentDB, others with Lambda)              | No                           | No                                   |
| **Cost**               | $0.40/month + $0.05/10,000 API calls                                | Free (up to 10,000 requests) | $0.05/month + $0.05/10,000 API calls |
| **Encryption**         | KMS (required)                                                      | Optional KMS                 | KMS (required)                       |
| **Versioning**         | Automatic                                                           | Automatic                    | Automatic                            |
| **Use case**           | Secrets that need rotation                                          | Configuration data           | Secrets + sensitive config           |

> [!EXAM] **When to Use Which?**
> - **Secrets Manager:** Database credentials, API keys, OAuth tokens requiring rotation
> - **Parameter Store:** Application configuration, feature flags, connection strings (non-rotating)

## Automatic Secret Rotation

AWS Secrets Manager uses Lambda functions to rotate the secrets. For a supported list of services it can also rotate the authentication information stored within the service. Essential Secrets Manager provides functionality to rotate the secrets as well as keep services that have used those secrets in sync.

### Supported Services (Native Rotation)
AWS provides **built-in rotation templates** for 
 - **Amazon RDS** (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server), 
 - **Amazon Aurora**
 - **Amazon DocumentDB**
 - **Amazon Neptune**
 - **Amazon Redshift**


### Custom Rotation (Lambda Function)

For **unsupported services**, use a custom Lambda function:

**Rotation Lifecycle (4 Steps):**

1. **Create Secret:** Create a new version of the secret
2. **Set Secret:** Update the service/application with new secret
3. **Test Secret:** Verify the new secret works
4. **Finish Rotation:** Mark rotation successful

> [!WARNING] **Multi-User Pattern**
> Rotation creates TWO users:
> - **Primary user:** Currently in use
> - **Rotation user:** Used for rotation only
> - Secret stores BOTH credentials but returns primary to applications
> - Prevents application downtime during rotation

### Rotation Schedule
- **Frequency:** 1-365 days (configure as schedule expression)
- **Rotation window:** Within the configured period
- **Backward compatibility:** Old versions remain accessible (up to 100 versions)

> [!INFO] **Rotation Window**
> Rotation happens at random time within the schedule window to distribute load.
> - Example: Schedule "Every 30 days" → rotates between day 30-32

## Versioning and Retrieval

### Secret Versions
- Each rotation creates a **new version**
- Up to **100 versions** retained
- **Version with Stage AWSCURRENT** is what applications retrieve
- **Previous versions:** AWSPREVIOUS (immediate previous), version numbers

### Retrieve API
```bash
# Retrieve current secret (recommended)
aws secretsmanager get-secret-value \
  --secret-id prod/db-credentials \
  --version-stage AWSCURRENT

# Retrieve specific version
aws secretsmanager get-secret-value \
  --secret-id prod/db-credentials \
  --version-id 1234567890
```

> [!EXAM] **AWSCURRENT vs Specific Version**
> - **AWSCURRENT:** Always returns latest version (recommended for applications)
> - **Specific version:** Useful for rolling back if rotation breaks something

## Cross-Account Secret Access

### Pattern 1: Copy Secret (Simplest)
```
Account A (Source) → Account B (Destination)
```

**Steps:**
1. **Account A:** Create secret
2. **Account B:** Copy secret from Account A via AWS CLI/API
3. **Account B:** Secret is independent (changes don't sync)

**Limitation:** Changes in Account A don't propagate to Account B

### Pattern 2: Assume Role (Recommended)
```
Account A (Secret Owner) ← Account B (Consumer)
```

**Setup in Account A:**
1. Create IAM role with permission to access secret
2. Role trust policy allows Account B to assume it
3. KMS key policy allows Role B to decrypt secret

**Setup in Account B:**
1. Application assumes role in Account A
2. Retrieves secret using temporary credentials
3. No manual copy required

**IAM Policy for Secret Access:**
```json
{
  "Effect": "Allow",
  "Action": "secretsmanager:GetSecretValue",
  "Resource": "arn:aws:secretsmanager:REGION:ACCOUNT_A:secret:prod/db-creds-*"
}
```

> [!TIP] **Which Pattern to Choose?**
> - **Copy secret:** For one-time migration or when accounts are independent
> - **Assume role:** For ongoing access where changes should sync (recommended)

## Encryption with KMS

### Default Encryption
- All secrets encrypted using **AWS-managed KMS key** by default
- Optional: Use **customer-managed CMK** for compliance

### Using Customer-Managed CMK
1. Create CMK in AWS KMS
2. **Key policy** must allow Secrets Manager service to use it
3. Select CMK when creating/updating secret

> [!WARNING] **Key Rotation Impact**
> If you rotate the KMS key, Secrets Manager automatically re-encrypts all secret versions

## Deletion and Recovery

### Deleting a Secret
**Two options:**

1. **Schedule Deletion (Recovery possible)**
   - Minimum: 7 days, Maximum: 30 days
   - Secret immediately inaccessible
   - Can restore during recovery window

2. **Immediate Deletion (No recovery)**
   - Secret deleted immediately
   - No way to recover
   - Only for secrets with no dependencies

> [!WARNING] **Dependency Check**
> Before deleting, check:
> - Applications referencing the secret
> - Lambda functions with environment variables using it
> - CloudFormation stacks referencing it

## Integration with AWS Services

### Lambda Environment Variables
```yaml
# NOT RECOMMENDED - No rotation
Environment:
  DB_PASSWORD: "plain-text-password"

# RECOMMENDED - Use Secrets Manager
Environment:
  SECRET_ARN: "arn:aws:secretsmanager:region:account:secret:prod/db-creds"
```

**In Lambda code:**
```python
import boto3
import json

client = boto3.client('secretsmanager')

def get_secret():
    response = client.get_secret_value(
        SecretId='prod/db-creds'
    )
    return json.loads(response['SecretString'])
```

### RDS IAM Authentication
1. **Secret:** Stores database credentials (IAM user)
2. **Rotation:** Lambda rotates database password
3. **Database:** Configured with IAM authentication
4. **Application:** Uses IAM role to authenticate (not password)

> [!EXAM] **IAM Authentication vs Secret**
> - **IAM Authentication:** Application uses IAM role → no secret needed
> - **Secret-based:** Application retrieves secret → uses username/password
> - **Combination:** Secret stores IAM credentials for rotation

## Common Exam Patterns

### Pattern 1: RDS Password Rotation
**Question:** "Company needs to rotate RDS PostgreSQL password every 30 days without application downtime."

**Answer:**
- Create secret in Secrets Manager
- Enable automatic rotation (every 30 days)
- RDS must use IAM authentication
- AWS provides built-in rotation template
- Application retrieves `AWSCURRENT` version

### Pattern 2: API Key Rotation
**Question:** "External API key needs rotation every 90 days."

**Answer:**
- Create secret with API key
- **Custom Lambda function** for rotation
- Lambda calls external API to generate new key
- Lambda updates secret with new key
- Application always uses `AWSCURRENT`

### Pattern 3: Cross-Account Lambda Access
**Question:** "Lambda in Account B needs RDS credentials stored in Account A."

**Answer:**
- Account A: Create secret + IAM role with `secretsmanager:GetSecretValue`
- Account A: Role trust policy allows Account B
- Account B: Lambda assumes role in Account A → retrieves secret

### Pattern 4: Cost Optimization
**Question:** "100+ applications need same database credentials. Minimize cost."

**Answer:**
- Store secret once in Secrets Manager
- All applications retrieve same secret ARN
- **Cost:** $0.40/month (single secret) vs $40/month (100 Parameter Store Advanced tier secrets)

##  Use Cases

### When to Use Secrets Manager
1. **Database credentials** with automatic rotation
2. **API keys** and tokens requiring periodic rotation
3. **OAuth tokens** and authentication secrets
4. **Cross-account secret access** with controlled permissions
5. **Compliance requirements** for secret management and rotation

### When to Use Parameter Store
1. **Application configuration** (feature flags, settings)
2. **Small secrets** without rotation requirements (Standard tier = free)
3. **Configuration data** for infrastructure as code
4. **Secrets referenced by CloudFormation** (SSM parameters)

> [!EXAM] **Key Decision Factor**
> **Does it need automatic rotation?** → Yes = Secrets Manager, No = Parameter Store

---
## Related Services
- [[AWS KMS]] (encryption, key management)
- [[RDS and Aurora Fundamentals]] (database rotation)
- [[Lambda]] (custom rotation functions)
- [[AWS IAM]] (cross-account access, roles)
- [[Amazon Redshift]] (IAM authentication)
