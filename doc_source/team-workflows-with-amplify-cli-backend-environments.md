# Team workflows with Amplify backend environments<a name="team-workflows-with-amplify-cli-backend-environments"></a>

A feature branch deployment consists of a **frontend**, and an optional **backend** environment\. The frontend is built and deployed to a global content delivery network \(CDN\), while the backend is deployed by Amplify Studio or the Amplify CLI to AWS\. For more information about this deployment scenario, see [Getting started with fullstack continuous deployments](deploy-backend.md)\.

**Note**  
You can easily reuse Amplify backend environments across your Amplify apps\. For more information, see [Use Amplify backends across apps](reuse-backends.md)\.

Amplify Hosting continuously deploys backend resources such as GraphQL APIs and Lambda functions with your feature branch deployments\. You can use the following branching models to deploy your backend and frontend with Amplify Hosting\.

**Topics**
+ [Feature branch workflow](#standard)
+ [GitFlow workflow](#gitflow)
+ [Per\-developer sandbox](#sandbox)

## Feature branch workflow<a name="standard"></a>
+ Create **prod**, **test**, and **dev** backend environments with Amplify Studio or the Amplify CLI\.
+ Map the **prod** backend to the **main** branch\. 
+ Map the **test** backend to the **develop** branch\.
+ Team members can use the **dev** backend environment for testing individual **feature** branches\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/FeatureBranchWorkflow.png)

1. Install the Amplify CLI to initialize a new Amplify project\.

   ```
   npm install -g @aws-amplify/cli
   ```

1. Initialize a *prod* backend environment for your project\. If you don’t have a project, create one using bootstrap tools like create\-react\-app or Gatsby\.

   ```
   create-react-app next-unicorn
   cd next-unicorn
   amplify init
    ? Do you want to use an existing environment? (Y/n): n
    ? Enter a name for the environment: prod
   ...
   amplify push
   ```

1. Add *test* and *dev* backend environments\.

   ```
   amplify env add
    ? Do you want to use an existing environment? (Y/n): n
    ? Enter a name for the environment: test
   ...
   amplify push
   
   amplify env add
    ? Do you want to use an existing environment? (Y/n): n
    ? Enter a name for the environment: dev
   ...
   amplify push
   ```

1. Push code to a Git repository of your choice \(in this example we’ll assume you pushed to main\)\.

   ```
   git commit -am 'Added dev, test, and prod environments'
   git push origin main
   ```

1. Visit Amplify in the AWS Management Console to see your current backend environment\. Navigate a level up from the breadcrumb to view a list of all backend environments created in the **Backend environments** tab\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/reuse-backend-5.png)

1. Switch to the **Frontend environments** tab and connect your repository provider and *main* branch\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/reuse-backend-6.png)

1. In the build settings screen, pick an existing backend environment to set up continuous deployment with the main branch\. Choose *prod* from the dropdown and grant the service role to Amplify\. Choose **Save and deploy**\. After the build completes you will get a main branch deployment available at *https://main\.appid\.amplifyapp\.com*\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/reuse-backend-2.png)

1. Connect *develop* branch in Amplify \(assume *develop* and *main* branch are the same at this point\)\. Choose the *test* backend environment\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/reuse-backend-4.png)

1. Amplify is now set up\. You can start working on new features in a feature branch\. Add backend functionality by using the *dev* backend environment from your local workstation\.

   ```
   git checkout -b newinternet
   amplify env checkout dev
   amplify add api
   ...
   amplify push
   ```

1. After you finish working on the feature, commit your code, create a pull request to review internally\.

   ```
   git commit -am 'Decentralized internet v0.1'
   git push origin newinternet
   ```

1. To preview what the changes will look like, go to the Amplify console and connect your feature branch\. Note: If you have the AWS CLI installed on your system \(Not the Amplify CLI\), you can connect a branch directly from your terminal\. You can find your appid by going to App settings > General > AppARN: *arn:aws:amplify:<region>:<region>:apps/<appid>* 

   ```
   aws amplify create-branch --app-id <appid> --branch-name <branchname>
   aws amplify start-job --app-id <appid> --branch-name <branchname> --job-type RELEASE
   ```

1. Your feature will be accessible at *https://newinternet\.appid\.amplifyapp\.com* to share with your teammates\. If everything looks good merge the PR to the develop branch\.

   ```
   git checkout develop
   git merge newinternet
   git push
   ```

1. This will kickoff a build that will update the backend as well as the frontend in Amplify with a branch deployment at *https://dev\.appid\.amplifyapp\.com*\. You can share this link with internal stakeholders so they can review the new feature\.

1. Delete your feature branch from Git, Amplify, and remove the backend environment from the cloud \(you can always spin up a new one based on by running ‘amplify env checkout prod’ and running ‘amplify env add’\)\.

   ```
   git push origin --delete newinternet
   aws amplify delete-branch --app-id <appid> --branch-name <branchname>
   amplify env remove dev
   ```

## GitFlow workflow<a name="gitflow"></a>

GitFlow uses two branches to record the history of the project\. The *main* branch tracks release code only, and the *develop* branch is used as an integration branch for new features\. GitFlow simplifies parallel development by isolating new development from completed work\. New development \(such as features and non\-emergency bug fixes\) is done in *feature* branches\. When the developer is satisfied that the code is ready for release, the *feature* branch is merged back into the integration *develop* branch\. The only commits to the main branch are merges from *release* branches and *hotfix* branches \(to fix emergency bugs\)\.

The diagram below shows a recommended setup with GitFlow\. You can follow the same process as described in the feature branch workflow section above\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/GitflowWorkflow.png)

## Per\-developer sandbox<a name="sandbox"></a>
+ Each developer in a team creates a sandbox environment in the cloud that is separate from their local computer\. This allows developers to work in isolation from each other without overwriting other team members’ changes\.
+ Each branch in Amplify has its own backend\. This ensures that the Amplify uses the Git repository as a single source of truth from which to deploy changes, rather than relying on developers on the team to manually push their backend or front end to production from their local computers\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/AmplifySandboxWorkflow.png)

1. Install the Amplify CLI to initialize a new Amplify project\.

   ```
   npm install -g @aws-amplify/cli
   ```

1. Initialize a *mary* backend environment for your project\. If you don’t have a project, create one using bootstrap tools like create\-react\-app or Gatsby\.

   ```
   cd next-unicorn
   amplify init
    ? Do you want to use an existing environment? (Y/n): n
    ? Enter a name for the environment: mary
   ...
   amplify push
   ```

1. Push code to a Git repository of your choice \(in this example we’ll assume you pushed to main\.

   ```
   git commit -am 'Added mary sandbox'
   git push origin main
   ```

1. Connect your repo > *main* to Amplify\.

1. The Amplify console will detect backend environments created by the Amplify CLI\. Choose *Create new environment* from the dropdown and grant the service role to Amplify\. Choose **Save and deploy**\. After the build completes you will get a main branch deployment available at *https://main\.appid\.amplifyapp\.com* with a new backend environment that is linked to the branch\.

1. Connect *develop* branch in Amplify \(assume *develop* and *main* branch are the same at this point\) and choose *Create new environment*\. After the build completes you will get a develop branch deployment available at *https://develop\.appid\.amplifyapp\.com* with a new backend environment that is linked to the branch\.