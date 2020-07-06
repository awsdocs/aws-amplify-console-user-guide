# Set up automatic subdomains for a Amazon Route 53 custom domain<a name="to-set-up-automatic-subdomains-for-a-Route-53-custom-domain"></a>

After an app is connected to a custom domain in Route 53, Amplify Console enables you to automatically create subdomains for newly connected branches\. For example, if you connect your **dev** branch, Amplify can automatically create **dev\.exampledomain\.com**\. When you delete a branch, any associated subdomains are automatically deleted\. 

**To set up automatic subdomain creation for newly connected branches**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose an app that is connected to a custom domain managed in Route 53\.

1. In the navigation pane, choose **App Settings**, and then choose **Domain management**\.

1. On the **Domain management** page, choose **Edit domain**\.

1. Select the **Sub\-domain auto\-detection** check box on the bottom left side\.

## Web previews with subdomains<a name="web-previews-on-subdomains"></a>

After you enable **Sub\-domain auto\-detection** using the preceding procedures, your app’s pull request web previews will also be accessible with automatically created subdomains\. When a pull request is closed, the associated branch and subdomain are automatically deleted\. For more information on setting up web previews for pull requests, see [Web previews](pr-previews.md)\.