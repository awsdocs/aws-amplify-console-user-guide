# Migrating a Next\.js 11 SSR app to Amplify Hosting compute<a name="update-app-nextjs-version"></a>

When you deploy a new Next\.js app, by default Amplify uses the most recent supported version of Next\.js\. Currently, the Amplify Hosting compute SSR provider supports Next\.js version 13\.

The Amplify console detects apps in your account that were deployed prior to the release of the Amplify Hosting compute service with full support for Next\.js 12 or later\. The console displays an information banner identifying apps with branches that are deployed using Amplify's previous SSR provider, Classic \(Next\.js 11 only\)\. We strongly recommend that you migrate your apps to the Amplify Hosting compute SSR provider\.

You must manually migrate the app and all of its production branches at the same time\. An app can't contain both Classic \(Next\.js 11 only\) and Next\.js 12 branches\.

Use the following instructions to migrate an app to the Amplify Hosting compute SSR provider\.

**To migrate an app to the Amplify Hosting compute SSR provider**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the Next\.js app that you want to migrate\.
**Note**  
Before you migrate an app in the Amplify console, you must first update the app's package\.json file to use Next\.js version 12 or later\.

1. In the navigation pane, choose **App settings**, **General**\.

1. On the app homepage, the console displays a banner if the app has branches deployed using the *Classic \(Next\.js 11 only\)* **SSR provider**\. On the banner, choose **Migrate**\.

1. In the migration confirmation window, select the three statements and choose **Migrate**\.

1. Amplify will build and redeploy your app to complete the migration\.

## Reverting an SSR migration<a name="revert-ssr-migration"></a>

When you deploy a Next\.js app, Amplify Hosting detects the settings in your app and sets the internal platform value for the app\. There are three valid platform values\. An SSG app is set to the platform value `WEB`\. An SSR app using Next\.js version 11 is set to the platform value `WEB_DYNAMIC`\. A Next\.js 12 or later SSR app is set to the platform value `WEB_COMPUTE`\.

When you migrate an app using the instructions in the previous section, Amplify changes the platform value of your app from `WEB_DYNAMIC` to `WEB_COMPUTE`\. After the migration to Amplify Hosting compute is complete, you can't revert the migration in the console\. To revert the migration, you must use the AWS Command Line Interface to change the app's platform back to `WEB_DYNAMIC`\. Open a terminal window and enter the following command, updating the text in red with your unique app id and Region\.

```
aws amplify update-app --app-id abcd1234 --platform WEB_DYNAMIC --region us-west-2
```