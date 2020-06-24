# Add a custom domain managed by a third\-party DNS provider<a name="to-add-a-custom-domain-managed-by-a-third-party-dns-provider"></a>

If you are not using Amazon Route 53 to manage your domain, you can add a custom domain managed by a third\-party DNS provider to your app deployed in the Amplify Console\.

If you are using GoDaddy or Google Domains, see [Add a custom domain managed by GoDaddy](to-add-a-custom-domain-managed-by-godaddy.md) or [Add a custom domain managed by Google Domains](to-add-a-custom-domain-managed-by-google-domains.md) for procedures specific to these providers\.

**To add a custom domain managed by a third\-party DNS provider**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to add a custom domain to\.

1. In the navigation pane, choose **App Settings**, **Domain management**\.

1. On the Domain management page, choose **Add domain**\.

1. For **Domain**, enter the name of your root domain, and then choose **Configure domain**\. For example, if the name of your domain is **https://example\.com**, enter **example\.com**\.

    If you don't already own the domain and it is available, you can purchase the domain in [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)\.

1. By default, the Amplify Console automatically creates two subdomain entries for your domain\. For example, if your domain name is **example\.com**, you will see the subdomains **https://www\.example\.com** and **https://example\.com** with a redirect set up from the root domain to the **www** subdomain\. 

   \(Optional\) You can modify the default configuration if you want to add subdomains only\. To change the default configuration, choose **Rewrites and redirects** from the navigation pane, configure your domain, and then choose **Save**\.  
![\[Screenshot of the Domain management section in the Amplify Console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-thirdparty-1Update.png)

1. Do one of the following: 
   + If you're using GoDaddy, go to [Add a custom domain managed by GoDaddy](to-add-a-custom-domain-managed-by-godaddy.md)\.
   + If you're using Google Domains, go to [Add a custom domain managed by Google Domains](to-add-a-custom-domain-managed-by-google-domains.md)\.
   + If you're using a different third\-party DNS provider, go to the next step in this procedure\. 

1. On the **Actions** menu, choose **View DNS records**\. Use the DNS records displayed in the Amplify Console to update your DNS records with your third\-party domain provider\.  
![\[Screenshot of the Update DNS records section in the Amplify Console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-thirdpartyDNS-1.png)

1. Go to your DNS provider's website, log in to your account, and locate the DNS management settings for your domain\.

1. Configure a CNAME to point to the AWS validation server\. For example, if the validation server is **\_cjhwou20vhu2exampleuw20vuyb2ovb9\.j9s73ucn9vy\.acm\-validations\.aws**, enter **\_cjhwou20vhu2exampleuw20vuyb2ovb9\.j9s73ucn9vy\.acm\-validations\.aws**\. The Amplify Console uses this information to verify ownership of your domain and generate an SSL certificate for your domain\. Once the Amplify Console validates ownership of your domain, all traffic will be served using HTTPS/2\.
**Important**  
 It is important that you perform this step soon after adding your custom domain in the Amplify Console\. The AWS Certificate Manager \(ACM\) immediately starts attempting to verify ownership\. Over time, the checks become less frequent\. If you add or update your CNAME records a few hours after you create your app, this can cause your app to get stuck in the pending verification state\.

1. Configure a second CNAME record \(for example, **https://\*\.example\.com**\), to point your subdomains to the Amplify domain\. If you have production traffic, we recommended you update this CNAME record after your domain status shows as **AVAILABLE** in the Amplify Console\.

1. Configure the ANAME/ALIAS record to point to the root domain of your amplifyapp domain \(for example **https://example\.com**\)\. An ANAME record points the root of your domain to a hostname\. If you have production traffic, we recommended that you update your ANAME record after your domain status shows as **AVAILABLE** in the console\. For DNS providers that don't have ANAME/ALIAS support, we strongly recommend migrating your DNS to Route 53\. For more information, see [Configuring Amazon Route 53 as your DNS service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html)\.

**Note**  
 Verification of domain ownership and DNS propagation for third\-party domains can take up to 48 hours\. For help resolving errors that occur, see [Troubleshooting custom domains](custom-domain-troubleshoot-guide.md)\. 