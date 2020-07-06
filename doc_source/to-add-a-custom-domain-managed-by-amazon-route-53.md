# Add a custom domain managed by Amazon Route 53<a name="to-add-a-custom-domain-managed-by-amazon-route-53"></a>

**To add a custom domain managed by Amazon Route 53**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to connect to a custom domain\.

1. In the navigation pane, choose **App Settings**, **Domain management**\.

1.  On the **Domain management** page, choose **Add domain**\.  
![\[Screenshot of the Domain management section in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomain-1.png)

1. For **Domain**, enter your root domain, choose the domain you want to use when it appears in the list, and then choose **Configure Domain**\.

   As you start typing, any root domains that you already manage in Route 53 appear in the list\. For example, if the name of your domain is **https://example\.com**, enter **example\.com** for **Domain**\.  
![\[Screenshot of the Domain management section in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomain-2.png)

1. By default, the Amplify console automatically creates two subdomain entries for your domain\. For example, if your domain name is **example\.com**, you will see the subdomains **https://www\.example\.com** and **https://example\.com** with a redirect set up from the root domain to the **www** subdomain\.

   \(Optional\) You can modify the default configuration if you want to add subdomains only\. To change the default configuration, choose **Rewrites and redirects** from the navigation pane, configure your domain, and then choose **Save**\.   
![\[Screenshot of the Add domain section in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomain-configureUpdate.png)
**Note**  
 It can take up to 24 hours for the DNS to propagate and to issue the SSL certificate\. For help with resolving errors that occur, see [Troubleshooting custom domains](custom-domain-troubleshoot-guide.md)\.