IAM Policies can be categorized into the following categories.
## Identity Policies
* Attached to an IAM identity (users, groups, and roles).
* Grant permissions to the identity itself, controlling what actions that identity can perform and on which resources.
* Can be AWS managed policies or customer managed policies (inline or standalone).

> Identity policies can only be attached to identities in your own account.
### Principal
Principal represents the entity that is allowed or denied access to AWS resources. It can be -
- IAM user
- IAM role
- AWS service
- Anonymous user

> An IAM Principal can only access an S3 object if the user IAM permissions allow it OR the resource policy allows it AND there's no explicit DENY.

## Resource Policies
* Attached to a resource (e.g., S3 buckets, SQS queues, KMS keys, Lambda functions).
* Specify who (which principal) has access to that specific resource and what actions they can perform on it.
* Are always inline policies, embedded directly into the resource.
- *[[S3]] Bucket Policies*: Bucket-wide rules from the S3 console - allows cross account
- *Object Access Control List (ACL)*: fine grained access control for objects in the bucket.
- *Bucket Access Controls List (ACL)*: fine grained access control for buckets in the account.

> Resource Policies can grant access to identities inside or outside your own account.






