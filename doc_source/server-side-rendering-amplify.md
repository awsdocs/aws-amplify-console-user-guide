# Deploy and host server\-side rendered apps with Amplify<a name="server-side-rendering-amplify"></a>

You can use AWS Amplify to deploy and host web apps that use server\-side rendering \(SSR\)\. Currently, Amplify supports SSR apps created using the Next\.js framework\. When you deploy your app, Amplify automatically detects SSR–you do not have to perform any manual configuration in the AWS Management Console\.

To learn about how Amplify supports SSR, review the following topics\.

**Topics**
+ [What is server\-side rendering](#What-is-server-side-rendering)
+ [Amplify support for Next\.js SSR](#ssr-Amplify-support)
+ [Deploying a Next\.js SSR app with Amplify](#deploy-nextjs-app)
+ [Adding SSR functionality to a static Next\.js app](#redeploy-ssg-to-ssr)
+ [Updating the Next\.js version for an existing app](#update-app-nextjs-version)
+ [Troubleshooting SSR deployment issues](#troubleshooting-ssr-deployment)

## What is server\-side rendering<a name="What-is-server-side-rendering"></a>

Previously, Amplify supported the deployment and hosting of static web apps only\. These include apps created with single\-page application \(SPA\) frameworks such as React, and apps created with a static site generator \(SSG\) such as Gatsby\. Static web apps consist of a combination of files, such as HTML, CSS, and JavaScript files, that are stored on a content delivery network \(CDN\)\. When a client browser makes a request to the website, the server returns a page to the client with an HTTP response and the client browser interprets the content and displays it to the user\.

Amplify now supports web apps with server\-side rendering \(SSR\)\. When a client sends a request to an SSR page, the HTML for the page is created on the server on each request\. SSR enables a developer to customize a website per request and per user\. In addition, SSR can improve performance and search engine optimization \(SEO\) for a website\.

## Amplify support for Next\.js SSR<a name="ssr-Amplify-support"></a>

Currently Amplify supports deployment and hosting for server\-side rendered \(SSR\) web apps created using Next\.js only\. Next\.js is a React framework for developing SPAs with JavaScript\. You can deploy apps built with Next.js 11 with features such as image and script optimization. Incremental static regeneration is currently not fully supported.

Developers can use Next\.js to combine static site generation \(SSG\) and SSR in a single project\. SSG pages are prerendered at build time, and SSR pages are prerendered at request time\. 

Prerendering can improve performance and search engine optimization\. Because Next\.js prerenders all pages on the server, the HTML content of each page is ready when it reaches the client's browser\. This content can also load faster\. Faster load times improve the end user's experience with a website and positively impact the site's SEO ranking\. Prerendering also improves SEO by enabling search engine bots to find and crawl a website's HTML content easily\.

Next\.js provides built\-in analytics support for measuring various performance metrics, such as Time to first byte \(TTFB\) and First contentful paint \(FCP\)\. For more information about Next\.js, see [Getting started](https://nextjs.org/docs/getting-started) on the Next\.js website\.

### Pricing for Next\.js SSR apps<a name="nextjs-ssr-pricing"></a>

When deploying your Next\.js SSR app, Amplify creates additional backend resources in your AWS account, including:
+ An Amazon Simple Storage Service \(Amazon S3\) bucket that stores the resources for your app's static assets\. For information about Amazon S3 charges, see [Amazon S3 Pricing](http://aws.amazon.com/s3/pricing/)\.
+ An Amazon CloudFront distribution to serve the app\. For information about CloudFront charges, see [Amazon CloudFront Pricing](http://aws.amazon.com/cloudfront/pricing/)\.
+ A [Lambda@Edge function](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) to customize the content that CloudFront delivers\.

When you use the Amplify Framework \(Libraries, CLI, UI components\), you pay only for the underlying AWS services you use\. For more information about Amplify deployment and hosting charges, see [AWS Amplify Pricing](http://aws.amazon.com/amplify/pricing/)\. 

## Deploying a Next\.js SSR app with Amplify<a name="deploy-nextjs-app"></a>

To deploy a Next\.js SSR app with Amplify Console, follow the same workflow for setting up a static app with continuous deployments\. For detailed instructions, see [Getting started with existing code](getting-started.md)\. Note that you can't set up an SSR app in Amplify with [manual deploys](manual-deploys.md)\.

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

You can add SSR functionality to an existing static \(SSG\) Next\.js app deployed with Amplify Console\. This requires three steps\. First, add a service role to the app\. Next, update the output directory in the app's build settings\. Lastly, update the app's `package.json` file to indicate that the app uses SSR\.

### Add a service role<a name="add-service-role"></a>

A service role is the AWS Identity and Access Management \(IAM\) role that Amplify Console assumes when calling other services on your behalf\. Follow these steps to add a service role to an SSG app that's already deployed with Amplify Console\.

**To add a service role**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. If you haven't already created a service role in your Amplify account, see [create a service role](how-to-service-role-amplify-console.md) to complete this prerequisite step\.

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
   + Enter **latest**, to always upgrade to the latest Next\.js version that Amplify supports\.

1. Choose **Save**\. The next time the app builds, it can use the features supported by the Next\.js version you specified in step 6\.

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
+ [Access control isn't available for your app](#access-control-unsupported)
+ [Your Next\.js app uses unsupported features](#nextjs-version-support)
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

If you try to deploy a Next\.js SSR app to Amplify and get a `RequestEntityTooLargeException` error, your app is too large to deploy\. You can attempt to work around this issue by adding cache cleanup code to your `next.config.js` file\.

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

### Access control isn't available for your app<a name="access-control-unsupported"></a>

Currently, Amplify doesn't support access control for Next\.js apps that use SSR\. If you are working with an SSR app in the Amplify console, **Access control** isn't available in the **App settings** menu in the navigation pane\.

### Your Next\.js app uses unsupported features<a name="nextjs-version-support"></a>

Amplify currently supports all features of Next\.js version 10\.*x*\.*x*, including Incremental Static Regeneration \(ISR\), Optional Catch All Routes, and Image Optimization\. In addition, Amplify supports Next\.js version 11\. For a list and description of these new features, see [Next\.js 11](https://nextjs.org/blog/next-11) on the Nextjs\.org website\.

When you deploy a new Next\.js app, Amplify uses the most recent supported version of Next\.js by default\. If you have an existing Next\.js app that you deployed to Amplify with an older version of Next\.js, you can edit the app's build settings to use a newer version\. For instructions, see [Updating the Next\.js version for an existing app](#update-app-nextjs-version)\.



### Unsupported Regions<a name="amplify-region-support"></a>

Amplify doesn't support Next\.js SSR app deployment in every AWS region where Amplify Console is available\. Currently, Next\.js SSR isn't supported in the following Regions: Europe \(Milan\) eu\-south\-1, Middle East \(Bahrain\) me\-south\-1, and Asia Pacific \(Hong Kong\) ap\-east\-1\.
