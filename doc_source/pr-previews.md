# Web previews for pull requests<a name="pr-previews"></a>

Web previews offer development and quality assurance \(QA\) teams a way to preview changes from pull requests \(PRs\) before merging code to a production or integration branch\. Pull requests let you tell others about changes you’ve pushed to a branch in a repository\. After a pull request is opened, you can discuss and review the potential changes with collaborators and add follow\-up commits before your changes are merged into the base branch\.

A web preview deploys every pull request made to your GitHub repository to a unique preview URL which is completely different from the URL your main site uses\. For apps with backend environments provisioned using the Amplify CLI or Amplify Studio, every pull request \(**private Git repositories only**\) spins up an ephemeral backend that is deleted when the PR is closed\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews1.png)

**Note**  
**Previews** is visible in the Amplify console’s **App settings** menu only when an app is set up for continuous deployment and connected to a git repository\. For instructions on this type of deployment, see [Getting started with existing code](getting-started.md)\.

## Enable web previews<a name="enable-web-previews"></a>

For apps stored in a GitHub repo, previews use the Amplify GitHub App for repo access\. If you are enabling web previews on an existing Amplify app that you previously deployed from a GitHub repo using OAuth for access, you must first migrate the app to use the Amplify GitHub App\. For migration instructions, see [Migrating an existing OAuth app to the Amplify GitHub App](setting-up-GitHub-access.md#migrating-to-github-app-auth)\.

**To enable web previews for pull requests**

1. Choose **App settings**, **Previews** and then choose **Enable previews**\. 
**Important**  
For security purposes, previews only work with private repositories for fullstack apps\.

1. For GitHub repositories only, do the following to install and authorize the Amplify GitHub App in your account:

   1. In the **Install GitHub App to enable previews** window, choose **Install GitHub app**\.

   1. Select the GitHub account where you want to configure the Amplify GitHub App\.

   1. A page opens on Github\.com to configure repository permissions for your account\.

   1. Do one of the following:
      + To apply the installation to all repositories, choose **All repositories**\.
      + To limit the installation to the specific repositories that you select, choose **Only select repositories**\. Make sure to include the repo for the app that you are enabling web previews for in the repositories that you select\.

   1. Choose **Save**

1. After you enable previews for your repo, return to the Amplify console to enable previews for specific branches\. On the **Previews** page, select a branch from the list and choose **Manage**\.   
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews2.png)

1. In the **Manage preview settings for branch** window, turn on **Pull request previews**\.

1. For fullstack applications do one of the following:
   + Choose, **Create new backend environment for every Pull Request**\. This option enables you to test changes without impacting production\.
   + Choose **Point all Pull Requests for this branch to an existing environment**\.

1. Choose **Confirm**\.

The next time you submit a pull request for the branch, Amplify builds and deploys your PR to a preview URL\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews4.png)

For GitHub repositories only, you can access a preview of your URL directly from the pull request in your GitHub account\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews3.png)

After the pull request is closed, the preview URL is deleted, and any temporary backend environment linked to the pull request is deleted\.

## Web preview access with subdomains<a name="web-preview-access-on-subdomains"></a>

Web previews from pull requests are accessible with subdomains for an Amplify app that is connected to a custom domain managed by Amazon Route 53\. When the pull request is closed, branches and subdomains associated with the pull request are automatically deleted\. This is the default behavior for web previews after you set up pattern\-based feature branch deployments for your app\. For instructions on setting up automatic subdomains, see [Set up automatic subdomains for a Amazon Route 53 custom domain](to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md)\.