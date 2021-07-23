# AWS Amplify Console User Guide

-----
*****Copyright &copy; Amazon Web Services, Inc. and/or its affiliates. All rights reserved.*****

-----
Amazon's trademarks and trade dress may not be used in 
     connection with any product or service that is not Amazon's, 
     in any manner that is likely to cause confusion among customers, 
     or in any manner that disparages or discredits Amazon. All other 
     trademarks not owned by Amazon are the property of their respective
     owners, who may or may not be affiliated with, connected to, or 
     sponsored by Amazon.

-----
## Contents
+ [Welcome to the AWS Amplify Console](welcome.md)
+ [Getting started with existing code](getting-started.md)
+ [Getting started with fullstack continuous deployments](deploy-backend.md)
+ [Deploy and host server-side rendered apps with Amplify](server-side-rendering-amplify.md)
+ [Set up custom domains](custom-domains.md)
   + [Understanding DNS terminology and concepts](understanding-dns-terminology-and-concepts.md)
   + [Add a custom domain managed by Amazon Route 53](to-add-a-custom-domain-managed-by-amazon-route-53.md)
   + [Add a custom domain managed by a third-party DNS provider](to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md)
   + [Add a custom domain managed by GoDaddy](to-add-a-custom-domain-managed-by-godaddy.md)
   + [Add a custom domain managed by Google Domains](to-add-a-custom-domain-managed-by-google-domains.md)
   + [Manage subdomains](to-manage-subdomains.md)
   + [Set up automatic subdomains for a Amazon Route 53 custom domain](to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md)
   + [Troubleshooting custom domains](custom-domain-troubleshoot-guide.md)
+ [Configuring build settings](build-settings.md)
   + [Monorepo build settings](monorepo-configuration.md)
+ [Feature branch deployments and team workflows](multi-environments.md)
   + [Team workflows with Amplify backend environments](team-workflows-with-amplify-cli-backend-environments.md)
   + [Pattern-based feature branch deployments](pattern-based-feature-branch-deployments.md)
   + [Automatic build-time generation of Amplify config](amplify-config-autogeneration.md)
   + [Conditional backend builds](conditional-backends.md)
   + [Use Amplify backends across apps](reuse-backends.md)
+ [Manual deploys](manual-deploys.md)
+ [Deploy to Amplify Console button](one-click.md)
+ [Web previews](pr-previews.md)
+ [Add end-to-end tests to your Amplify app](running-tests.md)
+ [Using redirects](redirects.md)
+ [Restricting access](access-control.md)
+ [Environment variables](environment-variables.md)
+ [Custom headers](custom-headers.md)
+ [Incoming webhooks](webhooks.md)
+ [Monitoring](access-logs.md)
+ [Notifications](notifications.md)
+ [Custom build images and live package updates](custom-build-image.md)
+ [Adding a service role to the Amplify Console when you connect an app](how-to-service-role-amplify-console.md)
+ [Managing app performance](ttl.md)
+ [Logging Amplify API calls using AWS CloudTrail](logging-using-cloudtrail.md)
+ [Security in Amplify](security.md)
   + [Identity and Access Management for Amplify](security-iam.md)
      + [How Amplify works with IAM](security_iam_service-with-iam.md)
      + [Identity-based policy examples for Amplify](security_iam_id-based-policy-examples.md)
      + [Troubleshooting Amplify identity and access](security_iam_troubleshoot.md)
      + [Amplify permissions reference](security_iam_permissions-reference.md)
   + [Security event logging and monitoring in Amplify](monitoring-overview.md)
   + [Data Protection in Amplify](data-protection.md)
      + [Encryption at rest](encryption-at-rest.md)
      + [Encryption in transit](encryption-in-transit.md)
      + [Encryption key management](encryption-key-management.md)
   + [Compliance Validation for AWS Amplify](Amplify-compliance.md)
   + [Infrastructure Security in AWS Amplify](infrastructure-security.md)
+ [AWS Amplify reference](aws-amplify-reference-chapter.md)
   + [AWS CloudFormation support](cloudformation-support-chapter.md)
   + [AWS Command Line Interface support](aws-cli-support-chapter.md)
   + [Resource tagging support](resource-tagging-support-chapter.md)
+ [Document history for AWS Amplify](document-history.md)