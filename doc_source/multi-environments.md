# Feature branch deployments and team workflows<a name="multi-environments"></a>

The Amplify Console is designed to work with feature branch and GitFlow workflows\. The Amplify Console leverages Git branches to create new deployments every time a developer connects a new branch in their repository\. After connecting your first branch, you can create a new feature branch deployment by adding a branch as follows:

1. On the branch list page, choose **Connect branch**\.

1. Choose a branch from your repository\.

1. Save and then deploy your app\.

Your app now has two deployments available at *https://main\.appid\.amplifyapp\.com* and *https://dev\.appid\.amplifyapp\.com*\. This may vary from team\-to\-team, but typically the **main branch** \(formerly referred to as the master branch\) tracks release code and is your production branch\. The **develop branch** is used as an integration branch to test new features\. This way beta testers can test unreleased features on the develop branch deployment, without affecting any of the production end users on the main branch deployment\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-environments-1.png)

**Topics**
+ [Team workflows with Amplify CLI backend environments](team-workflows-with-amplify-cli-backend-environments.md)
+ [Pattern\-based feature branch deployments](pattern-based-feature-branch-deployments.md)