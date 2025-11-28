IAM Policies can be categorized into two - 

# User-Based Policies
*Theses policies ascertain the API calls that should be allowed for a specific user from IAM*

# Resource-Based Policies
- *Bucket Policies*: Bucket-wide rules from the S3 console - allows cross account
- *Object Access Control List (ACL)*: fine grained access control for objects in the bucket.
- *Bucket Access Controls List (ACL)*: fine grained access control for buckets in the account.
> an IAM Principal can only access an S3 object if the user IAM permissions allow it OR the resource policy allows it AND there's no explicit DENY.

# Principal
_Principal represents the entity that is allowed or denied access to AWS resources. It can be an IAM user, an IAM role, an AWS service, or even an anonymous user_




