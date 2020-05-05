# To add a custom domain managed by Google Domains<a name="to-add-a-custom-domain-managed-by-google-domains"></a>

1. Follow steps one through six of the procedures [To add a custom domain managed by a third\-party DNS provider](to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md)\.

1. Log in to your account at [https://domains\.google\.com](https://domains.google.com) and choose **DNS** in the left navigation pane\.

1. Scroll down the page to **Custom resource records** where you will add two new CNAME records\.

1. Create the first CNAME record to point all subdomains to the Amplify domain\. For **Name**, enter only the subdomain name\. For example, if your subdomain is *www\.example\.com*, enter *www* for **Name**\. The value that you enter for **Data** is available in the Amplify console\. If the Amplify console displays the domain for your app as *xxxxxxxxxxxxxx\.cloudfront\.net*, then enter *xxxxxxxxxxxxx\.cloudfront\.net* for **Name**\.

1. Create the second CNAME record to point to the Amazon Certificate Manager \(ACM\) validation server\. A single validated ACM generates an SSL certificate for your domain\. For **Name**, enter the subdomain and for **Data**, enter the ACM validation certificate\. For example, if the DNS record in the Amplify console for verifying ownership of your subdomain is *\_c3e2d7eaf1e656b73f46cd6980fdc0e\.example\.com*, enter only *\_c3e2d7eaf1e656b73f46cd6980fdc0e* for **Name**\. If the validation server is *\_68126cb4e8b7ab90c515ea3edb5be60d\.hkvuiqjoua\.acm\-validations\.aws\.*, enter *\_68126cb4e8b7ab90c515ea3edb5be60d\.hkvuiqjoua\.acm\-validations\.aws\.* for **Data**\. The following screenshot shows the correctly configured CNAME records\.  
![\[Screenshot of the Custom resource records section on the Google Domains website.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-google-2Update.png)

1. Google Domains doesn’t support ANAME/ALIAS records\. For DNS providers that do not have ANAME/ALIAS support, we strongly recommend migrating your DNS to Amazon Route 53\. For more information, see [Configuring Amazon Route 53 as your DNS service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html)\. If you want to keep Google Domains as your provider and update the root domain, set up a subdomain forward\. Locate the **Synthetic records** pane\. For **Subdomain**, enter the **@** symbol and then choose **Forward path**\. For **Destination URL**, enter your root domain\. The following screenshot shows a Synthetic record configuration for a subdomain forward for the root domain *example\.com*\.  
![\[Screenshot of the Synthetic records section on the Google Domains website.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-google-3Update.png)

**Note**  
 Updates to your DNS settings for a Google domain can take up to 48 hours to take effect\. For help with resolving errors that occur, see [Troubleshooting custom domains](troubleshooting-custom-domains.md)\. 