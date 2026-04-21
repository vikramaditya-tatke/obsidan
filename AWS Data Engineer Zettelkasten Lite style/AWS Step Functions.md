---
services:
  - AWS Step Functions
  - AWS Lambda
  - Amazon Athena
  - Amazon Glue
  - Amazon S3
  - Amazon SQS
  - Amazon SNS
  - Amazon EventBridge
  - AWS Batch
  - AWS Fargate
tags: ['aws', 'step-functions', 'orchestration', 'workflow']
status: atomic
topic: AWS Data Engineering
domain: Data Ingestion and Transformation
created_at: 2025-12-29
---
## AWS Step Functions

###  Active Recall
- What's the difference between Standard and Express workflows?
- How does Step Functions handle error handling and retries?
- What are task states and how do they integrate with AWS services?
- What's the difference between Wait and Choice states?

---

## Core Concepts

**AWS Step Functions** is a serverless **orchestration service** that lets you coordinate distributed applications and microservices using visual workflows.

### Workflow (State Machine)
A **state machine** defines a workflow as states and transitions. It has the following components -
- **States:** Individual steps in workflow
- **Transitions:** Arrows connecting states
- **Input/Output:** Data passed between states
- **Execution:** One run of the state machine

### Workflow Types

| Feature                | Standard Workflows                                              | Express Workflows                                              |
| ---------------------- | --------------------------------------------------------------- | -------------------------------------------------------------- |
| **Execution duration** | Up to 1 year                                                    | Up to 5 minutes                                                |
| **Execution start**    | At most 1 per request                                           | At most 2,000 per second                                       |
| **Pricing**            | $0.025 per 1,000 state transitions + $1/month per state machine | $0.025 per 1,000 state transitions + $0.00000025 per GB-second |
| **Use case**           | Long-running, complex workflows                                 | High-volume, event-driven workflows                            |
| **Exact count**        | Yes (audit)                                                     | No (at-least-once)                                             |

> [!EXAM] **Which to Choose?**
> - **Standard:** ETL pipelines, data processing jobs, approval workflows
> - **Express:** High-frequency events (e.g., IoT sensor data), real-time processing

## State Types

### Task State
Executes an activity or calls an AWS service.

**Supported Service Integrations:**

| Service | Integration Type | Common Use |
|---------|----------------|-------------|
| **AWS Lambda** | Sync/Async | Data transformation, validation |
| **AWS Batch** | Sync | Job submission, array jobs |
| **Amazon Athena** | Sync | Query execution |
| **Amazon Glue** | Sync | Job runs, crawlers |
| **Amazon S3** | Sync | Copy, delete objects |
| **Amazon SNS** | Sync | Publish to topic |
| **Amazon SQS** | Sync | Send message to queue |
| **Amazon EventBridge** | Sync | Put events to bus |
| **Amazon EMR** | Sync | Step execution |
| **Amazon Redshift** | Sync | Query execution |

> [!INFO] **Optimized Integration**
> Some services have **optimized integrations** (no Lambda needed):
> - `dynamodb:UpdateItem` → Direct DynamoDB call
> - `sns:Publish` → Direct SNS publish
> - `sqs:SendMessage` → Direct SQS send

### Choice State
Branches workflow based on conditional logic.

**Example:**
```json
"Choice": {
  "Type": "Choice",
  "Choices": [
    {
      "Variable": "$.status",
      "StringEquals": "success",
      "Next": "SuccessHandler"
    },
    {
      "Variable": "$.status",
      "StringEquals": "error",
      "Next": "ErrorHandler"
    }
  ],
  "Default": "DefaultHandler"
}
```

### Wait State
Delays workflow for a specified time.

**Types:**
- **Wait for seconds:** `"Seconds": 300`
- **Wait until timestamp:** `"Timestamp": "2025-12-31T12:00:00Z"`
- **Wait for task token:** Wait for external signal (callback pattern)

### Parallel State
Executes multiple branches concurrently.

**Example:**
```json
"Parallel": {
  "Type": "Parallel",
  "Branches": [
    {"StartAt": "Branch1"},
    {"StartAt": "Branch2"}
  ],
  "Next": "MergeResults"
}
```

> [!EXAM] **Parallel Execution**
> - All branches execute **concurrently**
> - Workflow waits for **ALL branches** to complete
> - Useful for parallel data processing (e.g., process multiple files)

### Map State
Iterates over an array, processing each element.

**Use Cases:**
- Process batch of files in S3
- Query multiple Athena queries in parallel
- Call Glue job for each partition

**Example:**
```json
"ProcessFiles": {
  "Type": "Map",
  "Iterator": {
    "StartAt": "ProcessFile",
    "States": {
      "ProcessFile": {
        "Type": "Task",
        "Resource": "arn:aws:lambda:region:account:function:ProcessFile",
        "End": true
      }
    }
  },
  "ItemsPath": "$.files",
  "MaxConcurrency": 10
}
```

> [!TIP] **Map vs. Parallel**
> - **Parallel:** Fixed number of concurrent branches
> - **Map:** Dynamic iteration over array (like for loop)

### Fail State
Stops execution with an error.

**Types:**
- **Fail:** Marks execution as failed
- **Succeed:** Marks execution as successful (even if incomplete)

### Pass State
Passes input to output without doing work (data transformation).

```json
"PassData": {
  "Type": "Pass",
  "Result": {
    "processedAt": "2025-12-29T12:00:00Z",
    "status": "completed"
  },
  "ResultPath": "$.metadata"
}
```

### Retry and Catch

**Retry:** Automatic retry on failure
```json
"TaskWithRetry": {
  "Type": "Task",
  "Resource": "arn:aws:lambda:region:account:function:ProcessData",
  "Retry": [
    {
      "ErrorEquals": ["Lambda.ServiceException", "Lambda.AWSLambdaException"],
      "IntervalSeconds": 2,
      "MaxAttempts": 3,
      "BackoffRate": 2.0
    }
  ],
  "Catch": [
    {
      "ErrorEquals": ["States.ALL"],
      "ResultPath": "$.error",
      "Next": "ErrorHandler"
    }
  ]
}
```

**Retry Parameters:**
- **IntervalSeconds:** Wait time between retries
- **MaxAttempts:** Maximum retry attempts
- **BackoffRate:** Exponential backoff multiplier (1.0 = linear, 2.0 = exponential)

**Catch:** Handle errors and route to alternative path
- **States.ALL:** Catch all errors
- **Custom errors:** Catch specific error types

> [!EXAM] **Exponential Backoff**
> - **BackoffRate: 2.0** = Retry delay doubles each attempt
> - Example: 2s, 4s, 8s, 16s (if MaxAttempts=4)

## Input/Output Processing

### ResultSelector
Extract specific fields from state output.

```json
"GetAthenaResults": {
  "Type": "Task",
  "Resource": "arn:aws:states:::athena:startQueryExecution",
  "ResultSelector": {
    "rows": "$.ResultSet.Rows",
    "queryId": "$.QueryExecutionId"
  }
}
```

### ResultPath
Where to put state output in JSON.

```json
"AddMetadata": {
  "Type": "Pass",
  "Result": {
    "timestamp": "2025-12-29",
    "user": "data-engineer"
  },
  "ResultPath": "$.metadata"  # Adds metadata to existing input
}
```

### Parameters
Configure input for task state.

```json
"ProcessFile": {
  "Type": "Task",
  "Resource": "arn:aws:lambda:region:account:function:ProcessFile",
  "Parameters": {
    "FunctionName": "ProcessFile",
    "Payload.$": "$"
  }
}
```

> [!TIP] **Parameters vs. ResultPath**
> - **Parameters:** Filter/transform input BEFORE state execution
> - **ResultPath:** Where to place output AFTER state execution

## Service Integration Patterns

### Optimized Integration
Direct call to AWS service (no Lambda needed).

**Example:** Execute Glue job
```json
"RunGlueJob": {
  "Type": "Task",
  "Resource": "arn:aws:states:::glue:startJobRun",
  "Parameters": {
    "JobName": "ETL-Job",
    "Arguments.$": "$.jobArguments"
  }
}
```

### AWS SDK Integration
Call any AWS service using AWS SDK (requires Lambda or custom code).

**When to Use:**
- Service without optimized integration
- Multiple API calls in sequence
- Complex logic not in optimized integration

### Callback Pattern
Task waits for external signal to complete.

**Use Cases:**
- Human approval workflow
- External API callback
- Long-running process with status polling

```json
"WaitForApproval": {
  "Type": "Task",
  "Resource": "arn:aws:states:::sns:publish",
  "TimeoutSeconds": 86400,  # 24 hours
  "HeartbeatSeconds": 3600,   # Send heartbeat every hour
  "Next": "CheckApproval"
}
```

> [!INFO] **Task Token**
> - Step Functions passes a **task token** to the service
> - Service must call `SendTaskSuccess` or `SendTaskFailure` with token
> - Execution continues only after success/failure callback

## Error Handling

### Error Types

| Error Category | Example Errors |
|---------------|----------------|
| **Service errors** | `Lambda.ServiceException`, `DynamoDB.ServiceException` |
| **SDK errors** | `Lambda.AWSLambdaException`, `S3.NoSuchKey` |
| **Custom errors** | Application-specific errors |
| **State errors** | `States.Timeout`, `States.TaskFailed`, `States.ALL` |

### Retry vs. Catch

**Retry:** Automatic recovery from transient errors
- Network timeouts
- Service throttling
- Temporary failures

**Catch:** Handle non-recoverable errors
- Invalid input
- Permission denied
- Business logic errors

### Fallback States

**Example:** Try direct S3 copy, fall back to Lambda
```json
"CopyWithFallback": {
  "Type": "Task",
  "Resource": "arn:aws:states:::s3:copyObject",
  "Retry": [
    {"ErrorEquals": ["States.ServiceException"], "MaxAttempts": 3}
  ],
  "Catch": [
    {
      "ErrorEquals": ["States.ALL"],
      "Next": "FallbackCopyWithLambda"
    }
  ],
  "Next": "Success"
}
```

## Data Pipeline Examples

### Pattern 1: ETL Pipeline
**Workflow:** Validate → Transform → Load → Notify

```json
{
  "Comment": "Data Pipeline",
  "StartAt": "ValidateInput",
  "States": {
    "ValidateInput": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:Validate",
      "Next": "TransformData"
    },
    "TransformData": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun",
      "Next": "LoadToWarehouse"
    },
    "LoadToWarehouse": {
      "Type": "Task",
      "Resource": "arn:aws:states:::redshift:executeStatement",
      "Next": "NotifySuccess"
    },
    "NotifySuccess": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "End": true
    }
  }
}
```

### Pattern 2: Parallel Processing
**Workflow:** Read S3 bucket → Process files in parallel → Merge results

```json
{
  "StartAt": "ListFiles",
  "States": {
    "ListFiles": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:ListS3Files",
      "Next": "ProcessInParallel"
    },
    "ProcessInParallel": {
      "Type": "Map",
      "ItemsPath": "$.files",
      "MaxConcurrency": 10,
      "Iterator": {
        "StartAt": "ProcessFile",
        "States": {
          "ProcessFile": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:region:account:function:ProcessFile",
            "End": true
          }
        }
      },
      "Next": "AggregateResults"
    },
    "AggregateResults": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:region:account:function:Aggregate",
      "End": true
    }
  }
}
```

### Pattern 3: Human Approval
**Workflow:** Submit for approval → Wait → Continue/Reject

```json
{
  "StartAt": "SubmitForApproval",
  "States": {
    "SubmitForApproval": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:region:account:approval-topic",
        "Message": {
          "workflow.$": "$"
        }
      },
      "Next": "WaitForApproval"
    },
    "WaitForApproval": {
      "Type": "Wait",
      "Seconds": 3600,
      "Next": "CheckApproval"
    },
    "CheckApproval": {
      "Type": "Task",
      "Resource": "arn:aws:states:::dynamodb:getItem",
      "Next": "Decision"
    },
    "Decision": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.Item.approvalStatus",
          "StringEquals": "approved",
          "Next": "ContinueWorkflow"
        }
      ],
      "Default": "RejectWorkflow"
    }
  }
}
```

## Monitoring and Observability

### CloudWatch Metrics

| Metric | Description | Alarm Threshold |
|--------|-------------|-----------------|
| **ExecutionsStarted** | Number of executions started | Monitor for spikes |
| **ExecutionsSucceeded** | Successful executions | Track success rate |
| **ExecutionsFailed** | Failed executions | Alert on failures |
| **ExecutionThrottled** | Throttled executions | Scale workflow |
| **ExecutionTime** | Time taken by executions | Identify slow workflows |

### CloudWatch Logs

**Automatic logging:**
- Standard workflows: Full execution history
- Express workflows: Sampled logs (5% by default)

**Use cases:**
- Debug failed executions
- Analyze performance
- Audit trail for compliance

### Step Functions Visual Workflow

**Console features:**
- **Graph view:** Visual representation of workflow
- **Execution history:** List of past executions
- **Execution details:** Input/output, state transitions
- **Inspect execution:** Step-by-step debugging

## Pricing Considerations

### Standard Workflow Pricing
- **State transitions:** $0.025 per 1,000 transitions
- **State machine:** $1.00 per month

**Example:** 100K executions/day, 10 states each
- **Daily cost:** (100,000 × 10 / 1,000 × $0.025) = $25
- **Monthly cost:** $25 × 30 + $1 = $751

### Express Workflow Pricing
- **State transitions:** $0.025 per 1,000 transitions
- **Duration:** $0.00000025 per GB-second

**Example:** 10M executions/day, 2 states each, 1 second each
- **Duration:** 10,000,000 × 1 second = 10M GB-seconds
- **Transitions:** 10,000,000 × 2 / 1,000 = 20K transitions
- **Daily cost:** (10M × $0.00000025) + (20K × $0.025 / 1,000) = $2.5 + $0.5 = $3

> [!TIP] **Cost Optimization**
> - **Express:** High volume, short duration
> - **Standard:** Long-running, infrequent
> - **Minimize states:** Combine steps where possible
> - **Map vs. Parallel:** Map for dynamic arrays

## Common Exam Patterns

### Pattern 1: Error Recovery with Retry
**Question:** "Data transformation Lambda fails intermittently due to throttling."

**Answer:**
- Use **Retry** in task state configuration
- Set `BackoffRate: 2.0` for exponential backoff
- Set `MaxAttempts: 5` for maximum retries
- Use `Catch` to route to error handler if all retries fail

### Pattern 2: Parallel File Processing
**Question:** "Process 1,000 files in S3 as fast as possible."

**Answer:**
- Use **Map state** to iterate over files
- Set `MaxConcurrency: 10` (or higher based on limits)
- Each iteration calls Lambda to process single file
- Workflow waits for all files to complete

### Pattern 3: Conditional Branching
**Question:** "Route to different Glue jobs based on file type (CSV vs. JSON)."

**Answer:**
- Use **Choice state** after file type detection
- Check `$.fileType` variable
- Branch to appropriate Glue job (CSV-Job or JSON-Job)
- Use **Default** branch for unsupported types

### Pattern 4: Human-in-the-Loop Approval
**Question:** "Production deployment requires approval from manager."

**Answer:**
- **Publish to SNS** (email notification)
- **Wait state** for approval callback
- **Choice state** to check approval status (approved/rejected)
- Continue to deployment if approved, terminate if rejected

### Pattern 5: Workflow Orchestration
**Question:** "Coordinate Glue ETL, Redshift loading, and notification."

**Answer:**
- **Step 1:** Start Glue job (task state)
- **Step 2:** Load to Redshift (task state) - waits for Glue to finish
- **Step 3:** Publish to SNS on success
- **Retry and Catch** on each step for error handling

##  Use Cases

### When to Use Step Functions
1. **Orchestrating multi-step workflows** (ETL pipelines, data processing)
2. **Error handling and retry logic** with visual workflow
3. **Human approval workflows** (deployment approvals, data access requests)
4. **Parallel processing** of multiple data sources
5. **Long-running processes** (Standard workflows up to 1 year)
6. **High-frequency event processing** (Express workflows)

### When NOT to Use Step Functions
1. **Simple, single-step operations** → Direct service call
2. **Real-time streaming (< 1 second)** → Use Kinesis
3. **Complex data transformations** → Use AWS Glue
4. **Stateless processing** → Use Lambda directly

> [!EXAM] **Step Functions vs. Glue Workflows**
> - **Step Functions:** Orchestrates ANY AWS service (stateful)
> - **Glue Workflows:** Orchestrates ONLY Glue jobs and crawlers (ETL-specific)

---
## Related Services
- [[Lambda]] (task execution, data transformation)
- [[AWS Glue Fundamentals]] (ETL jobs, crawlers)
- [[Amazon S3]] (data source/target)
- [[Amazon Athena]] (query execution)
- [[Redshift Data Loading COPY]] (data warehouse loading)
- [[Amazon SNS]] (notifications, callbacks)
- [[Amazon SQS]] (message queues)
- [[Amazon EventBridge]] (event-driven workflows)
- [[AWS Batch]] (job orchestration, array jobs)
