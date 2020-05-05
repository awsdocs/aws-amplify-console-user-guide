# Incoming Webhooks<a name="webhooks"></a>

Set up an incoming webhook in the Amplify Console to trigger a build without comitting code to your Git repository\. Webhook triggers can be used with headless CMS tools \(such as Contentful or GraphCMS\) to trigger builds on content changes, or to trigger daily builds using services such as Zapier\.

1. Log in to the [Amplify Console](https://console.aws.amazon.com/amplify/home) and choose your app\.

1. Navigate to **App Settings > Build Settings** and scroll to the **Incoming webhook** container\. Choose **Create webhook**   
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/webhooks.png)

1. Give your webhook a name and choose **Save**\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/webhooks2.png)

1. You can copy the webhook URL or run a curl command in your command line to trigger a new build\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/webhooks3.png)