# To add a custom domain managed by a third\-party DNS provider<a name="to-add-a-custom-domain-managed-by-a-third-party-dns-provider"></a>

If you are not using Amazon Route 53 to manage your domain, you can add a custom domain managed by a third\-party DNS provider to your app deployed in the Amplify Console\. If you are using GoDaddy or Google Domains, see [To add a custom domain managed by GoDaddy](to-add-a-custom-domain-managed-by-godaddy.md) or [To add a custom domain managed by Google Domains](to-add-a-custom-domain-managed-by-google-domains.md) for procedures specific to these providers\.

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to add a custom domain to\.

1. In the Navigation pane, choose **App Settings**, **Domain management**, and then in the Domain management page, choose **Add domain**\.

1. For **Domain**, enter the name of your root domain\. For example, if the name of your domain is *https://example\.com*, enter *example\.com* for **Domain** and then choose **Configure domain**\. If you do not already own the domain and it is available, you can purchase the domain in [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)\.

1. By default, the Amplify Console automatically creates two subdomain entries for your domain\. For example, if your domain name is *example\.com*, you will see the subdomains *https://www\.example\.com* and *https://example\.com* with a redirect set up from the *www* subdomain to the root domain\. You can change this by choosing **Rewrites and redirects** from the Navigation pane\. You can modify the default configuration to add subdomains only\. For more information, see [To add a subdomain only](to-manage-subdomains.md#to-add-a-subdomain-only)\. Choose **Save** after configuring your domain\. The following screenshot shows the Domain management configuration for the *example\.com* domain\.  
![\[Screenshot of the Domain management section in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-thirdparty-1Update.png)

1. On the **Actions** menu, choose **View DNS records**\. Use the DNS records displayed in the Amplify console to update your DNS records with your third\-party domain provider\. The following screenshot is an example of the DNS records for an app\.  
![\[Screenshot of the Update DNS records section in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-thirdpartyDNS-1.png)

1. Log in to your account with your DNS provider and locate the DNS management settings for your domain\.

1. Configure a CNAME to point to the AWS validation server\. For example, if the validation server is *\_68126cb4e8b7ab90c515ea3edb5be60d\.hkvuiqjoua\.acm\-validations\.aws*, enter *\_68126cb4e8b7ab90c515ea3edb5be60d\.hkvuiqjoua\.acm\-validations\.aws*\. The Amplify Console uses this information to verify ownership of your domain and generate an SSL certificate for your domain\. Once the Amplify Console validates ownership of your domain, all traffic will be served using HTTPS/2\.
**Important**  
 It is important that you perform this step soon after adding your custom domain in the Amplify Console\. The Amazon Certificate Manager \(ACM\) will immediately start attempting to verify ownership\. Over time, the checks become less frequent\. If you add or update your CNAME records a few hours after you create your app, this can cause your app to get stuck in the pending verification state\.

1. Configure a second CNAME record to point to your subdomains for example, *https://\*\.example\.com*, to the Amplify domain\. If you have production traffic, we recommended you update this CNAME record after your domain status shows as AVAILABLE in the Amplify console\.

1. Configure the ANAME/ALIAS record to point to the root domain, for example *https://example\.com*, to your amplifyapp domain\. An ANAME record points the root of your domain to a hostname\. If you have production traffic, we recommended that you update your ANAME record after your domain status shows as AVAILABLE in the console\. For DNS providers that do not have ANAME/ALIAS support, we strongly recommend migrating your DNS to Route 53\. For more information, see [Configuring Amazon Route 53 as your DNS service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html)\.

**Note**  
 Verification of domain ownership and DNS propagation for third\-party domains can take up to 48 hours\. For help resolving errors that occur, see [Troubleshooting custom domains](troubleshooting-custom-domains.md)\. 