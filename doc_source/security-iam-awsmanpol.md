# AWS managed policies for AWS Amplify<a name="security-iam-awsmanpol"></a>







To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself\. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need\. To get started quickly, you can use our AWS managed policies\. These policies cover common use cases and are available in your AWS account\. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*\.

AWS services maintain and update AWS managed policies\. You can't change the permissions in AWS managed policies\. Services occasionally add additional permissions to an AWS managed policy to support new features\. This type of update affects all identities \(users, groups, and roles\) where the policy is attached\. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available\. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions\.

Additionally, AWS supports managed policies for job functions that span multiple services\. For example, the **ReadOnlyAccess** AWS managed policy provides read\-only access to all AWS services and resources\. When a service launches a new feature, AWS adds read\-only permissions for new operations and resources\. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*\.









## AWS managed policy: AdministratorAccess\-Amplify<a name="security-iam-awsmanpol-AdministratorAccess-Amplify"></a>





You can attach `AdministratorAccess-Amplify` to your IAM entities\. Amplify also attaches this policy to a service role that allows Amplify to perform actions on your behalf\. When you deploy a backend in the Amplify console, you must create an `Amplify-Backend Deployment` service role that Amplify uses to create and manage AWS resources\. IAM attaches the `AdministratorAccess-Amplify` managed policy to the `Amplify-Backend Deployment` service role\.



This policy grants account administrative permissions while explicity allowing direct access to resources that Amplify applications require to create and manage backends\.



**Permissions details**

This policy provides access to multiple AWS services, including IAM actions\. These actions allow identities with this policy to use AWS Identity and Access Management to create other identities with any permissions\. This allows permissions escalation and this policy should be considered as powerful as the `AdministratorAccess` policy\.







```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CLICloudformationPolicy",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateChangeSet",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeChangeSet",
                "cloudformation:DescribeStackEvents",
                "cloudformation:DescribeStackResource",
                "cloudformation:DescribeStackResources",
                "cloudformation:DescribeStacks",
                "cloudformation:ExecuteChangeSet",
                "cloudformation:GetTemplate",
                "cloudformation:UpdateStack",
                "cloudformation:ListStackResources",
                "cloudformation:DeleteStackSet",
                "cloudformation:DescribeStackSet",
                "cloudformation:UpdateStackSet"
            ],
            "Resource": [
                "arn:aws:cloudformation:*:*:stack/amplify-*"
            ]
        },
        {
            "Sid": "CLIManageviaCFNPolicy",
            "Effect": "Allow",
            "Action": [
                "iam:ListRoleTags",
                "iam:TagRole",
                "iam:AttachRolePolicy",
                "iam:CreatePolicy",
                "iam:DeletePolicy",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:PutRolePolicy",
                "iam:UpdateRole",
                "iam:GetRole",
                "iam:GetPolicy",
                "iam:GetRolePolicy",
                "iam:PassRole",
                "iam:ListPolicyVersions",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:CreateRole",
                "iam:ListRolePolicies",
                "iam:PutRolePermissionsBoundary",
                "iam:DeleteRolePermissionsBoundary",
                "appsync:CreateApiKey",
                "appsync:CreateDataSource",
                "appsync:CreateFunction",
                "appsync:CreateResolver",
                "appsync:CreateType",
                "appsync:DeleteApiKey",
                "appsync:DeleteDataSource",
                "appsync:DeleteFunction",
                "appsync:DeleteResolver",
                "appsync:DeleteType",
                "appsync:GetDataSource",
                "appsync:GetFunction",
                "appsync:GetIntrospectionSchema",
                "appsync:GetResolver",
                "appsync:GetSchemaCreationStatus",
                "appsync:GetType",
                "appsync:GraphQL",
                "appsync:ListApiKeys",
                "appsync:ListDataSources",
                "appsync:ListFunctions",
                "appsync:ListGraphqlApis",
                "appsync:ListResolvers",
                "appsync:ListResolversByFunction",
                "appsync:ListTypes",
                "appsync:StartSchemaCreation",
                "appsync:UpdateApiKey",
                "appsync:UpdateDataSource",
                "appsync:UpdateFunction",
                "appsync:UpdateResolver",
                "appsync:UpdateType",
                "appsync:TagResource",
                "appsync:CreateGraphqlApi",
                "appsync:DeleteGraphqlApi",
                "appsync:GetGraphqlApi",
                "appsync:ListTagsForResource",
                "appsync:UpdateGraphqlApi",
                "apigateway:DELETE",
                "apigateway:GET",
                "apigateway:PATCH",
                "apigateway:POST",
                "apigateway:PUT",
                "cognito-idp:CreateUserPool",
                "cognito-identity:CreateIdentityPool",
                "cognito-identity:DeleteIdentityPool",
                "cognito-identity:DescribeIdentity",
                "cognito-identity:DescribeIdentityPool",
                "cognito-identity:SetIdentityPoolRoles",
                "cognito-identity:GetIdentityPoolRoles",
                "cognito-identity:UpdateIdentityPool",
                "cognito-idp:CreateUserPoolClient",
                "cognito-idp:DeleteUserPool",
                "cognito-idp:DeleteUserPoolClient",
                "cognito-idp:DescribeUserPool",
                "cognito-idp:DescribeUserPoolClient",
                "cognito-idp:ListTagsForResource",
                "cognito-idp:ListUserPoolClients",
                "cognito-idp:UpdateUserPoolClient",
                "cognito-idp:CreateGroup",
                "cognito-idp:DeleteGroup",
                "cognito-identity:TagResource",
                "cognito-idp:TagResource",
                "cognito-idp:UpdateUserPool",
                "cognito-idp:SetUserPoolMfaConfig",
                "lambda:AddPermission",
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:GetFunctionConfiguration",
                "lambda:InvokeAsync",
                "lambda:InvokeFunction",
                "lambda:RemovePermission",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "lambda:ListTags",
                "lambda:TagResource",
                "lambda:UntagResource",
                "lambda:AddLayerVersionPermission",
                "lambda:CreateEventSourceMapping",
                "lambda:DeleteEventSourceMapping",
                "lambda:DeleteLayerVersion",
                "lambda:GetEventSourceMapping",
                "lambda:GetLayerVersion",
                "lambda:ListEventSourceMappings",
                "lambda:ListLayerVersions",
                "lambda:PublishLayerVersion",
                "lambda:RemoveLayerVersionPermission",
                "lambda:GetLayerVersionByArn",
                "dynamodb:CreateTable",
                "dynamodb:DeleteItem",
                "dynamodb:DeleteTable",
                "dynamodb:DescribeContinuousBackups",
                "dynamodb:DescribeTable",
                "dynamodb:DescribeTimeToLive",
                "dynamodb:ListStreams",
                "dynamodb:PutItem",
                "dynamodb:TagResource",
                "dynamodb:ListTagsOfResource",
                "dynamodb:UpdateContinuousBackups",
                "dynamodb:UpdateItem",
                "dynamodb:UpdateTable",
                "dynamodb:UpdateTimeToLive",
                "s3:CreateBucket",
                "s3:ListBucket",
                "s3:PutBucketAcl",
                "s3:PutBucketCORS",
                "s3:PutBucketNotification",
                "s3:PutBucketPolicy",
                "s3:PutBucketWebsite",
                "s3:PutObjectAcl",
                "cloudfront:CreateCloudFrontOriginAccessIdentity",
                "cloudfront:CreateDistribution",
                "cloudfront:DeleteCloudFrontOriginAccessIdentity",
                "cloudfront:DeleteDistribution",
                "cloudfront:GetCloudFrontOriginAccessIdentity",
                "cloudfront:GetCloudFrontOriginAccessIdentityConfig",
                "cloudfront:GetDistribution",
                "cloudfront:GetDistributionConfig",
                "cloudfront:TagResource",
                "cloudfront:UntagResource",
                "cloudfront:UpdateCloudFrontOriginAccessIdentity",
                "cloudfront:UpdateDistribution",
                "events:DeleteRule",
                "events:DescribeRule",
                "events:ListRuleNamesByTarget",
                "events:PutRule",
                "events:PutTargets",
                "events:RemoveTargets",
                "mobiletargeting:GetApp",
                "kinesis:AddTagsToStream",
                "kinesis:CreateStream",
                "kinesis:DeleteStream",
                "kinesis:DescribeStream",
                "kinesis:PutRecords",
                "es:AddTags",
                "es:CreateElasticsearchDomain",
                "es:DeleteElasticsearchDomain",
                "es:DescribeElasticsearchDomain",
                "s3:PutEncryptionConfiguration"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "cloudformation.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "CLISDKCalls",
            "Effect": "Allow",
            "Action": [
                "appsync:GetIntrospectionSchema",
                "appsync:GraphQL",
                "appsync:UpdateApiKey",
                "appsync:ListApiKeys",
                "amplify:*",
                "amplifybackend:*",
                "sts:AssumeRole",
                "mobiletargeting:*",
                "cognito-idp:AdminAddUserToGroup",
                "cognito-idp:AdminCreateUser",
                "cognito-idp:CreateGroup",
                "cognito-idp:DeleteGroup",
                "cognito-idp:DeleteUser",
                "cognito-idp:ListUsers",
                "cognito-idp:AdminGetUser",
                "cognito-idp:ListUsersInGroup",
                "cognito-idp:AdminDisableUser",
                "cognito-idp:AdminRemoveUserFromGroup",
                "cognito-idp:AdminResetUserPassword",
                "cognito-idp:AdminListGroupsForUser",
                "cognito-idp:ListGroups",
                "cognito-idp:AdminListUserAuthEvents",
                "cognito-idp:AdminDeleteUser",
                "cognito-idp:AdminConfirmSignUp",
                "cognito-idp:AdminEnableUser",
                "cognito-idp:AdminUpdateUserAttributes",
                "cognito-idp:DescribeIdentityProvider",
                "cognito-idp:DescribeUserPool",
                "cognito-idp:DeleteUserPool",
                "cognito-idp:DescribeUserPoolClient",
                "cognito-idp:CreateUserPool",
                "cognito-idp:CreateUserPoolClient",
                "cognito-idp:UpdateUserPool",
                "cognito-idp:AdminSetUserPassword",
                "cognito-idp:ListUserPools",
                "cognito-idp:ListUserPoolClients",
                "cognito-identity:GetIdentityPoolRoles",
                "cognito-identity:SetIdentityPoolRoles",
                "cognito-identity:CreateIdentityPool",
                "cognito-identity:DeleteIdentityPool",
                "cognito-identity:ListIdentityPools",
                "cognito-identity:DescribeIdentityPool",
                "dynamodb:DescribeTable",
                "dynamodb:ListTables",
                "lambda:GetFunction",
                "lambda:CreateFunction",
                "lambda:AddPermission",
                "lambda:DeleteFunction",
                "lambda:InvokeFunction",
                "iam:PutRolePolicy",
                "iam:CreatePolicy",
                "iam:AttachRolePolicy",
                "iam:ListPolicyVersions",
                "iam:ListAttachedRolePolicies",
                "iam:CreateRole",
                "iam:PassRole",
                "iam:ListRolePolicies",
                "iam:DeleteRolePolicy",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:DeleteRole",
                "iam:DetachRolePolicy",
                "cloudformation:ListStacks",
                "sns:CreateSMSSandboxPhoneNumber",
                "sns:GetSMSSandboxAccountStatus",
                "sns:VerifySMSSandboxPhoneNumber",
                "sns:DeleteSMSSandboxPhoneNumber",
                "sns:ListSMSSandboxPhoneNumbers",
                "sns:ListOriginationNumbers",
                "rekognition:DescribeCollection",
                "logs:DescribeLogStreams",
                "logs:GetLogEvents",
                "lex:GetBot",
                "lex:GetBuiltinIntent",
                "lex:GetBuiltinIntents",
                "lex:GetBuiltinSlotTypes,
                "cloudformation:GetTemplateSummary",
                "codecommit:GitPull"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AmplifySSMCalls",
            "Effect": "Allow",
            "Action": [
                "ssm:PutParameter",
                "ssm:DeleteParameter",
                "ssm:GetParametersByPath",
                "ssm:GetParameters",
                "ssm:GetParameter",
                "ssm:DeleteParameters"
            ],
            "Resource": "arn:aws:ssm:*:*:parameter/amplify/*"
        },
        {
            "Sid": "GeoPowerUser",
            "Effect": "Allow",
            "Action": [
                "geo:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AmplifyStorageSDKCalls",
            "Effect": "Allow",
            "Action": [
               "s3:CreateBucket",
               "s3:DeleteBucket",
               "s3:DeleteBucketPolicy",
               "s3:DeleteBucketWebsite",
               "s3:DeleteObject",
               "s3:DeleteObjectVersion",
               "s3:GetBucketLocation",
               "s3:GetObject",
               "s3:ListAllMyBuckets",
               "s3:ListBucket",
               "s3:ListBucketVersions",
               "s3:PutBucketAcl",
               "s3:PutBucketCORS",
               "s3:PutBucketNotification",
               "s3:PutBucketPolicy",
               "s3:PutBucketWebsite",
               "s3:PutEncryptionConfiguration",
               "s3:PutObject",
               "s3:PutObjectAcl"
           ],
           "Resource": "*"
      },
      {
         "Sid": "AmplifySSRCalls",
         "Effect": "Allow",
         "Action": [
             "cloudfront:CreateCloudFrontOriginAccessIdentity",
             "cloudfront:CreateDistribution",
             "cloudfront:CreateInvalidation",
             "cloudfront:GetDistribution",
             "cloudfront:GetDistributionConfig",
             "cloudfront:ListCloudFrontOriginAccessIdentities",
             "cloudfront:ListDistributions",
             "cloudfront:ListDistributionsByLambdaFunction",
             "cloudfront:ListDistributionsByWebACLId",
             "cloudfront:ListFieldLevelEncryptionConfigs",
             "cloudfront:ListFieldLevelEncryptionProfiles",
             "cloudfront:ListInvalidations",
             "cloudfront:ListPublicKeys",
             "cloudfront:ListStreamingDistributions",
             "cloudfront:UpdateDistribution",
             "cloudfront:TagResource",
             "cloudfront:UntagResource",
             "cloudfront:ListTagsForResource",
             "iam:AttachRolePolicy",
             "iam:CreateRole",
             "iam:CreateServiceLinkedRole",
             "iam:GetRole",
             "iam:PutRolePolicy",
             "iam:PassRole",
             "lambda:CreateFunction",
             "lambda:EnableReplication",
             "lambda:DeleteFunction",
             "lambda:GetFunction",
             "lambda:GetFunctionConfiguration",
             "lambda:PublishVersion",
             "lambda:UpdateFunctionCode",
             "lambda:UpdateFunctionConfiguration",
             "lambda:ListTags",
             "lambda:TagResource",
             "lambda:UntagResource",
             "route53:ChangeResourceRecordSets",
             "route53:ListHostedZonesByName",
             "route53:ListResourceRecordSets",
             "s3:CreateBucket",
             "s3:GetAccelerateConfiguration",
             "s3:GetObject",
             "s3:ListBucket",
             "s3:PutAccelerateConfiguration",
             "s3:PutBucketPolicy",
             "s3:PutObject",
             "s3:PutBucketTagging",
             "s3:GetBucketTagging",
             "lambda:ListEventSourceMappings",
             "lambda:CreateEventSourceMapping",
             "iam:UpdateAssumeRolePolicy",
             "iam:DeleteRolePolicy",
             "sqs:CreateQueue",
             "sqs:DeleteQueue",
             "sqs:GetQueueAttributes",
             "sqs:SetQueueAttributes",
             "amplify:GetApp",
             "amplify:GetBranch",
             "amplify:UpdateApp",
             "amplify:UpdateBranch"
        ],
        "Resource": "*"
     }
  ]
}
```





## Amplify updates to AWS managed policies<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Amplify since this service began tracking these changes\. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document history for AWS Amplify](document-history.md) page\.




| Change | Description | Date | 
| --- | --- | --- | 
|  [AdministratorAccess\-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy  |  Add Amazon Lex actions to support the [Amplify Interactions category](https://docs.amplify.aws/lib/interactions/getting-started/q/platform/js/#interactions-with-aws)\. Add Amazon Rekognition actions to support the [Amplify Predictions category](https://docs.amplify.aws/lib/predictions/intro/q/platform/js/#configure-your-application)\. Add an Amazon Cognito action to support MFA configuration on Amazon Cognito user pools\. Add CloudFormation actions to support AWS CloudFormation StackSets\. Add Amazon Location Service actions to support the [Amplify Geo category](https://docs.amplify.aws/lib/geo/getting-started/q/platform/js/)\. Add a Lambda action to support Lambda layers in Amplify\. Add CloudWatch Logs actions to support CloudWatch Events\. Add Amazon S3 actions to support the [Amplify Storage category](https://docs.amplify.aws/lib/storage/getting-started/q/platform/js/)\. Add policy actions to support server\-side rendered \(SSR\) apps\.  | September 27, 2021 | 
|  [AdministratorAccess\-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy  |  Consolidate all Amplify actions into a single `amplify:*` action\. Add an Amazon S3 action to support encrypting customer Amazon S3 buckets\. Add IAM permission boundary actions to support Amplify apps that have permission boundaries enabled\. Add Amazon SNS actions to support viewing origination phone numbers, and viewing, creating, verifying, and deleting destination phone numbers\. Amplify Admin UI: Add Amazon Cognito, AWS Lambda, IAM, and AWS CloudFormation policy actions to enable managing backends in the Amplify console and Amplify Admin UI \. Add an AWS Systems Manager \(SSM\) policy statement to manage Amplify environment secrets\. Add an AWS CloudFormation `ListResources` action to support Lambda layers for Amplify apps\.  | July 28, 2021 | 
|  Amplify started tracking changes  |  Amplify started tracking changes for its AWS managed policies\.  | July 28, 2021 | 