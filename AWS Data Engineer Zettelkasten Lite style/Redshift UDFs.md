---
services:
  - AWS IAM
  - Amazon Redshift
  - Amazon S3
tags: ['aws', 'redshift', 'udf']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Redshift UDFs
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[RedShift]]

## User Defined Functions (UDF)

```sql
CREATE [ OR REPLACE ] FUNCTION f_function_name
( [ argument_name arg_type, ... ] )
RETURNS data_type
{ VOLATILE | STABLE | IMMUTABLE }
AS $$
    python_program
$$ LANGUAGE plpythonu;


-- Importing Python's url Parse library to extract hostnames
CREATE FUNCTION f_hostname(url VARCHAR)
RETURNS varchar
IMMUTABLE AS $$
import urllib.parse
return urllib.parse.urlparse(url).hostname
$$ LANGUAGE plpythonu;

```