---
services:
  - Amazon S3
tags: ['aws', 's3']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon S3 Fundamentals
###  Active Recall
- Are there any critical limits or quotas to be aware of?

---

![[S3_1]]

- Must have a globally unique name
- S3 is a [[Public vs Private AWS Services|Public Service]], but access is **Private by default.**
- Not a global service - Buckets are created in a region.
- Objects have a **Key** and a **Value**
	- The key for every object is the FULL path: s3://my_bucket/_my_directory/my_subdirectory/my_file.some_extension_, where _s3://my_bucket/_my_directory/my_subdirectory/_ is called the **prefix**
	- The value is the content of the body. Max object size is 5TB (5000GB) and if _uploading_ a file greater than 5GB, must use multi-part upload.

> There are no directories in S3. Only keys - Keys are just long strings containing slashes /