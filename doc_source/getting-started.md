# Getting started with existing code<a name="getting-started"></a>

In this walkthrough, you learn how to continuously build, deploy, and host a modern web app\. Modern web apps include single\-page application \(SPA\) frameworks \(for example, React, Angular, or Vue\) and static\-site generators \(SSGs\) \(for example, Hugo, Jekyll, or Gatsby\)\. Amplify Hosting also supports web apps that use server\-side rendering \(SSR\) and are created using Next\.js\.

To get started, sign in to the [Amplify console](https://console.aws.amazon.com/amplify/home)\. If you are starting from the **AWS Amplify** home page, choose **Get Started** at the top of the page\.

![\[The AWS Amplify home page with the Get Started button circled in red.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/Get_Started_1.png)

Then choose **Get started** under **Deliver**\.

![\[The Deliver section at the bottom of the AWS Amplify home page with Get started circled in red.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/Get_Started_2.png)

If you are starting from the **All apps** page, choose **New app**, then **Host web app** in the upper right corner\.

![\[Screenshot of the All apps page in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/Get_Started_3.png)

## Step 1: Connect a repository<a name="step-1-connect-repository"></a>

Connect your GitHub, Bitbucket, GitLab, or AWS CodeCommit repository\. You also have the option of manually uploading your build artifacts without connecting a Git repository\. For more information, see [Manual Deploys](manual-deploys.md)\.

![\[Screenshot of the Get started with Amplify Hosting page in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-gettingstarted-2.png)

After you authorize the Amplify console with Bitbucket, GitLab, or AWS CodeCommit, Amplify fetches an access token from the repository provider, but it *doesn’t store the token* on the AWS servers\. Amplify accesses your repository using deploy keys installed in a specific repository only\.

For GitHub repositories, Amplify now uses the GitHub Apps feature to authorize Amplify access\. With the Amplify GitHub App, permissions are more fine\-tuned, enabling you to grant Amplify access to only the repositories that you specify\. For more information about installing and authorizing the GitHub App, see [Setting up Amplify access to GitHub repositories](setting-up-GitHub-access.md)\.

After you connect the repository service provider, choose a repository, and then choose a corresponding branch to build and deploy\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-gettingstarted-3.png)

## Step 2a: Confirm build settings for the front end<a name="step-2a-confirm-build-settings-for-the-front-end"></a>

For the selected branch, Amplify inspects your repository to automatically detect the sequence of build commands to run\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-gettingstarted-4.png)

 **Important:** Verify that the build commands and build output directory \(that is, artifacts > baseDirectory\) is accurate\. If you need to modify this information, choose **Edit** to open the YML editor\. You can save your build settings on our servers, or you can download the YML and add it to the root of your repo \(for monorepos, store the YML at the app’s root directory\)\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-gettingstarted-5.png)

For more information, see [Build specification YAML syntax](build-settings.md#yml-specification-syntax)\.

## Step 2b: Confirm build settings for the backend<a name="step-2b-confirm-build-settings-for-the-backend"></a>

If you connected a repository provisioned by the Amplify CLI v1\.0\+ \(run *amplify \-v* to find CLI version\), Amplify Hosting will deploy or automatically update backend resources \(any resource provisioned by the Amplify CLI\) in a single workflow with the frontend build\. You can choose to point an existing backend environment to your branch, or create a completely new environment\. For a step\-by\-step tutorial, see [Getting started with fullstack deployments](deploy-backend.md)\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/reuse-backend.png)

To deploy backend functionality using the Amplify CLI during your build, create or reuse an AWS Identity and Access Management \(IAM\) service role\. IAM roles are a secure way to grant Amplify permissions to act on resources in your account\. For detailed instructions, see [Adding a service role](how-to-service-role-amplify-console.md)\.

 **Note:** The Amplify CLI won’t run without an IAM service role enabled\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-gettingstarted-7.png)

## Step 2c: Add environment variables \(optional\)<a name="step-2c-add-environment-variables-optional"></a>

Almost every app needs to get configuration information at runtime\. These configurations can be database connection details, API keys, or different parameters\. [Environment variables](environment-variables.md) provide a means to expose these configurations at build time\.

## Step 3: Save and deploy<a name="step-3-save-and-deploy"></a>

Review all of your settings to ensure everything is set up correctly\. Choose **Save and deploy** to deploy your web app to the AWS global content delivery network \(CDN\)\. Your front end build typically takes 1 to 2 minutes but can vary based on the size of the app\.

Access the build logs screen by choosing a progress indicator in the branch section\. A build has the following stages:

1.  **Provision** \- Your build environment is set up using a Docker image on a host with 4 vCPU, 7GB memory\. Each build gets its own host instance, ensuring that all resources are securely isolated\. The contents of the Docker file are displayed to ensure that the default image supports your requirements\.

1.  **Build** \- The build phase consists of three stages: setup \(clones repository into container\), deploy backend \(runs the Amplify CLI to deploy backend resources\), and build front end \(builds your front\-end artifacts\)\.

1.  **Deploy** \- When the build is complete, all artifacts are deployed to a hosting environment managed by Amplify Hosting\. Every deployment is atomic \- atomic deployments eliminate maintenance windows by ensuring that the web app is only updated after the entire deployment has completed\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-backend-frontend-alternate.png)

## Next steps<a name="next-steps"></a>
+  [Add a custom domain to your app](custom-domains.md) 
+  [Manage multiple environments](multi-environments.md) 
+  [Preview pull requests before merging](pr-previews.md) 