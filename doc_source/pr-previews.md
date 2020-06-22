# Web previews<a name="pr-previews"></a>

Web previews offer development and quality assurance \(QA\) teams a way to preview changes from pull requests \(PRs\) before merging code to a production or integration branch\. Pull requests let you tell others about changes you’ve pushed to a branch in a repository\. After a pull request is opened, you can discuss and review the potential changes with collaborators and add follow\-up commits before your changes are merged into the base branch\.

A web preview deploys every pull request made to your GitHub repository to a unique preview URL which is completely different from the URL your main site uses\. For apps with backend environments provisioned using the Amplify CLI, every pull request \(**private Git repositories only**\) spins up an ephemeral backend that is deleted when the PR is closed\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews1.png)

**Note**  
**Previews** is visible in the Amplify Console’s App settings menu only when an app is set up for continuous deployment and connected to a git repository\. For instructions on this type of deployment, see [Getting started with existing code](getting-started.md)\.

## Enable web previews<a name="enable-web-previews"></a>

**To enable web previews for pull requests**

1. Choose **App settings**, choose ** Previews** and then choose **Enable previews**\. For GitHub repositories only, you are required to install a GitHub app in your account to enable this feature\. You can give the Amplify Console permission to all repositories or the current repository only\. 
**Important**  
For security purposes, previews only work with private repositories for fullstack apps using the Amplify CLI\.

1. After you enable previews, return to the Amplify Console to enable previews for specific branches\. Choose a branch from the list and choose **Manage**\. For fullstack applications, you can choose to create a a new backend for every pull request, or point all pull requests to an existing backend environment\. By choosing the first option, you can test changes without impacting production\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews2.png)

The next time you submit a pull request for the branch, the Amplify Console builds and deploys your PR to a preview URL\. For GitHub repositories only, you can view a preview of your URL directly from the pull request\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews3.png)

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/previews4.png)

After the pull request is closed, the preview URL is deleted, and any ephemeral backend environment linked to the pull request is deleted\.

## Web preview access with subdomains<a name="web-preview-access-on-subdomains"></a>

Web previews from pull requests are accessible with subdomains for an Amplify app that is connected to a custom domain managed by Amazon Route 53\. When the pull request is closed, branches and subdomains associated with the pull request are automatically deleted\. This is the default behavior for web previews after you set up pattern\-based feature branch deployments for your app\. For instructions on setting up automatic subdomains, see [Set up automatic subdomains for a Amazon Route 53 custom domain](to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md)\.