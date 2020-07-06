# Notifications<a name="notifications"></a>

You can set up notifications for an Amplify app to alert stakeholders or team members when a build succeeds or fails\. Amplify Console creates an Amazon Simple Notification Service \(SNS\) topic in your account and uses it to configure email notifications\. This SNS topic can be used to send notifications to other tools such as Slack\. Notifications can be configured to apply to all branches or specific branches of an Amplify app\.

## Email Notifications<a name="email-notifications"></a>

Use the following procedures to set up email notifications for all branches or specific branches of an Amplify app\.

**To set up email notifications for an Amplify app**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app that you want to set up email notifications for\.

1. In the navigation pane, choose **App Settings**, **Notifications**, and then in the **Email notifications** section, choose **Add notification**\. 

1. Do one of the following in the **Manage notifications** section:
   + To send notifications for a single branch, for **Email**, enter the email address to send notifications to\. For **Branch**, select the name of the branch to send notifications for\. 
   +  To send notifications for all connected branches, for **Email**, enter the email address to send notifications to\. For **Branch**, select *All Branches*\.

1. Choose **Save** when you are finished\.  
![\[Screenshot of the Manage notifications section in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-notifications-email.png)