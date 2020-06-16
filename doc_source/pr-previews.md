# Web Previews<a name="pr-previews"></a>

Web Previews offer development and QA teams a way to preview changes from pull requests before merging code to a production or integration branch\. Pull requests let you tell others about changes you’ve pushed to a branch in a repository\. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow\-up commits before your changes are merged into the base branch\.

A web preview deploys every pull request made to your GitHub repository to a unique preview URL; completely different from the one your main site uses\. For apps with backend environments provisioned via the Amplify CLI, every pull request \(**private Git repositories only**\) spins up an ephemeral backend that is deleted when the PR is closed\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews1.png)

**Note**  
**Previews** is visible in the Amplify Console’s App settings menu only when an app is set up for continuous deployment and connected to a git repository\. For instructions on this type of deployment, see [Getting started with existing code](getting-started.md)\.

## Enable web previews<a name="enable-web-previews"></a>

1. Choose **App setting**, **Previews** and then choose **Enable previews**\. For GitHub repositories only, you are required to install a GitHub app in your account to enable this feature\. You can give the Amplify Console permission to all repositories or only the current one\. **Note: For security purposes, Previews will only work with private repositories for fullstack apps using the Amplify CLI\.** 

1. Once enabled, return to the Amplify Console to enable previews for specific branches\. Pick a branch from the list and choose **Manage**\. For fullstack applications, you will be able to choose to create a a new backend for every pull request, or point all pull requests to an existing backend environment\. Choosing the first option will allow you to test changes without impacting production\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews2.png)

1. The next time you submit a pull request for the branch, the Amplify Console will build and deploy your PR to a preview URL For GitHub repositories only, you can view a preview of your URL directly from the pull request\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews3.png)

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews4.png)

1. Once the pull request is closed, the preview URL is deleted, and any ephemeral backend environment linked to the pull request is deleted\.