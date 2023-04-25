# Manual deploys<a name="manual-deploys"></a>

Manual deploys allows you to publish your web app with Amplify Hosting without connecting a Git provider\. You can drag and drop a folder from your desktop and host your site in seconds\. Alternatively, you can reference assets in an Amazon S3 bucket or specify a public URL to the location where your files are stored\.

For Amazon S3, you can also set up AWS Lambda triggers to update your site each time new assets are uploaded\. See the [Deploy files stored on Amazon S3, Dropbox, or your Desktop to the AWS Amplify console](http://aws.amazon.com/blogs/mobile/deploy-files-s3-dropbox-amplify-console/) blog post for more details about setting up this scenario\.

Amplify Hosting does not support manual deploys for server\-side rendered \(SSR\) apps\. For more information, see [Deploy server\-side rendered apps with Amplify Hosting](server-side-rendering-amplify.md)\.

## Drag and drop manual deploy<a name="drag-and-drop"></a>

**To manually deploy an app using drag and drop**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. How you get to the **Host your web app** page depends on whether you are starting from the Amplify home page or the **All apps** page\.
   + From the Amplify home page

     1. Choose **Get started**\.

     1. In the **Deliver** section, choose **Get started**\.
   + From the **All apps** page

     1. In the upper right corner, choose **New app**, **Host web app**

1. On the **Host your web app** page, choose **Deploy without Git provider**\. Then, choose **Continue**\.

1. In the **Start a manual deployment** section, for **App name**, enter the name of your app\.

1. For **Environment name**, enter a meaningful name for the environment, such as **development** or **production**\.

1. For **Method**, choose **Drag and drop**\.

1. Either drag and drop files from your desktop onto the drop zone or use **Choose files** to select the files from your computer\. The files that you drag and drop or select can be a folder or a zip file that contains the root of your site\.

1. Choose **Save and deploy**\.

## Amazon S3 or URL manual deploy<a name="amazon-s3-or-any-url"></a>

**To manually deploy an app from Amazon S3 or a public URL**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. At the top of the page, choose **Get started**\.

1. In the **Deliver** section, choose **Get started**\.

1. On the **Host your web app** page, choose **Deploy without Git provider**\. Then, choose **Continue**\.

1. In the **Start a manual deployment** section, for **App name**, enter the name of your app\.

1. For **Environment name**, enter a meaningful name for the environment, such as **development** or **production**\.

1. For **Method**, choose either **Amazon S3** or **Any URL**\.

1. The procedure for uploading your files depends on the upload method\.
   + Amazon S3

     1. For **Bucket**, select the name of the Amazon S3 bucket from the list\. Access control lists \(ACLs\) must be enabled for the bucket you select\. For more information, see [Troubleshooting Amazon S3 bucket access](#troubleshooting-s3-bucket-access)\.

     1. For **Zip file**, select the name of the zip file to deploy\.
   + Any URL

     1. For **Resource URL**, enter the URL to the zipped file to deploy\.

1. Choose **Save and deploy**\.

**Note**  
When you create the zip folder, make sure you zip the contents of your build output and not the top level folder\. For example, if your build output generates a folder named “build” or “public”, first navigate into that folder, select all of the contents, and zip it from there\. If you do not do this, you will see an “Access Denied” error because the site's root directory will not be initialized properly\.

### Troubleshooting Amazon S3 bucket access<a name="troubleshooting-s3-bucket-access"></a>

When you create an Amazon S3 bucket, you use its Amazon S3 Object Ownership setting to control whether access control lists \(ACLs\) are enabled or disabled for the bucket\. To manually deploy an app to Amplify from an Amazon S3 bucket, ACLs must be enabled on the bucket\.

If you get an `AccessControlList` error when you deploy from an Amazon S3 bucket, the bucket was created with ACLs disabled and you must enable them in the Amazon S3 console\. For instructions, see [Setting Object Ownership on an existing bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-existing-bucket.html?icmpid=docs_s3_hp-edit-object-ownership-page) in the *Amazon Simple Storage Service User Guide*\.