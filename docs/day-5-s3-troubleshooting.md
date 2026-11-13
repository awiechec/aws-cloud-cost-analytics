# Day 5 — AWS S3 Troubleshooting Lab

## Project Overview

This lab focused on diagnosing and resolving common AWS CLI and Amazon S3 issues using a structured troubleshooting process.

The objective was to practice identifying errors, investigating potential causes, implementing solutions, and verifying successful resolution.

**Environment:**
- AWS Services: Amazon S3, AWS STS
- Development Environment: GitHub Codespaces (Linux)
- Tools: AWS CLI
- AWS Region: us-east-2 (Ohio)
- S3 Bucket: `northstar-cloud-analytics-aaron`

## Scenario 1 — Expired AWS Authentication Session

### Problem

While attempting to verify AWS authentication, the following error appeared:

```text
Your session has expired. Please reauthenticate using 'aws login'
```

### Investigation

Executed:

```bash
aws sts get-caller-identity --no-cli-pager
```

The command could not retrieve identity information because the existing AWS login session had expired.

### Resolution

Reauthenticated using:

```bash
aws login --remote
```

Completed the browser-based authentication process.

### Verification

Successfully restored AWS authentication and verified access using AWS CLI.

**Status:** Resolved

## Scenario 2 — Amazon S3 Object Not Found (404)

### Problem

Simulated an application requesting an incorrect S3 object key.

Executed:

```bash
aws s3api head-object --bucket northstar-cloud-analytics-aaron --key cloud_spending_2026.csv --no-cli-pager
```

Received:

```text
aws: [ERROR]: An error occurred (404) when calling the HeadObject operation: Not Found
```

### Investigation

Listed all objects in the bucket:

```bash
aws s3 ls s3://northstar-cloud-analytics-aaron/ --recursive
```

Discovered the existing object:

```text
2026-11-08 02:29:12        541 cloud_spending.csv
```

### Root Cause

The requested object key did not match the actual filename stored in S3.

- Incorrect key: `cloud_spending_2026.csv`
- Correct key: `cloud_spending.csv`

Amazon S3 requires an exact object key match.

### Resolution

Corrected the object key in the AWS CLI request.

### Verification

Executed:

```bash
aws s3api head-object --bucket northstar-cloud-analytics-aaron --key cloud_spending.csv --query '{KeySize:ContentLength,Encryption:ServerSideEncryption,FileType:ContentType}' --output json --no-cli-pager
```

Successfully retrieved the object's metadata, confirming the corrected request worked.

Verified object properties:

- Size: 541 bytes
- Content Type: text/csv
- Encryption: SSE-S3 (AES256)

**Status:** Resolved

## Troubleshooting Methodology

The following process was used throughout the lab:

1. Identify and reproduce the problem.
2. Examine the error message.
3. Investigate the relevant AWS resource.
4. Determine the root cause.
5. Apply the appropriate solution.
6. Verify that the issue is resolved.
7. Document the findings.

## Skills Developed

- AWS CLI troubleshooting
- AWS authentication and session management
- Amazon S3 object inspection
- HTTP 404 error investigation
- S3 object key verification
- AWS CLI query filtering
- Root cause analysis
- Incident documentation
- Cloud support fundamentals

## Conclusion

Successfully diagnosed and resolved two AWS troubleshooting scenarios involving expired authentication and incorrect S3 object keys.

This lab strengthened foundational cloud support skills by applying a structured troubleshooting process to AWS CLI and Amazon S3.