# Getting Started with Fullstack Continuous Deployments<a name="deploy-backend"></a>

The Amplify Console enables developers building apps with the Amplify Framework to continuously deploy updates to their backend and frontend on every code commit\. With the Amplify Console you can deploy serverless backends with GraphQL/REST APIs, authentication, analytics, and storage created by the Amplify CLI on the same commit as your frontend code\.

**Important**  
This feature only works with the Amplify CLI v4\.0\+

In this tutorial, we are going to create and deploy a React app which implements a basic authentication flow for signing up/signing in users as well as protected client side routing using AWS Amplify\.

## Step 1: Deploy a fullstack sample<a name="step-1-deploy-a-fullstack-sample"></a>

Log in to the [Amplify Console](https://console.aws.amazon.com/amplify/home) and choose **Get Started** under **Deploy**\. In the following screen, choose **From fullstack samples**\. Alternatively, start your own adventure by building a backend **from scratch** by installing the Amplify CLI\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/fullstack1.png)

Choose the **Authentication Starter** and **Deploy app**\. You will be asked to connect your GitHub account\. Connecting your GitHub acccount allows the Amplify Console to create a fork of the repository in your account, deploy the AWS backend services, and build and deploy the frontend\. In order to deploy backend resources to AWS, you will need to [create a service role](how-to-service-role-amplify-console.md)\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/fullstack2.gif)

## Step 2: Explore the Fullstack App<a name="step-2-explore-the-fullstack-app"></a>

Your app build will start by deploying the backend followed by the frontend\. Click on the branch name to see the running build\. When the build completes you will be able to see screenshots of your app on different devices\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-backend-frontend.png)

At the end of the build, you will have one frontend environment \(the main branch deployed at *‘https://main\.appid\.amplifyapp\.com’*\) and one backend environment named devX\. To add a user to your app, you can either register a user through the deployed frontend, or choose the **Authentication** tab which links to the Amazon Cognito UserPool\. Create a user and try logging in to your app\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/fullstack3.gif)

## Step 3: Add a GraphQL backend<a name="step-3-add-a-graphql-backend"></a>

1. Let’s add a GraphQL API backend with a NoSQL database to your app\. To start, clone the repository that was forked in your account\.

   ```
   git clone git@github.com:<username>/create-react-app-auth-amplify.git
   cd create-react-app-auth-amplify
   ```

1. From the **Backend environments** tab, choose **Edit backend**\. As a pre\-requisite, follow the instructions to install and configure the Amplify CLI\. The Amplify command line toolchain allows you to edit the backend you just created to add more functionality such as GraphQL/REST APIs, analytics, and storage\. Once the Amplify CLI is configured, copy the *amplify pull* command to connect to this backend from your local machine\.

   ```
   amplify pull --appId XXXXXXXX --envName devw
   ```  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/fullstack4.png)

1. Add the GraphQL API using the default todo example\. Learn more about modeling your backend with the [GraphQL transform](https://aws-amplify.github.io/docs/cli-toolchain/graphql)\.

   ```
   amplify add api
   ? Please select from one of the below mentioned services GraphQL
   ? Provide API name: todo
   ? Choose the default authorization type for the API API key
   ? Enter a description for the API key:
   ? After how many days from now the API key should expire (1-365): 7
   ? Do you want to configure advanced settings for the GraphQL API No, I am done.
   ? Do you have an annotated GraphQL schema? No
   ? Do you want a guided schema creation? (Y/n) Y
   ? What best describes your project: Single object with fields (e.g., “Todo” with ID, name, description)
   ? Do you want to edit the schema now? No
   ...
   GraphQL schema compiled successfully.
   ```

1. To deploy these changes to the cloud run the following commands\.

   ```
   amplify push
   Current Environment: devw
   
   | Category | Resource name   | Operation | Provider plugin   |
   | -------- | --------------- | --------- | ----------------- |
   | Api      | todo            | Create    | awscloudformation |
   | Auth     | cognitocf0c6096 | No Change | awscloudformation |
   ? Are you sure you want to continue? (Y/n) Y
   ..
   ✔ Generated GraphQL operations successfully and saved at src/graphql
   ✔ All resources are updated in the cloud
   GraphQL endpoint: https://gumwpbojgraj5b547y5d3shurq.appsync-api.us-west-2.amazonaws.com/graphql
   GraphQL API KEY: da2-vlthvw5qcffxzl2hibgowv3rdq
   ```

1. Visit the Amplify Console to view the added API category\. Choosing the API category will allow you to navigate to the AppSync Console \(to write queries or mutations performing CRUD operations\), or the DynamoDB Console \(to view your Todo table\)\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/fullstack5.png)

1. Use the [Amplify GraphQL client](https://aws-amplify.github.io/docs/js/api#amplify-graphql-client) to write frontend code that lists and updates the todos\. To deploy the updates to your frontend, simply commit your code and a new build will be triggered in the Amplify Console\.

## Next steps: Set up feature branch deployments<a name="next-steps-set-up-feature-branch-deployments"></a>

Follow our recommended workflow to [set up feature branch deployments with multiple backend environments](https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html#team-workflows-with-amplify-cli-backend-environments)\.