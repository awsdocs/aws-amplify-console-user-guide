# Encryption at rest<a name="encryption-at-rest"></a>

Encryption at rest refers to protecting your data from unauthorized access by encrypting data while stored\. Amplify encrypts an app's build artifacts by default using customer master keys \(CMKs\) for Amazon S3 that are managed by the AWS Key Management Service\.

Amplify uses Amazon CloudFront to serve your app to your customers\. CloudFront uses SSDs which are encrypted for edge location points of presence \(POPs\), and encrypted EBS volumes for Regional Edge Caches \(RECs\)\. Function code and configuration in CloudFront Functions is always stored in an encrypted format on the encrypted SSDs on the edge location POPs, and in other storage locations used by CloudFront\. 