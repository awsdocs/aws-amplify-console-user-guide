# Restricting access to branches<a name="access-control"></a>

If you are working on unreleased features, you can password protect feature branches that are not ready to be publicly accessed\. When access control is set on a branch, users are prompted for a user name and password when they attempt to access the URL for the branch\.

**To set passwords on feature branches**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app you want to set feature branch passwords on\.

1. In the navigation pane, choose **App settings**, and then choose **Access control**\.

1. In the **Access control settings** section, choose **Manage access**\.

1. Do one of the following in **Access control settings**:
   + To set a username and password that applies to all connected branches, turn on **Apply a global password**\. For example, if you have **main**, **dev**, and **feature** branches connected, you can use a global password to set the same username and password for all branches\.
   + To apply a username and password to an individual branch, turn off **Apply a global password**\. For the branch that you want to set a unique username and password for, choose **Restricted\-password required** for **Access setting** and enter a username and password\.

1. If you are managing access control for a server\-side rendered \(SSR\) app, redeploy the app by performing a new build from your Git repository\. This step is required to enable Amplify to apply your access control settings\.