
# Amazon S3 Bucket Review

## Project Overview

This exercise documents an operational review of an
Amazon S3 bucket used to store cloud spending data.

The objective is to verify object availability and
review basic storage security configurations.

## 1. Bucket Information

- AWS Service: Amazon S3
- Bucket Name: northstar-cloud-analytics-aaron
- AWS Region: US East (Ohio) us-east-2
- Stored File: cloud_spending.csv

## 2. Object Verification

- [X] Confirmed the CSV file exists.
- [X] Reviewed the file size.
- [X] Reviewed the last modified date.
- [X] Reviewed the storage class.

## 3. Security Review

- [X] Reviewed Block Public Access settings.
- [X] Reviewed bucket permissions.
- [X] Verified default encryption settings.

### Bucket Permissions

- Bucket Policy: Public access is blocked by the bucket's Block Public Access settings.
- ACL: ACLs are disabled.
- Object Ownership: Bucket owner enforced.

### Default Encryption

- Encryption Type: SSE-S3 (Amazon S3 managed keys).
- Bucket Key: Enabled.
- Blocked Encryption Type: SSE-C.

## 4. Versioning Review

- [X] Checked whether S3 Versioning is enabled.
- [X] Documented the current configuration.

- Bucket Versioning: Disabled.
- MFA Delete: Disabled.

## 5. Findings

Document your observations here:

- Object availability: cloud_spending.csv is present in the bucket.
- Public access configuration:Public access is blocked by Block Public Access settings.
- Encryption configuration: Default encryption is enabled using SSE-S3.
- Versioning configuration: Disabled

## 6. Conclusion

This review demonstrates basic Amazon S3
administration, resource inspection, and
cloud storage security awareness.

The bucket has public access protections enabled,
ACLs disabled, and default encryption configured
using SSE-S3.

Versioning is currently disabled, meaning previous
object versions are not being retained.

This exercise provided hands-on experience with
AWS storage configuration, security settings,
and operational documentation.

## Skills Practiced

- Amazon S3
- AWS Management Console
- Cloud storage administration
- Security configuration review
- Technical documentation
- Basic troubleshooting
