# Deploy and host server\-side rendered apps with Amplify<a name="server-side-rendering-amplify"></a>

You can use AWS Amplify to deploy and host web apps that use server\-side rendering \(SSR\)\. Currently, Amplify supports SSR apps created using the Next\.js framework\. When you deploy your app, Amplify automatically detects SSR–you do not have to perform any manual configuration in the AWS Management Console\.

To learn about how Amplify supports SSR, review the following topics\.

**Topics**
+ [What is server\-side rendering](#What-is-server-side-rendering)
+ [Amplify support for Next\.js SSR](#ssr-Amplify-support)
+ [Pricing for Next\.js SSR apps](#nextjs-ssr-pricing)
+ [Deploying a Next\.js SSR app with Amplify](#deploy-nextjs-app)
+ [Adding SSR functionality to a static Next\.js app](#redeploy-ssg-to-ssr)
+ [Updating the Next\.js version for an existing app](#update-app-nextjs-version)
+ [AWS Identity and Access Management permissions for SSR apps](#ssr-IAM-permissions)
+ [Troubleshooting SSR deployment issues](#troubleshooting-ssr-deployment)

## What is server\-side rendering<a name="What-is-server-side-rendering"></a>

Previously, Amplify supported the deployment and hosting of static web apps only\. These include apps created with single\-page application \(SPA\) frameworks such as React, and apps created with a static site generator \(SSG\) such as Gatsby\. Static web apps consist of a combination of files, such as HTML, CSS, and JavaScript files, that are stored on a content delivery network \(CDN\)\. When a client browser makes a request to the website, the server returns a page to the client with an HTTP response and the client browser interprets the content and displays it to the user\.

Amplify now supports web apps with server\-side rendering \(SSR\)\. When a client sends a request to an SSR page, the HTML for the page is created on the server on each request\. SSR enables a developer to customize a website per request and per user\. In addition, SSR can improve performance and search engine optimization \(SEO\) for a website\.

## Amplify support for Next\.js SSR<a name="ssr-Amplify-support"></a>

Currently Amplify supports deployment and hosting for server\-side rendered \(SSR\) web apps created using Next\.js only\. Next\.js is a React framework for developing SPAs with JavaScript\. You can deploy apps built with Next\.js 11 with features such as image and script optimization, and Incremental Static Regeneration \(ISR\)\.

Developers can use Next\.js to combine static site generation \(SSG\), and SSR in a single project\. SSG pages are prerendered at build time, and SSR pages are prerendered at request time\. 

Prerendering can improve performance and search engine optimization\. Because Next\.js prerenders all pages on the server, the HTML content of each page is ready when it reaches the client's browser\. This content can also load faster\. Faster load times improve the end user's experience with a website and positively impact the site's SEO ranking\. Prerendering also improves SEO by enabling search engine bots to find and crawl a website's HTML content easily\.

Next\.js provides built\-in analytics support for measuring various performance metrics, such as Time to first byte \(TTFB\) and First contentful paint \(FCP\)\. For more information about Next\.js, see [Getting started](https://nextjs.org/docs/getting-started) on the Next\.js website\.

### Supported and unsupported Next\.js features<a name="supported-unsupported-features"></a>

Amplify supports apps built with the Next\.js major versions 9, 10, and 11\. The following list describes the specific features that Amplify supports and does not support\.

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
+ Image optimization\. The size of the image can't exceed 1 MB\. The AVIF and WebP image formats are not supported\.

**Unsupported features**
+ Internationalized \(i18n\) domain routing
+ Internationalized \(i18n\) automatic locale detection
+ Middleware

## Pricing for Next\.js SSR apps<a name="nextjs-ssr-pricing"></a>

When deploying your Next\.js SSR app, Amplify creates additional backend resources in your AWS account, including:
+ An Amazon Simple Storage Service \(Amazon S3\) bucket that stores the resources for your app's static assets\. For information about Amazon S3 charges, see [Amazon S3 Pricing](http://aws.amazon.com/s3/pricing/)\.
+ An Amazon CloudFront distribution to serve the app\. For information about CloudFront charges, see [Amazon CloudFront Pricing](http://aws.amazon.com/cloudfront/pricing/)\.
+ Four [Lambda@Edge functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) to customize the content that CloudFront delivers\.

When you use the Amplify Framework \(Libraries, CLI, UI components\), you pay only for the underlying AWS services you use\. For more information about Amplify deployment and hosting charges, see [AWS Amplify Pricing](http://aws.amazon.com/amplify/pricing/)\. 

## Deploying a Next\.js SSR app with Amplify<a name="deploy-nextjs-app"></a>

To deploy a Next\.js SSR app with Amplify, follow the same workflow for setting up a static app with continuous deployments\. For detailed instructions, see [Getting started with existing code](getting-started.md)\. Note that you can't set up an SSR app in Amplify with [manual deploys](manual-deploys.md)\.

### Package\.json file settings<a name="package.json-settings"></a>

When you deploy a Next\.js app, Amplify inspects the app's build script in the `package.json` file to detect whether the app is SSR or SSG\.

The following is an example of the build script for a Next\.js SSR app\. The build script `"next build"` indicates that the app supports both SSG and SSR pages\.

```
"scripts": {
  "dev": "next dev",
  "build": "next build",
  "start": "next start"
},
```

The following is an example of the build script for a Next\.js SSG app\. The build script `"next build && next export"` indicates that the app supports only SSG pages\.

```
"scripts": {
  "dev": "next dev",
  "build": "next build && next export",
  "start": "next start"
},
```

### Amplify build settings<a name="build-setting-detection"></a>

After inspecting your app's `package.json` file to determine whether you are deploying an SSG or SSR app, Amplify checks the build settings for the app\. You can save build settings in the Amplify console or in an `amplify.yml` file in the root of your repository\. For more information, see [Configuring build settings](build-settings.md)\.

If Amplify detects that you are deploying a Next\.js SSR app, and no `amplify.yml` file is present, it generates a buildspec for the app and sets `baseDirectory` to `.next`\. If you are deploying an app where an `amplify.yml` file is present, the build settings in the file override any build settings in the console\. Therefore, you must manually set the `baseDirectory` to `.next` in the file\.

The following is an example of the build settings for an app where `baseDirectory` is set to `.next`\. This indicates that the build artifacts are for a Next\.js app that supports SSG and SSR pages\.

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

If Amplify detects that you are deploying an SSG app, it generates a buildspec for the app and sets `baseDirectory` to out\. If you are deploying an app where an `amplify.yml` file is present, you must manually set the `baseDirectory` to `out` in the file\.

The following is an example of the build settings for an app where `baseDirectory` is set to `out`\. This indicates that the build artifacts are for a Next\.js app that supports only SSG pages\.

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
    baseDirectory: out
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
```

## Adding SSR functionality to a static Next\.js app<a name="redeploy-ssg-to-ssr"></a>

You can add SSR functionality to an existing static \(SSG\) Next\.js app deployed with Amplify\. This requires three steps\. First, add a service role to the app\. Next, update the output directory in the app's build settings\. Lastly, update the app's `package.json` file to indicate that the app uses SSR\.

### Add a service role<a name="add-service-role"></a>

A service role is the AWS Identity and Access Management \(IAM\) role that Amplify assumes when calling other services on your behalf\. Follow these steps to add a service role to an SSG app that's already deployed with Amplify\.

**To add a service role**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. If you haven't already created a service role in your Amplify account, see [create a service role](how-to-service-role-amplify-console.md) to complete this prerequisite step\. See [AWS Identity and Access Management permissions for SSR apps](#ssr-IAM-permissions) for information about the permissions required to deploy an SSR app\.

1. Choose the static Next\.js app that you want to add a service role to\.

1. In the navigation pane, choose **App settings**, **General**\.

1. On the **App details** page, choose **Edit**

1. For **Service role**, choose the name of an existing service role or the name of the service role that you created in step 2\.

1. Choose **Save**\.

### Update build settings<a name="update-build-settings"></a>

Before you redeploy your app with SSR functionality, you must update the build settings for the app to set the output directory to `.next`\. You can edit the build settings in the Amplify console or in an `amplify.yml` file stored in your repo\. For more information see, [Configuring build settings](build-settings.md)\.

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

### Update the package\.json file<a name="update-package.json-file"></a>

After you add a service role and update the build settings, update the app's `package.json` file\. As in the following example, set the build script to `"next build"` to indicate that the Next\.js app supports both SSG and SSR pages\.

```
"scripts": {
  "dev": "next dev",
  "build": "next build",
  "start": "next start"
},
```

Amplify detects the change to the `package.json` file in your repo and redeploys the app with SSR functionality\.

## Updating the Next\.js version for an existing app<a name="update-app-nextjs-version"></a>

When you deploy a new Next\.js app with Amplify, by default Amplify uses the most recent supported version of Next\.js\. Currently, Amplify supports Next\.js version 11\.

For an existing app, use the following instructions to change the version of Next\.js that Amplify uses to build the app\.

**To update the Next\.js version for an existing app**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the Next\.js app that you want to update\.

1. In the navigation pane, choose **App settings**, **Build settings**\.

1. On the **Build settings** page, in the **Build image settings** section, choose **Edit**\.

1. In the **Edit build image settings** dialog box, expand the **Add package version override** list, and choose **Next\.js version**\.

1. For **Version**, do one of the following:
   + Enter **9** for support up to Next\.js version 9\.4\.*x*\.
   + Enter **10** for support for Next\.js versions 9\.4\.*x* to 10\.*x*\.*x*\.
   + Enter **11** for support for Next\.js versions 11\.*x* to 11\.1\.3\.
   + Enter **latest**, to always upgrade to the latest Next\.js version that Amplify supports\.

1. Choose **Save**\. The next time the app builds, it can use the features supported by the Next\.js version you specified in step 6\.

## AWS Identity and Access Management permissions for SSR apps<a name="ssr-IAM-permissions"></a>

Amplify requires AWS Identity and Access Management \(IAM\) permissions to deploy an SSR app\. Without the required minimum permissions, you will get an error when you try to deploy your SSR app\. To provide Amplify with the required permissions, you must create an IAM service role that Amplify assumes when calling other services on your behalf\. See [create a service role](how-to-service-role-amplify-console.md) for detailed instructions on creating an `Amplify-Backend Deployment` service role that Amplify uses to create and manage AWS resources\. IAM attaches the `AdministratorAccess-Amplify` managed policy to the `Amplify-Backend Deployment` service role\.

The `AdministratorAccess-Amplify` managed policy provides access to multiple AWS services, including IAM actions\. and should be considered as powerful as the `AdministratorAccess` policy\. This policy provides more permissions than required to deploy your SSR app\. It is recommended that you follow the best practice of granting least privilege and reduce the permissions granted to the service role\.

Instead of granting administrator access permissions to your service role, you can create your own customer managed IAM policy that grants only the permissions required to deploy your SSR app\. See [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide* for instructions on creating a customer managed policy\. Add the following list of minimum permissions required to deploy an SSR app to the policy you create\.

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

To reduce the scope of permissions granted to an Amplify service role in your account, edit the role to remove the `AdministratorAccess-Amplify` policy and attach your new SSR\-specific policy\.

## Troubleshooting SSR deployment issues<a name="troubleshooting-ssr-deployment"></a>

If you experience unexpected issues when deploying an SSR app with Amplify, review the following troubleshooting topics\.

**Topics**
+ [Your output directory is overridden](#output-directory-overridden)
+ [You get a 404 error after deploying your SSR site](#404-error)
+ [Your app is missing the rewrite rule for CloudFront SSR distributions](#cloudfront-rewrite-rule-missing)
+ [Your app is too large to deploy](#app-too-large-to-deploy)
+ [Your app has both SSR and SSG branches](#ssr-and-ssg-branches)
+ [Your app stores static files in a folder with a reserved path](#amplify-reserved-path)
+ [Your app has reached a CloudFront limit](#cloudfront-distribution-limit)
+ [Environment variables are not carried through to Lambda functions](#ssr-environment-variable-support)
+ [Lambda@Edge functions are created in the US East \(N\. Virginia\) Region](#nextjs-version-lambda-edge-funchtions)
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

### Your app has both SSR and SSG branches<a name="ssr-and-ssg-branches"></a>

You can't deploy an app that has both SSR and SSG branches\. If you need to deploy both SSR and SSG branches, you must deploy one app that uses only SSR branches and another app that uses only SSG branches\.

### Your app stores static files in a folder with a reserved path<a name="amplify-reserved-path"></a>

Next\.js can serve static files from a folder named `public` that's stored in the project's root directory\. When you deploy and host a Next\.js app with Amplify, your project can't include folders with the path `public/static`\. Amplify reserves the `public/static` path for use when distributing the app\. If your app includes this path, you must rename the `static` folder before deploying with Amplify\.

### Your app has reached a CloudFront limit<a name="cloudfront-distribution-limit"></a>

[CloudFront service quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) limit your AWS account to 25 distributions with attached Lambda@Edge functions\. If you exceed this quota, you can either delete any unused CloudFront distributions from your account or request a quota increase\. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*\. 

### Environment variables are not carried through to Lambda functions<a name="ssr-environment-variable-support"></a>

Environment variables that you specify in the Amplify console for an SSR app are not carried through to the app's AWS Lambda functions\. Use the following instructions to add environment variables that you can reference from your Lambda functions\.

**To add environment variables to a Next\.js SSR app**

1. Follow the [Set environment variables](environment-variables.md#setting-env-vars) instructions to add environment variables to your app in the Amplify console\.

1. Open the `next.config.js` file for your app\. If this file doesn't exist, create it\.

1. Update the `next.config.js` file with the environment variables that you added in step 1\. For example, if you created an environment variable named `MY_ENV_VAR`, add the following code to your `next.config.js` file:

   ```
   module.exports = {
     env: {
       MY_ENV_VAR: process.env.MY_ENV_VAR
     }
   };
   ```

1. Rebuild your app\. You can now reference the environment variables you added, such as `process.env.MY_ENV_VAR`, in the app's Lambda functions\.

### Lambda@Edge functions are created in the US East \(N\. Virginia\) Region<a name="nextjs-version-lambda-edge-funchtions"></a>

When you deploy a Next\.js app, Amplify creates Lambda@Edge functions to customize the content that CloudFront delivers\. Lambda@Edge functions are created in the US East \(N\. Virginia\) Region, not the Region where your app is deployed\. This is a Lambda@Edge restriction\. For more information about Lambda@Edge functions, see [Restrictions on edge functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-restrictions.html) in the *Amazon CloudFront Developer Guide\.* 

### Your Next\.js app uses unsupported features<a name="nextjs-version-support"></a>

Amplify currently supports the Next\.js major versions 9, 10, including Optional Catch All Routes, Image Optimization, and Incremental Static Regeneration \(ISR\), and 11\. For a list and description of the new features in version 11, see [Next\.js 11](https://nextjs.org/blog/next-11) on the Nextjs\.org website\. For a detailed list of the Next\.js features that are supported and unsupported by Amplify, see [Supported and unsupported Next\.js features](#supported-unsupported-features)\.

When you deploy a new Next\.js app, Amplify uses the most recent supported version of Next\.js by default\. If you have an existing Next\.js app that you deployed to Amplify with an older version of Next\.js, you can edit the app's build settings to use a newer version\. For instructions, see [Updating the Next\.js version for an existing app](#update-app-nextjs-version)\.



### Images in your Next\.js app aren't loading<a name="image-size-limit"></a>

When you add images to your Next\.js app using the `next/image` component, the size of the image can't exceed 1 MB\. When you deploy the app to Amplify, images that are larger than 1 MB will return a 503 error\. This is caused by a Lambda@Edge limit that restricts the size of a response that is generated by a Lambda function, including headers and body, to 1 MB\.

The 1 MB limit applies to other artifacts in your app, such as PDF and document files\.

### Unsupported Regions<a name="amplify-region-support"></a>

Amplify doesn't support Next\.js SSR app deployment in every AWS region where Amplify is available\. Currently, Next\.js SSR isn't supported in the following Regions: Europe \(Milan\) eu\-south\-1, Middle East \(Bahrain\) me\-south\-1, and Asia Pacific \(Hong Kong\) ap\-east\-1\.