# Setting up Amplify access to GitHub repositories<a name="setting-up-GitHub-access"></a>

Amplify now uses the GitHub Apps feature to authorize Amplify read\-only access to GitHub repositories\. With the Amplify GitHub App, permissions are more fine\-tuned, enabling you to grant Amplify access to only the repositories that you specify\. To learn more about GitHub Apps, see [About GitHub Apps](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps#about-github-apps) on the GitHub website\.

When you connect a new app stored in a GitHub repo, by default Amplify uses the GitHub App to access the repo\. However, existing Amplify apps that you previously connected from GitHub repos use OAuth for access\. CI/CD will continue to work for these apps, but we highly recommend that you migrate them to use the new Amplify GitHub App\.

When you deploy a new app or migrate an existing app using the Amplify console, you are automatically directed to the installation location for the Amplify GitHub App\. To manually access the installation landing page for the app, open a web browser and navigate to the app by region\. Use the format `https://github.com/apps/aws-amplify-REGION`, replacing *REGION* with the region where you will deploy your Amplify app\. For example, to install the Amplify GitHub App in the US West \(Oregon\) region, navigate to https://github\.com/apps/aws\-amplify\-us\-west\-2\.

**Topics**
+ [Installing and authorizing the Amplify GitHub App for a new deployment](#setting-up-github-app)
+ [Migrating an existing OAuth app to the Amplify GitHub App](#migrating-to-github-app-auth)
+ [Setting up the Amplify GitHub App for AWS CloudFormation, CLI, and SDK deployments](#setting-up-github-app-cloudformation)
+ [Setting up web previews with the Amplify GitHub App](#setting-up-github-app-pr-previews)

## Installing and authorizing the Amplify GitHub App for a new deployment<a name="setting-up-github-app"></a>

When you deploy a new app to Amplify from existing code in a GitHub repo, use the following instructions to install and authorize the GitHub App\.

**To install and authorize the Amplify GitHub App**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. From the **All apps** page, choose **New app**, then **Host web app**\.

1. On the **Get started with Amplify Hosting** page, choose **GitHub**, then choose **Continue**\.

1. If this is the first time connecting a GitHub repository, A new page opens in your browser on GitHub\.com, requesting permission to authorize AWS Amplify in your GitHub account\. Choose **Authorize**\.

1. Next, you must install the Amplify GitHub App in your GitHub account\. A page opens on Github\.com requesting permission to install and authorize AWS Amplify in your GitHub account\.

1. Select the GitHub account where you want to install the Amplify GitHub App\.

1. Do one of the following:
   + To apply the installation to all repositories, choose **All repositories**\.
   + To limit the installation to the specific repositories that you select, choose **Only select repositories**\. Make sure to include the repo for the app that you are migrating in the repos that you select\.

1. Choose **Install & Authorize**\.

1. You are redirected to the **Add repository branch** page for your app in the Amplify console\.

1. In the **Recently updated repositories** list, select the name of the repository to connect\.

1. In the **Branch** list, select the name of the repository branch to connect\.

1. Choose **Next**\.

1. On the **Configure build settings** page, choose **Next**\.

1. On the **Review** page, choose **Save and deploy**\.

## Migrating an existing OAuth app to the Amplify GitHub App<a name="migrating-to-github-app-auth"></a>

Existing Amplify apps that you previously connected from GitHub repositories use OAuth for repo access\. We strongly recommend that you migrate these apps to use the Amplify GitHub App\.

Use the following instructions to migrate an app and delete its corresponding OAuth webhook in your GitHub account\. Note that the procedure for migrating varies depending on whether the Amplify GitHub app is already installed\. After you migrate your first app and install and authorize the GitHub App, you only need to update the repository permissions for subsequent app migrations\.

**To migrate an app from OAuth to the GitHub App**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app that you want to migrate\.

1. On the app's information page, locate the blue **Migrate to our GitHub App** message and choose **Start migration**\.

1. On the **Install and authorize GitHub App** page, choose **Configure GitHub App**\.

1. A new page opens in your browser on GitHub\.com, requesting permission to authorize AWS Amplify in your GitHub account\. Choose **Authorize**\.

1. Select the GitHub account where you want to install the Amplify GitHub App\.

1. Do one of the following:
   + To apply the installation to all repositories, choose **All repositories**\.
   + To limit the installation to the specific repositories that you select, choose **Only select repositories**\. Make sure to include the repo for the app that you are migrating in the repositories that you select\.

1. Choose **Install & Authorize**\.

1. You are redirected to the **Install and authorize GitHub App** page for your app in the Amplify console\. If GitHub authorization was successful, you will see a success message\. Choose, **Next**\.

1. On the **Complete installation** page, choose **Complete installation**\. This step deletes your existing webhook, creates a new one, and completes the migration\.

## Setting up the Amplify GitHub App for AWS CloudFormation, CLI, and SDK deployments<a name="setting-up-github-app-cloudformation"></a>

Existing Amplify apps that you previously connected from GitHub repositories use OAuth for repo access\. This can include apps that you deployed using the Amplify Command Line Interface \(CLI\), AWS CloudFormation, or the SDKs\. We strongly recommend that you migrate these apps to use the new Amplify GitHub App\. Migration must be performed in the Amplify console in the AWS Management Console\. For instructions, see [Migrating an existing OAuth app to the Amplify GitHub App](#migrating-to-github-app-auth)\.

You can use AWS CloudFormation, the Amplify CLI, and the SDKs to deploy a new Amplify app that uses the GitHub App for repo access\. This process requires that you first install the Amplify GitHub App in your GitHub account\. Next, you will need to generate a personal access token in your GitHub account\. Lastly, deploy the app and specify the personal access token\.

**Install the Amplify GitHub App in your account**

1. Open a web browser and navigate to the installation location for the Amplify GitHub App in the AWS Region where you will deploy your app\.

   Use the format `https://github.com/apps/aws-amplify-REGION/installations/new`, replacing *REGION* with your own input\. For example, if you are installing your app in the US West \(Oregon\) region, specify `https://github.com/apps/aws-amplify-us-west-2/installations/new`\.

1. Select the GitHub account where you want to install the Amplify GitHub app\.

1. Do one of the following:
   + To apply the installation to all repositories, choose **All repositories**\.
   + To limit the installation to the specific repositories that you select, choose **Only select repositories**\. Make sure to include the repo for the app that you are migrating in the repos that you select\.

1. Choose **Install**\.

**Generate a personal access token in your GitHub account**

1. Sign in to your GitHub account\.

1. In the upper right corner, locate your profile photo and choose **Settings** from the menu\.

1. In the left navigation menu, choose **Developer settings**\.

1. On the **GitHub Apps** page, in the left navigation menu, choose **Personal access tokens**\.

1. On the **Personal access tokens** page, choose **Generate new token**\.

1. On the **New personal access token** page, for **Note** enter a descriptive name for the token\.

1. In the **Select scopes** section, select **admin:repo\_hook**\.

1. Choose **Generate token**\.

1. Copy and save the personal access token\. You will need to provide it when you deploy an Amplify app with the CLI, AWS CloudFormation, or the SDKs\.

After the Amplify GitHub app is installed in your GitHub account and you have generated a personal access token, you can deploy a new app with the Amplify CLI, AWS CloudFormation, or the SDKs\. Use the `accessToken` field to specify the personal access token that you created in the previous procedure\. For more information, see [CreateApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateApp.html#API_CreateApp_RequestSyntax) in the *Amplify API reference* and [AWS::Amplify::App](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html) in the *AWS CloudFormation User Guide*\.

The following CLI command deploys a new Amplify app that uses the GitHub App for repository access\. Replace *myapp\-using\-githubapp*, *https://github\.com/Myaccount/react\-app*, and *MY\_TOKEN* with your own information\.

```
aws amplify create-app --name myapp-using-githubapp --repository https://github.com/Myaccount/react-app --access-token MY_TOKEN
```

## Setting up web previews with the Amplify GitHub App<a name="setting-up-github-app-pr-previews"></a>

A web preview deploys every pull request \(PR\) made to your GitHub repository to a unique preview URL\. Previews now use the Amplify GitHub App for access to your GitHub repo\. For instructions on installing and authorizing the GitHub App for web previews, see [Enable web previews](pr-previews.md#enable-web-previews) \.