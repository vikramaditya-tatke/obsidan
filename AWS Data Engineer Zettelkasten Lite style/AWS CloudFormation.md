---
services:
  - AWS CloudFormation
  - AWS Lambda
  - Amazon EC2
  - Amazon S3
  - Amazon RDS
  - Amazon DynamoDB
  - AWS IAM
tags: ['aws', 'cloudformation', 'iac', 'infrastructure']
status: atomic
topic: AWS Data Engineering
domain: Data Operations and Support
created_at: 2025-12-29
---
## AWS CloudFormation

###  Active Recall
- What's the difference between a stack and a stack set?
- How does CloudFormation handle resource dependencies?
- What's a change set and when should you use it?
- What's drift detection and how does it work?

---

## Core Concepts

**AWS CloudFormation** is an **Infrastructure as Code (IaC)** service that lets you model, provision, and manage AWS and third-party resources by treating infrastructure as code.

### Key Components

| Component | Description | Analogy |
|-----------|-------------|-----------|
| **Template** | JSON/YAML file defining resources | Blueprint |
| **Stack** | Collection of AWS resources defined in template | Deployment instance |
| **Stack Set** | Collection of stacks across multiple accounts/regions | Multi-tenant deployment |
| **Change Set** | Planned changes to a stack | Migration plan |

> [!INFO] **Declarative vs. Imperative**
> - **CloudFormation:** Declarative (describe WHAT you want)
> - **CLI/SDK:** Imperative (describe HOW to create resources)

## Template Structure

### YAML vs. JSON

**YAML (Recommended):**
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Data Pipeline Stack"
Parameters:
  Environment:
    Type: String
    Default: dev
    AllowedValues:
      - dev
      - prod
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "${Environment}-data-bucket"
Outputs:
  BucketName:
    Description: "S3 Bucket Name"
    Value: !Ref MyBucket
```

**JSON:**
```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Data Pipeline Stack",
  "Parameters": {
    "Environment": {
      "Type": "String",
      "Default": "dev",
      "AllowedValues": ["dev", "prod"]
    }
  },
  "Resources": {
    "MyBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": { "Fn::Sub": "${Environment}-data-bucket" }
      }
    }
  },
  "Outputs": {
    "BucketName": {
      "Description": "S3 Bucket Name",
      "Value": { "Ref": "MyBucket" }
    }
  }
}
```

### Template Sections

| Section | Required | Description |
|---------|-----------|-------------|
| **AWSTemplateFormatVersion** |  Yes | Template format version |
| **Description** |  No | Stack description |
| **Parameters** |  No | Input values at stack creation |
| **Mappings** |  No | Conditional values (like lookup tables) |
| **Conditions** |  No | Logic for resource creation |
| **Resources** |  Yes | AWS resources to create |
| **Outputs** |  No | Values to export or use |

## Parameters

### Parameter Types

| Type | Example | When to Use |
|-------|----------|---------------|
| **String** | `"us-east-1"` | General text input |
| **Number** | `3` | Numeric values |
| **List<Number>** | `[1, 2, 3]` | Multiple numbers |
| **CommaDelimitedList** | `"a,b,c"` | CSV strings |
| **AWS-specific types** | `AWS::EC2::KeyPair::KeyName` | Validated AWS resource IDs |
| **SSM Parameter** | `AWS::SSM::Parameter::Value<String>` | Reference Parameter Store |

### Parameter Properties

```yaml
Parameters:
  VpcId:
    Type: AWS::EC2::VPC::Id
    Description: "VPC ID for resources"
    Default: vpc-12345678
  DatabaseSize:
    Type: String
    Default: "small"
    AllowedValues:
      - small
      - medium
      - large
    ConstraintDescription: "Must be small, medium, or large"
  DatabasePassword:
    Type: String
    NoEcho: true  # Masks value in console
    MinLength: 8
    MaxLength: 32
```

> [!TIP] **Parameter Validation**
> - **AllowedValues:** Restrict to specific options
> - **NoEcho:** Hide sensitive values (passwords, API keys)
> - **Min/Max Length:** Enforce complexity

## Mappings and Conditions

### Mappings
Lookup tables for conditional values.

```yaml
Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-12345678
    us-west-2:
      AMI: ami-87654321

Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !FindInMap [RegionMap, !Ref "AWS::Region", AMI]
```

### Conditions
Conditional resource creation.

```yaml
Conditions:
  IsProd: !Equals [!Ref Environment, "prod"]

Resources:
  ProdBucket:
    Type: AWS::S3::Bucket
    Condition: IsProd
    Properties:
      BucketName: prod-data-bucket
  DevBucket:
    Type: AWS::S3::Bucket
    Condition: !Not [IsProd]
    Properties:
      BucketName: dev-data-bucket
```

> [!EXAM] **Mapping vs. Parameter vs. Condition**
> - **Mapping:** Region/account-specific static values
> - **Parameter:** User input at stack creation
> - **Condition:** Boolean logic for conditional resources

## Intrinsic Functions

### String Manipulation
```yaml
!Sub "arn:aws:s3:::${AWS::AccountId}:bucket/${BucketName}"
!Join
  - "-"
  - - "my"
      - !Ref Environment
      - "bucket"
!Select [0, !Ref AvailabilityZones]  # Select first availability zone
!Split [",", "us-east-1a,us-east-1b"]  # Split string to list
```

### References
```yaml
!Ref LogicalId  # Reference another resource
!Ref ParameterName  # Reference parameter
```

### Logic
```yaml
!Equals [!Ref Environment, "prod"]
!Not [!Equals [!Ref Environment, "prod"]]
!And
  - !Equals [!Ref Environment, "prod"]
  - !Equals [!Ref Size, "large"]
!Or
  - !Equals [!Ref Environment, "prod"]
  - !Equals [!Ref Environment, "dev"]
!If
  - !Equals [!Ref Environment, "prod"]
  - prod-value
  - dev-value
```

### Others
```yaml
!GetAtt [LogicalId, Attribute]  # Get resource attribute
!GetAZs ""  # Get availability zones
!ImportValue ExportName  # Import from another stack
```

> [!INFO] **Most Common Functions**
> - `!Ref`: Reference resources/parameters
> - `!Sub`: String interpolation (ARNs, IDs)
> - `!GetAtt`: Get resource attributes (ARN, ID, DNS)
> - `!FindInMap`: Lookup from mappings

## Resource Attributes

### Common Resource Attributes

```yaml
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-bucket

Outputs:
  BucketArn:
    Description: "Bucket ARN"
    Value: !GetAtt MyBucket.Arn  # Get ARN attribute
  BucketName:
    Description: "Bucket Name"
    Value: !Ref MyBucket  # Get resource ID
```

### Reference Pattern Examples

```yaml
# Reference resource ID
!Ref MyBucket  # Returns: my-bucket

# Reference resource attribute
!GetAtt MyBucket.Arn  # Returns: arn:aws:s3:::123456789012:bucket/my-bucket
!GetAtt MyDDBTable.StreamArn  # Returns: DynamoDB Stream ARN

# Get pseudo parameter
!Ref "AWS::AccountId"  # Current account ID
!Ref "AWS::Region"  # Current region
```

## Nested Stacks

### When to Use Nested Stacks
- Reusable components (e.g., VPC, RDS, security groups)
- Overcome 500 resource limit per stack
- Organize large templates

### Parent-Child Stack Structure

```
Parent Stack
├── Nested Stack 1 (VPC)
├── Nested Stack 2 (RDS)
└── Nested Stack 3 (Lambda Functions)
```

```yaml
Resources:
  VPCStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/templates/vpc.yaml
      Parameters:
        Environment: !Ref Environment

  DatabaseStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/templates/rds.yaml
      Parameters:
        VpcId: !GetAtt VPCStack.Outputs.VpcId
        Environment: !Ref Environment
```

> [!WARNING] **Nested Stack Limits**
> - Maximum nesting depth: 5 levels
> - Each nested stack counts as 1 resource in parent

## Change Sets

### Change Set Process

1. **Create Change Set:** Preview changes without executing
2. **Review Change Set:** Examine what will be created/modified/deleted
3. **Execute Change Set:** Apply changes to stack

### Change Set Types

| Type | Description | When to Use |
|-------|-------------|---------------|
| **CREATE** | Initial stack creation | First deployment |
| **UPDATE** | Modify existing stack | Apply changes |
| **DELETE** | Remove stack | Cleanup |

```yaml
# Create change set
aws cloudformation create-change-set \
  --stack-name my-stack \
  --change-set-name my-change-set \
  --template-url https://s3.amazonaws.com/templates/update.yaml

# Review change set
aws cloudformation describe-change-set \
  --stack-name my-stack \
  --change-set-name my-change-set

# Execute change set
aws cloudformation execute-change-set \
  --stack-name my-stack \
  --change-set-name my-change-set
```

> [!EXAM] **Change Set Benefits**
> - **Preview changes** before applying
> - **Rollback protection** (automatic on failure)
> - **Controlled deployment** in production

## Drift Detection

### What is Drift?

**Drift** occurs when actual AWS resources differ from CloudFormation template definition.

**Causes:**
- Manual changes via Console/CLI
- External tools modifying resources
- Out-of-sync deployments

### Enabling Drift Detection

```yaml
# Enable on stack
aws cloudformation detect-stack-drift \
  --stack-name my-stack

# Check drift status
aws cloudformation describe-stack-resource-drifts \
  --stack-name my-stack
```

### Drift States

| State | Description |
|--------|-------------|
| **IN_SYNC** | Resource matches template |
| **MODIFIED** | Resource manually changed |
| **DELETED** | Resource deleted manually |
| **NOT_CHECKED** | Drift not yet checked |

> [!WARNING] **Drift Costs**
> - Detect stack drift: Free
> - Detect stack set drift: Charged per resource
> - Monitor drift: Use CloudWatch Events

## Stack Policies

### Update Protection

Prevents accidental stack deletion.

```yaml
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: critical-data
    DeletionPolicy: Retain  # Keep bucket on stack delete
```

| Policy | Behavior |
|---------|-----------|
| **Delete** (default) | Delete resource on stack delete |
| **Retain** | Keep resource on stack delete |
| **Snapshot** (for supported resources) | Create snapshot before delete |

### Termination Protection

Prevents stack deletion (even with `--force`).

```yaml
# Enable via CLI
aws cloudformation update-termination-protection \
  --stack-name my-stack \
  --enable-termination-protection
```

> [!INFO] **Delete Policy vs. Termination Protection**
> - **Delete Policy:** Per-resource (retain on delete)
> - **Termination Protection:** Stack-level (prevent delete entirely)

## Cross-Stack References

### Exports and Imports

**Export:** Share value with other stacks
**Import:** Use value from another stack

```yaml
# Export value (stack 1)
Outputs:
  VpcId:
    Description: "VPC ID"
    Value: !Ref MyVPC
    Export:
      Name: !Sub "${AWS::StackName}-VpcId"

# Import value (stack 2)
Resources:
  MySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Fn::ImportValue: !Sub "${OtherStackName}-VpcId"
```

> [!WARNING] **Import Limitations**
> - Cannot import from same stack (circular dependency)
> - Export must exist in same region
> - Only one stack can delete/export at a time

## Stack Sets

### Multi-Account/Region Deployment

Deploy the same template across multiple accounts and regions.

```yaml
# Create stack set
aws cloudformation create-stack-set \
  --stack-set-name my-stack-set \
  --template-url https://s3.amazonaws.com/templates/app.yaml

# Deploy to accounts/regions
aws cloudformation create-stack-instances \
  --stack-set-name my-stack-set \
  --accounts 123456789012,987654321098 \
  --regions us-east-1,us-west-2
```

**Use Cases:**
- **Multi-region deployment** (DR, global services)
- **Multi-account deployment** (dev/test/prod accounts)
- **Organizational units** (deploy to all accounts in OU)

## Rollback

### Automatic Rollback

CloudFormation **automatically rolls back** on failure.

**Rollback triggers:**
- Resource creation failure
- Update failure
- Deployment timeout
- Manual cancellation

### Rollback Triggers

| Trigger | Behavior |
|---------|-----------|
| **Failure** | Revert all changes, delete new resources |
| **Update failure** | Restore previous resource state |
| **Timeout** | Cancel deployment, clean up created resources |

### Disabling Rollback

```yaml
# Disable for troubleshooting
aws cloudformation update-stack \
  --stack-name my-stack \
  --disable-rollback
```

> [!WARNING] **Rollback Considerations**
> - Some resources **cannot be rolled back** (e.g., deleted S3 objects)
> - **Rollback costs** may apply for resources kept during rollback
> - Use **change sets** to preview and prevent rollback

## CloudFormation Linter (cfn-lint)

Validate templates for errors and best practices.

```bash
# Install
npm install -g @aws-cdk/cfn-lint

# Lint template
cfn-lint template.yaml
```

**Checks:**
- Syntax errors
- Best practices violations
- Security warnings
- Missing required properties

> [!TIP] **Lint Before Deploy**
> Always lint templates to catch errors before deployment

## Common Exam Patterns

### Pattern 1: Cross-Account Resource Sharing
**Question:** "Stack in Account A needs to reference VPC in Account B."

**Answer:**
1. Stack A exports VPC ID
2. Stack B imports VPC ID using `Fn::ImportValue`
3. Both stacks in same region
4. VPC resource in Stack A uses `DeletionPolicy: Retain`

### Pattern 2: Conditional Resource Creation
**Question:** "Create RDS only in production, not dev."

**Answer:**
```yaml
Conditions:
  IsProd: !Equals [!Ref Environment, "prod"]

Resources:
  ProductionRDS:
    Type: AWS::RDS::DBInstance
    Condition: IsProd
    Properties:
      # RDS configuration
```

### Pattern 3: Mapped AMI by Region
**Question:** "Deploy EC2 in multiple regions with correct AMIs."

**Answer:**
```yaml
Mappings:
  RegionAMI:
    us-east-1:
      AMI: ami-12345
    us-west-2:
      AMI: ami-67890

Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !FindInMap [RegionAMI, !Ref "AWS::Region", AMI]
```

### Pattern 4: Drift Detection
**Question:** "Manual changes made via Console. How to detect?"

**Answer:**
- Run `detect-stack-drift` on stack
- Review `describe-stack-resource-drifts`
- Resources with `MODIFIED` or `DELETED` state indicate drift
- Update stack to sync with template (use change set)

### Pattern 5: Nested Stacks for Reusability
**Question:** "Need to deploy VPC + RDS + Lambda across 10 environments."

**Answer:**
1. Create separate templates for VPC, RDS, Lambda
2. Create parent stack with nested stacks
3. Pass parameters to nested stacks (e.g., Environment)
4. Deploy parent stack (deploys all nested stacks)

##  Use Cases

### When to Use CloudFormation
1. **Infrastructure as Code** (version control, reproducibility)
2. **Multi-resource deployment** (coordinated creation)
3. **Environments** (dev, test, prod with same template)
4. **Disaster recovery** (quickly recreate infrastructure)
5. **Multi-account/region** deployment (stack sets)
6. **Drift prevention** (enforce desired state)

### When NOT to Use CloudFormation
1. **Ad-hoc resource creation** (quick testing)
2. **Frequent changes** not captured in code (use SDK/CLI)
3. **Simple, single-resource** (easier with Console)
4. **Non-AWS resources** (consider Terraform or custom tools)

> [!EXAM] **CloudFormation vs. CDK vs. Terraform**
> - **CloudFormation:** AWS-native, JSON/YAML, no transpilation
> - **CDK:** Programming languages (Python, TypeScript), transpiles to CloudFormation
> - **Terraform:** Multi-cloud, HCL, state file management

---
## Related Services
- [[AWS IAM]] (service roles, permissions)
- [[Lambda]] (custom resources, CloudFormation custom resources)
- [[Amazon S3 Fundamentals]] (template storage, nested stacks)
- [[Amazon EC2]] (compute resources)
- [[RDS and Aurora Fundamentals]] (database resources)
- [[DynamoDB Capacity Modes]] (NoSQL resources)
