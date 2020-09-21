# Restricting access<a name="access-control"></a>

If you are working on unreleased features you can password protect feature branches that are not ready to be accessed publicly\.

![\[Video graphic of password protected sign in.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/password.gif)

**To set passwords on feature branches**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app you want to set feature branch passwords on\.

1. In the navigation pane, choose **App settings**, and then choose **Access control**\.

1. In the **Access control settings** section, choose **Manage access**\.  
![\[Screenshot of the Access control settings section listing the branches connected to the app.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/accesscontrol1.png)

1. Do one of the following in **Access control settings**:
   + To set a username and password that applies to all connected branches, turn on **Apply a global password**\. For example, if you have **main**, **dev**, and **feature** branches connected, you can use a global password to set the same user name and password for all branches\.
   + To exclude branches from a global password, turn on **Apply a global password**, and then choose **Publicly viewable** for **Access setting** for any branch that you want to exclude\.
   + To apply a username and password to an individual branch, turn off **Apply a global password**\. For the branch that you want to enter a unique username and password for, choose **Restricted\-password required** for **Access setting** and enter a username and password\.  
![\[Screenshot of the Branch access section showing the options for applying passwords globally or per branch.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/accesscontrol2.png)