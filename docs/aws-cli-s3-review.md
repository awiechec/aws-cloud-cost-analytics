# Day 4 — AWS CLI & S3 Configuration Review

## Project Overview

This exercise introduces the AWS Command Line Interface (CLI) as a tool for inspecting Amazon S3 resources and verifying storage configurations.

The objective was to practice basic AWS CLI commands, verify resource availability, and compare command-line findings against the previous AWS Management Console review.

## 1. Environment

- Development Environment: GitHub Codespaces
- Operating System: Linux
- AWS CLI Version: 2.40.0
- AWS Region: us-east-2 (Ohio)
- S3 Bucket: northstar-cloud-analytics-aaron

## 2. AWS CLI Setup

- [x] Installed AWS CLI.
- [x] Verified AWS CLI installation.
- [x] Authenticated using AWS CLI browser-based login.
- [x] Verified AWS identity using AWS STS.

### Commands Used

```bash
aws --version
aws login --remote
aws sts get-caller-identity
```

## 3. S3 Object Verification

- [x] Listed available S3 buckets.
- [x] Located the project's existing S3 bucket.
- [x] Verified that cloud_spending.csv exists.

### Commands Used

```bash
aws s3 ls
aws s3 ls s3://northstar-cloud-analytics-aaron
```

## 4. S3 Configuration Review

### Bucket Versioning

Command:

```bash
aws s3api get-bucket-versioning --bucket northstar-cloud-analytics-aaron
```

**Finding:** The command returned no versioning configuration fields, consistent with the disabled status observed in the AWS Management Console.

### Block Public Access

Command:

```bash
aws s3api get-public-access-block --bucket northstar-cloud-analytics-aaron
```

**Findings:**

- BlockPublicAcls: true
- IgnorePublicAcls: true
- BlockPublicPolicy: true
- RestrictPublicBuckets: true

All four bucket-level public access protections are enabled.

### Default Encryption

Command:

```bash
aws s3api get-bucket-encryption --bucket northstar-cloud-analytics-aaron --no-cli-pager
```

**Findings:**

- Encryption Algorithm: AES256 (SSE-S3)
- Bucket Key: Enabled
- Blocked Encryption Type: SSE-C

## 5. Troubleshooting Experience

During setup, AWS CLI initially returned a command-not-found error because the tool was not installed.

After installing AWS CLI, an authentication error occurred because credentials had not yet been configured.

These issues were resolved by installing AWS CLI and completing browser-based authentication.

## 6. Conclusion

Successfully used AWS CLI to inspect an existing S3 bucket, verify object availability, and review storage security configurations.

This exercise provided hands-on experience with command-line administration, AWS authentication, configuration verification, and basic troubleshooting.

## Skills Practiced

- AWS Command Line Interface
- Amazon S3
- AWS STS
- Cloud resource inspection
- Cloud security fundamentals
- Troubleshooting CLI installation and authentication
- Technical documentation
