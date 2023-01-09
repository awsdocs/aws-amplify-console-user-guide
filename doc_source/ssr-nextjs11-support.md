# Amplify Next\.js 11 SSR support<a name="ssr-nextjs11-support"></a>

If you deployed a Next\.js app to Amplify prior to the release of Amplify Hosting compute on November 17, 2022, your app is using Amplify's previous SSR provider, Classic \(Next\.js 11 only\)\. The documentation in this section applies only to apps deployed using the Classic \(Next\.js 11 only\) SSR provider\.

**Note**  
We strongly recommend that you migrate your Next\.js 11 apps to the Amplify Hosting compute managed SSR provider\. For more information, see [Migrating a Next\.js 11 SSR app to Amplify Hosting compute](update-app-nextjs-version.md)\.

The following list describes the specific features that the Amplify Classic \(Next\.js 11 only\) SSR provider supports\.

**Supported features**
+ Server\-side rendered pages \(SSR\)
+ Static pages
+ API routes
+ Dynamic routes
+ Catch all routes
+ SSG \(Static generation\)
+ Incremental Static Regeneration \(ISR\)
+ Internationalized \(i18n\) sub\-path routing
+ Environment variables

**Unsupported features**
+ Image optimization
+ On\-Demand Incremental Static Regeneration \(ISR\)
+ Internationalized \(i18n\) domain routing
+ Internationalized \(i18n\) automatic locale detection
+ Middleware
+ Edge API routes

## Pricing for Next\.js 11 SSR apps<a name="Nextjs11-ssr-pricing"></a>

When deploying your Next\.js 11 SSR app, Amplify creates additional backend resources in your AWS account, including:
+ An Amazon Simple Storage Service \(Amazon S3\) bucket that stores the resources for your app's static assets\. For information about Amazon S3 charges, see [Amazon S3 Pricing](http://aws.amazon.com/s3/pricing/)\.
+ An Amazon CloudFront distribution to serve the app\. For information about CloudFront charges, see [Amazon CloudFront Pricing](http://aws.amazon.com/cloudfront/pricing/)\.
+ Four [Lambda@Edge functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) to customize the content that CloudFront delivers\.

## AWS Identity and Access Management permissions for Next\.js 11 SSR apps<a name="ssr-IAM-permissions"></a>

Amplify requires AWS Identity and Access Management \(IAM\) permissions to deploy an SSR app\. Without the required minimum permissions, you will get an error when you try to deploy your SSR app\. To provide Amplify with the required permissions, you must specify a service role\.

To create an IAM service role that Amplify assumes when calling other services on your behalf, see [Adding a service role](how-to-service-role-amplify-console.md)\. These instructions demonstrate how to create a role that attaches the `AdministratorAccess-Amplify` managed policy\.

The `AdministratorAccess-Amplify` managed policy provides access to multiple AWS services, including IAM actions\. and should be considered as powerful as the `AdministratorAccess` policy\. This policy provides more permissions than required to deploy your SSR app\.

It is recommended that you follow the best practice of granting least privilege and reduce the permissions granted to the service role\. Instead of granting administrator access permissions to your service role, you can create your own customer managed IAM policy that grants only the permissions required to deploy your SSR app\. See, [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide* for instructions on creating a customer managed policy\.

If you create your own policy, refer to the following list of the minimum permissions required to deploy an SSR app\.

```
acm:DescribeCertificate
acm:ListCertificates
acm:RequestCertificate
cloudfront:CreateCloudFrontOriginAccessIdentity
cloudfront:CreateDistribution
cloudfront:CreateInvalidation
cloudfront:GetDistribution
cloudfront:GetDistributionConfig
cloudfront:ListCloudFrontOriginAccessIdentities
cloudfront:ListDistributions
cloudfront:ListDistributionsByLambdaFunction
cloudfront:ListDistributionsByWebACLId
cloudfront:ListFieldLevelEncryptionConfigs
cloudfront:ListFieldLevelEncryptionProfiles
cloudfront:ListInvalidations
cloudfront:ListPublicKeys
cloudfront:ListStreamingDistributions
cloudfront:UpdateDistribution
cloudfront:TagResource
cloudfront:UntagResource
cloudfront:ListTagsForResource
cloudfront:DeleteDistribution
iam:AttachRolePolicy
iam:CreateRole
iam:CreateServiceLinkedRole
iam:GetRole
iam:PutRolePolicy
iam:PassRole
iam:UpdateAssumeRolePolicy
iam:DeleteRolePolicy
lambda:CreateFunction
lambda:EnableReplication
lambda:DeleteFunction
lambda:GetFunction
lambda:GetFunctionConfiguration
lambda:PublishVersion
lambda:UpdateFunctionCode
lambda:UpdateFunctionConfiguration
lambda:ListTags
lambda:TagResource
lambda:UntagResource
lambda:ListEventSourceMappings
lambda:CreateEventSourceMapping
route53:ChangeResourceRecordSets
route53:ListHostedZonesByName
route53:ListResourceRecordSets
s3:CreateBucket
s3:GetAccelerateConfiguration
s3:GetObject
s3:ListBucket
s3:PutAccelerateConfiguration
s3:PutBucketPolicy
s3:PutObject
s3:PutBucketTagging
s3:GetBucketTagging
sqs:CreateQueue
sqs:DeleteQueue
sqs:GetQueueAttributes
sqs:SetQueueAttributes
amplify:GetApp
amplify:GetBranch
amplify:UpdateApp
amplify:UpdateBranch
```

## Troubleshooting Next\.js 11 SSR deployments<a name="troubleshooting-Nextjs11-ssr-deployment"></a>

If you experience unexpected issues when deploying a Classic \(Next\.js 11 only\) SSR app with Amplify, review the following troubleshooting topics\.

**Topics**
+ [Your output directory is overridden](#output-directory-overridden)
+ [You get a 404 error after deploying your SSR site](#404-error)
+ [Your app is missing the rewrite rule for CloudFront SSR distributions](#cloudfront-rewrite-rule-missing)
+ [Your app is too large to deploy](#app-too-large-to-deploy)
+ [Your build fails with an out of memory error](#out-of-memory)
+ [Your app has both SSR and SSG branches](#ssr-and-ssg-branches)
+ [Your app stores static files in a folder with a reserved path](#amplify-reserved-path)
+ [Your app has reached a CloudFront limit](#cloudfront-distribution-limit)
+ [Environment variables are not carried through to Lambda functions](#ssr-environment-variable-support)
+ [Lambda@Edge functions are created in the US East \(N\. Virginia\) Region](#nextjs-version-lambda-edge-functions)
+ [Your Next\.js app uses unsupported features](#nextjs-version-support)
+ [Images in your Next\.js app aren't loading](#image-size-limit)
+ [Unsupported Regions](#amplify-region-support)

### Your output directory is overridden<a name="output-directory-overridden"></a>

The output directory for a Next\.js app deployed with Amplify must be set to `.next`\. If your app's output directory is being overridden, check the `next.config.js` file\. To have the build output directory default to `.next`, remove the following line from the file:

```
distDir: 'build'
```

Verify that the output directory is set to `.next` in your build settings\. For information about viewing your app's build settings, see [Configuring build settings](build-settings.md)\. 

The following is an example of the build settings for an app where `baseDirectory` is set to `.next`\.

```
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
```

### You get a 404 error after deploying your SSR site<a name="404-error"></a>

If you get a 404 error after deploying your site, the issue could be caused by your output directory being overridden\. To check your `next.config.js` file and verify the correct build output directory in your app's build spec, follow the steps in the previous topic, [Your output directory is overridden](#output-directory-overridden)\.

### Your app is missing the rewrite rule for CloudFront SSR distributions<a name="cloudfront-rewrite-rule-missing"></a>

When you deploy an SSR app, Amplify creates a rewrite rule for your CloudFront SSR distributions\. If you can't access your app in a web browser, verify that the CloudFront rewrite rule exists in your AWS account\. If it's missing, you can either add it manually or redeploy your app\.

To view or edit an app's rewrite and redirect rules in the Amplify console, in the navigation pane, choose **App settings**, then **Rewrites and redirects**\. The following screenshot shows an example of the rewrite rules that Amplify creates for you when you deploy an SSR app\.

![\[The rewrites and redirects pane in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-ssr-troubleshooting1.png)

### Your app is too large to deploy<a name="app-too-large-to-deploy"></a>

Amplify limits the size of an SSR deployment to 50 MB\. If you try to deploy a Next\.js SSR app to Amplify and get a `RequestEntityTooLargeException` error, your app is too large to deploy\. You can attempt to work around this issue by adding cache cleanup code to your `next.config.js` file\.

The following is an example of code in the `next.config.js` file that performs cache cleanup\.

```
module.exports = {
    webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
        config.optimization.splitChunks.cacheGroups = { }
        config.optimization.minimize = true;
        return config
      },
}
```

### Your build fails with an out of memory error<a name="out-of-memory"></a>

Next\.js enables you to cache build artifacts to improve performance on subsequent builds\. In addition, Amplify's AWS CodeBuild container compresses and uploads this cache to Amazon S3, on your behalf, to improve subsequent build performance\. This could cause your build to fail with an out of memory error\.

Perform the following actions to prevent your app from exceeding the memory limit during the build phase\. First, remove `.next/cache/**/*` from the cache\.paths section of your build settings\. Next, remove the `NODE_OPTIONS` environment variable from your build settings file\. Instead, set the `NODE_OPTIONS` environment variable in the Amplify console to define the Node maximum memory limit\. For more information about setting environment variables using the Amplify console, see [Set environment variables](environment-variables.md#setting-env-vars)\.

After making these changes, try your build again\. If it succeeds, add `.next/cache/**/*` back to the cache\.paths section of your build settings file\.

For more information about Next\.js cache configuration to improve build performance, see [AWS CodeBuild](https://nextjs.org/docs/advanced-features/ci-build-caching#aws-codebuild) on the Next\.js website\.

### Your app has both SSR and SSG branches<a name="ssr-and-ssg-branches"></a>

You can't deploy an app that has both SSR and SSG branches\. If you need to deploy both SSR and SSG branches, you must deploy one app that uses only SSR branches and another app that uses only SSG branches\.

### Your app stores static files in a folder with a reserved path<a name="amplify-reserved-path"></a>

Next\.js can serve static files from a folder named `public` that's stored in the project's root directory\. When you deploy and host a Next\.js app with Amplify, your project can't include folders with the path `public/static`\. Amplify reserves the `public/static` path for use when distributing the app\. If your app includes this path, you must rename the `static` folder before deploying with Amplify\.

### Your app has reached a CloudFront limit<a name="cloudfront-distribution-limit"></a>

[CloudFront service quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) limit your AWS account to 25 distributions with attached Lambda@Edge functions\. If you exceed this quota, you can either delete any unused CloudFront distributions from your account or request a quota increase\. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*\. 

### Environment variables are not carried through to Lambda functions<a name="ssr-environment-variable-support"></a>

Environment variables that you specify in the Amplify console for an SSR app are not carried through to the app's AWS Lambda functions\. See, [Making environment variables accessible to server\-side runtimes](ssr-environment-variables.md), for detailed instructions on how to add environment variables that you can reference from your Lambda functions\.

### Lambda@Edge functions are created in the US East \(N\. Virginia\) Region<a name="nextjs-version-lambda-edge-functions"></a>

When you deploy a Next\.js app, Amplify creates Lambda@Edge functions to customize the content that CloudFront delivers\. Lambda@Edge functions are created in the US East \(N\. Virginia\) Region, not the Region where your app is deployed\. This is a Lambda@Edge restriction\. For more information about Lambda@Edge functions, see [Restrictions on edge functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-restrictions.html) in the *Amazon CloudFront Developer Guide\.* 

### Your Next\.js app uses unsupported features<a name="nextjs-version-support"></a>

Apps deployed with Amplify support the Next\.js major versions up through version 11\. For a detailed list of the Next\.js features that are supported and unsupported by Amplify, see [supported features](#supportedfeatures)\.

When you deploy a new Next\.js app, Amplify uses the most recent supported version of Next\.js by default\. If you have an existing Next\.js app that you deployed to Amplify with an older version of Next\.js, you can migrate the app to the Amplify Hosting compute SSR provider\. For instructions, see [Migrating a Next\.js 11 SSR app to Amplify Hosting compute](update-app-nextjs-version.md)\.



### Images in your Next\.js app aren't loading<a name="image-size-limit"></a>

When you add images to your Next\.js app using the `next/image` component, the size of the image can't exceed 1 MB\. When you deploy the app to Amplify, images that are larger than 1 MB will return a 503 error\. This is caused by a Lambda@Edge limit that restricts the size of a response that is generated by a Lambda function, including headers and body, to 1 MB\.

The 1 MB limit applies to other artifacts in your app, such as PDF and document files\.

### Unsupported Regions<a name="amplify-region-support"></a>

Amplify doesn't support Classic \(Next\.js 11 only\) SSR app deployment in every AWS region where Amplify is available\. Classic \(Next\.js 11 only\) SSR isn't supported in the following Regions: Europe \(Milan\) eu\-south\-1, Middle East \(Bahrain\) me\-south\-1, and Asia Pacific \(Hong Kong\) ap\-east\-1\.