# Manual Deploys<a name="manual-deploys"></a>

Manual deploys allows you to publish your web app to the Amplify Console without connecting a Git provider\. You can choose to drag and drop a folder from your desktop, or reference an Amazon S3 bucket or external URL\.

## Drag and Drop<a name="drag-and-drop"></a>

Drag and drop a folder from your desktop to host your site in seconds\. Log in to the [Amplify Console](https://console.aws.amazon.com/amplify/home) and choose **Deploy without a Git provider**\. Give your app a name, and a name for the environment \(e\.g\. development or production\)\. Drag and drop files from your desktop to publish your web app\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/manual-deploys.gif)

## Amazon S3 or any URL<a name="amazon-s3-or-any-url"></a>

Reference assets that are uploaded to an Amazon S3 bucket, or provide a public URL to files stored elswhere\.

For Amazon S3, choose the bucket and zip file to deploy your site\. You can also set up AWS Lambda triggers so your site is updated everytime new assets are uploaded\. [This blog post](http://aws.amazon.com/blogs/mobile/deploy-files-s3-dropbox-amplify-console/) walks through setting up a Lambda trigger to automatically deploy changes to Amplify on any updates to a bucket\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/manual-deploys-s3.png)

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