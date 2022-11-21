# Getting started with fullstack continuous deployments<a name="deploy-backend"></a>

Amplify Hosting enables developers building apps with the Amplify Framework to continuously deploy updates to their backend and frontend on every code commit\. With Amplify Hosting, you can deploy serverless backends with GraphQL/REST APIs, authentication, analytics, and storage, created using Amplify Studio, on the same commit as your frontend code\.



In this tutorial, you will set up a fullstack CI/CD workflow with Amplify\. You will deploy a frontend app to Amplify Hosting\. Then you will create a backend using Amplify Studio\. Finally, you will connect the cloud backend to the frontend app\.

**Topics**
+ [Prerequisites](#fullstack-sample-prerequisites)
+ [Step 1: Deploy a frontend](#step-1-deploy-frontend)
+ [Step 2: Create a backend](#step-2-create-backend)
+ [Step 3: Connect the backend to the frontend](#step-3-connect-backend-to-frontend)
+ [Next steps](#next-steps-set-up-feature-branch-deployments)

## Prerequisites<a name="fullstack-sample-prerequisites"></a>

Before starting this tutorial, you will need to do the following:
+ Create an AWS account\. Open [https://portal\.aws\.amazon\.com/billing/signup\#/start/email](https://portal.aws.amazon.com/billing/signup#/start/email) to get started\.
+ Create an account with a git repository provider, such as GitHub, Bitbucket, GitLab, or AWS CodeCommit\.
+ Install the Amplify Command Line Interface \(CLI\)\. For instructions, see [Install the Amplify CLI](https://docs.amplify.aws/cli/start/install/) in the *Amplify Framework Documentation*\.

## Step 1: Deploy a frontend<a name="step-1-deploy-frontend"></a>

If you have an existing frontend app in a git repository that you want to use for this example, you can proceed to the instructions for deploying a frontend app\.

If you need to create a new frontend app to use for this example, choose the following **Deploy to Amplify Console** button to deploy a [Create React App](https://create-react-app.dev/docs/getting-started) starter app to your Amplify account\.

[https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/aws-samples/aws-starter-react-for-github-actions](https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/aws-samples/aws-starter-react-for-github-actions)

Alternatively, you can follow the [Create React App](https://create-react-app.dev/docs/getting-started) instructions in the *Create React App documentation*\.

**To deploy a frontend app**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. On the **All apps** page, choose **New app**, then **Host web app** in the upper right corner\.

1. Select your GitHub, Bitbucket, GitLab, or AWS CodeCommit repository provider and then choose **Continue**\.

1. Amplify authorizes access to your git repository\. For GitHub repositories, Amplify now uses the GitHub Apps feature to authorize Amplify access\. 

   For more information about installing and authorizing the GitHub App, see [Setting up Amplify access to GitHub repositories](setting-up-GitHub-access.md)\.

1. On the **Add repository branch** page do the following:

   1. In the **Recently updated repositories** list, select the name of the repository to connect\.

   1. In the **Branch** list, select the name of the repository branch to connect\.

   1. Choose **Next**\.

1. On the **Configure build settings** page, choose **Next**\.

1. On the **Review** page, choose **Save and deploy**\.

## Step 2: Create a backend<a name="step-2-create-backend"></a>

Now that you have deployed a frontend app to Amplify Hosting, you can create a backend\. Use the following instructions to create a backend with a simple database and GraphQL API endpoint\.

**To create a backend**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. On the **All apps** page, select the app that you created in *Step 1*\.

1. On the app homepage, choose the **Backend environments** tab, then choose **Get started**\. This initiates the set up process for a default **staging** environment\.

1. After the set up finishes, choose **Launch Studio** to access the **staging** backend environment in Amplify Studio\.

Amplify Studio is a visual interface to create and manage your backend and accelerate your frontend UI development\. For more information about Amplify Studio, see the [Amplify Studio documentation](https://docs.amplify.aws/console/)\.

Use the following instructions to create a simple database using the Amplify Studio visual backend builder interface\.

**Create a data model**

1. On the home page for your app's **staging** environment, choose **Create data model**\. This opens the data model designer\.

1. On the **Data modeling** page, choose **Add model**\.

1. For the title, enter **Todo**\.

1. Choose **Add a field**\.

1. For **Field name**, enter **Description**\.

   The following screenshot is an example of how your data model will look in the designer\.  
![\[The Amplify Studio UI for creating a data model.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-deploy-backend-1.png)

1. Choose **Save and Deploy**\.

1. Return to the Amplify Hosting console and the **staging** environment deployment will be in progress\.

During deployment, Amplify Studio creates all the required AWS resources in the backend, including an AWS AppSync GraphQL API to access data and an Amazon DynamoDB table to host the Todo items\. Amplify uses AWS CloudFormation to deploy your backend, which enables you to store your backend definition as infrastructure\-as\-code\.

## Step 3: Connect the backend to the frontend<a name="step-3-connect-backend-to-frontend"></a>

Now that you have deployed a frontend and created a cloud backend that contains a data model, you need to connect them\. Use the following instructions to pull your backend definition down to your local app project with the Amplify CLI\.

**To connect a cloud backend to a local frontend**

1. Open a terminal window and navigate to the root directory of your local project\.

1. Run the following command in the terminal window, replacing the red text with the unique app ID and backend environment name for your project\.

   ```
   amplify pull --appId abcd1234 --envName staging
   ```

1. Follow the instructions in the terminal window to complete the project set up\.

Now you can configure the build process to add the backend to the continuous deployment workflow\. Use the following instructions to connect a frontend branch with a backend in the Amplify Hosting console\.

**To connect a frontend app branch and cloud backend**

1. On the app homepage, choose the **Hosting environments** tab\.

1. Locate the **main** branch and choose **Edit**\.  
![\[The location of the Edit link for a branch in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify_edit_backend_alternate.png)

1. In the **Edit target backend** window, for **Environment**, select the name of the backend to connect\. In this example, choose the **staging** backend that you created in *Step 2*\. 

   By default, full\-stack CI/CD is enabled\. Uncheck this option to turn off full\-stack CI/CD for this backend\. Turning off full\-stack CI/CD causes the app to run in *pull only* mode\. At build time, Amplify will automatically generate the `aws-exports.js` file only, without modifying your backend environment\.

1. Next, you must set up a service role to give Amplify the permissions it requires to make changes to your app backend\. You can either use an existing service role or create a new one\. For instructions, see [Adding a service role](how-to-service-role-amplify-console.md)\.

1. After adding a service role, return to the **Edit target backend** window and choose **Save**\.

1. To finish connecting the **staging** backend to the **main** branch of the frontend app, perform a new build of your project\.

   Do one of the following:
   + From your git repository, push some code to initiate a build in the Amplify console\.
   + In the Amplify console, navigate to the app's build details page and choose **Redeploy this version**\.

## Next steps<a name="next-steps-set-up-feature-branch-deployments"></a>

### Set up feature branch deployments<a name="set-up-feature-branch-deployments"></a>

Follow our recommended workflow to [set up feature branch deployments with multiple backend environments](https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html#team-workflows-with-amplify-cli-backend-environments)\.

### Create a frontend UI in Amplify Studio<a name="create-studio-ui-components"></a>

Use Studio to build your frontend UI with a set of ready\-to\-use UI components, and then connect it to your app backend\. For more information and tutorials, see the user guide for [Amplify Studio](https://docs.amplify.aws/console) in the *Amplify Framework Documentation*\.