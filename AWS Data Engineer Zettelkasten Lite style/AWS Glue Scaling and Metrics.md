---
services:
  - AWS Glue
tags: ['aws', 'glue', 'scaling']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## AWS Glue Scaling and Metrics
###  Active Recall
- Are there any critical limits or quotas to be aware of?
- How to identify whether right amount of **DPUs** have been allocated for a job?

---


## Job Metrics
**AWS Glue** provides a feature called job metrics, which can be used to estimate the number of DPUs that can be used to scale out an AWS Glue job. This feature is particularly useful in understanding the resource utilization of your jobs and can help in making informed decisions about scaling.

When you run a job, AWS Glue provides metrics such as -
1. the number of maximum allocated executors
2. the number of maximum needed executors
3. the number of completed stages

Plotting a graph of metrics 1 and 2, in the Glue Console can give you insights into whether your job is under-provisioned or over-provisioned.

For example, if the number of maximum needed executors is significantly higher than the number of active executors, it indicates that the job is under-provisioned. In such a case, you can increase the maximum capacity job parameter, which effectively increases the number of DPUs allocated to the job.