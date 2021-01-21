# Manual deploys<a name="manual-deploys"></a>

Manual deploys allows you to publish your web app to the Amplify Console without connecting a Git provider\. You can choose to drag and drop a folder from your desktop and host your site in seconds\. Alternatively, you can reference assets in an Amazon S3 bucket\. You can also specify a public URL to the location where your files are stored\.

For Amazon S3, you can also set up AWS Lambda triggers to update your site each time new assets are uploaded\. [This blog post](http://aws.amazon.com/blogs/mobile/deploy-files-s3-dropbox-amplify-console/) describes the process for setting up a Lambda trigger to automatically deploy changes to Amplify when updates are made to an Amazon S3 bucket\.

## Drag and drop<a name="drag-and-drop"></a>

**To manually deploy an app using drag and drop**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. At the top of the page, choose **Get started**\.

1. In the **Deliver** section, choose **Get started**\.

1. On the **Host your web app** page, choose **Deploy without Git provider**\. Then, choose **Continue**\.

1. In the **Start a manual deployment** section, for **App name**, enter the name of your app\.

1. For **Environment name**, enter a meaningful name for the environment, such as **development** or **production**\.

1. For **Method**, choose **Drag and drop**\.

1. Either drag and drop files from your desktop onto the drop zone or use **Choose files** to select the files from your computer\. The files that you drag and drop or select can be a folder or a zip file that contains the root of your site\.

1. Choose **Save and deploy**\.

![\[An animated gif that demonstrates how to drag and drop or choose the files to deploy your app.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/manual-deploys.gif)

## Amazon S3 or any URL<a name="amazon-s3-or-any-url"></a>

**To manually deploy an app from Amazon S3 or a public URL**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. At the top of the page, choose **Get started**\.

1. In the **Deliver** section, choose **Get started**\.

1. On the **Host your web app** page, choose **Deploy without Git provider**\. Then, choose **Continue**\.

1. In the **Start a manual deployment** section, for **App name**, enter the name of your app\.

1. For **Environment name**, enter a meaningful name for the environment, such as **development** or **production**\.

1. For **Method**, choose either **Amazon S3** or **Any URL**\.

1. The procedure for uploading your files depends on the upload method\.
   + Amazon S3

     1. For **Bucket**, select the name of the bucket from the list\.

     1. For **Zip file**, select the name of the zip file to deploy\.
   + Any URL

     1. For **Resource URL**, enter the URL to the zipped file to deploy\.

1. Choose **Save and deploy**\.

**Note**  
When you create the zip folder, make sure you zip the contents of your build output and not the top level folder\. For example, if your build output generates a folder named “build” or “public”, first navigate into that folder, select all of the contents, and zip it from there\. If you do not do this, you will see an “Access Denied” error because the site's root directory will not be initialized properly\.  

```
<Error>
  <Code>AccessDenied</Code>
  <Message>Access Denied</Message>
  <RequestId>4442587FB7D0A2F9</RequestId>
  <HostId>...</HostId>
</Error>
```