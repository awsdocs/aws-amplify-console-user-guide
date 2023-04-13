# Deploying a Next\.js SSR app with Amplify<a name="deploy-nextjs-app"></a>

By default, Amplify deploys new SSR apps using Amplify Hosting's compute service with support for Next\.js 12 or later\. Amplify Hosting compute fully mangages the resources required to deploy an SSR app\. SSR apps in your Amplify account that you deployed before November 17, 2022 are using the Classic \(Next\.js 11 only\) SSR provider\. 

We strongly recommend that you migrate apps using Classic \(Next\.js 11 only\) SSR to the Amplify Hosting compute SSR provider\. Amplify doesn't perform automatic migrations for you\. You must manually migrate your app and then initiate a new build to complete the update\. For instructions, see [Migrating a Next\.js 11 SSR app to Amplify Hosting compute](update-app-nextjs-version.md)\. 

Use the following instructions to deploy a new SSR app\.

**To deploy an SSR app to Amplify using the Amplify Hosting compute SSR provider**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. On the **All apps** page, choose **New app**, then **Host web app**\.

1. Select your GitHub, Bitbucket, GitLab, or AWS CodeCommit repository provider and then choose **Continue**\.

1. On the **Add repository branch** page, do the following:

   1. In the **Recently updated repositories** list, select the name of the repository to connect\.

   1. In the **Branch** list, select the name of the repository branch to connect\.

   1. Choose **Next**\.

1. The app requires an IAM service role that Amplify assumes when calling other services on your behalf\. You can either allow Amplify Hosting compute to automatically create a service role for you or you can specify a role that you have created\.
   + To allow Amplify to automatically create a role and attach it to your app

     1. In the **IAM Role** section, choose **Create and use a new service role**\.
   + To attach a service role that you previously created

     1. In the **IAM Role** section, choose **Use an existing service role**\.

     1. Choose the role to use from the list\.

1. Choose **Next**\.

1. On the **Review** page, choose **Save and deploy**\.

## Package\.json file settings<a name="package.json-settings"></a>

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

## Amplify build settings<a name="build-setting-detection"></a>

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

If Amplify detects that you are deploying an SSG app, it generates a buildspec for the app and sets `baseDirectory` to `out`\. If you are deploying an app where an `amplify.yml` file is present, you must manually set the `baseDirectory` to `out` in the file\.

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
