# Add a custom domain managed by Google Domains<a name="to-add-a-custom-domain-managed-by-google-domains"></a>

**To add a custom domain managed by Google Domains**

1. Follow steps one through six of the procedure [To add a custom domain managed by a third\-party DNS provider](to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md)\.

1. Log in to your account at [https://domains\.google\.com](https://domains.google.com) and choose **DNS** in the left navigation pane\.

1. Scroll down the page to **Custom resource records** where you need to add two new CNAME records\.

1. Create the first CNAME record to point all subdomains to the Amplify domain as follows:

   1. For **Name**, enter only the subdomain name\. For example, if your subdomain is **www\.example\.com**, enter **www** for **Name**\.

   1. For **Data**, enter the value that's available in the Amplify Console\. 

      If the Amplify Console displays the domain for your app as **xxxxxxxxxxxxxx\.cloudfront\.net**, enter **xxxxxxxxxxxxx\.cloudfront\.net** for **Data**\.

1. Create the second CNAME record to point to the AWS Certificate Manager \(ACM\) validation server\. A single validated ACM generates an SSL certificate for your domain\. 

   1. For **Name**, enter the subdomain\.

      For example, if the DNS record in the Amplify Console for verifying ownership of your subdomain is **\_c3e2d7eaf1e656b73f46cd6980fdc0e\.example\.com**, enter only **\_c3e2d7eaf1e656b73f46cd6980fdc0e** for **Name**\. 

   1. For **Data**, enter the ACM validation certificate\.

      For example, if the validation server is **\_68126cb4e8b7ab90c515ea3edb5be60d\.hkvuiqjoua\.acm\-validations\.aws\.**, enter **\_68126cb4e8b7ab90c515ea3edb5be60d\.hkvuiqjoua\.acm\-validations\.aws\.** for **Data**\.   
![\[Screenshot of the Custom resource records section on the Google Domains website.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-google-2Update.png)

1. Google Domains doesn’t support ANAME/ALIAS records\. For DNS providers that don't have ANAME/ALIAS support, we strongly recommend migrating your DNS to Amazon Route 53\. For more information, see [Configuring Amazon Route 53 as your DNS service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html)\. If you want to keep Google Domains as your provider and update the root domain, set up a subdomain forward\. Locate the **Synthetic records** pane\. For **Subdomain**, enter the **@** symbol to specify the root domain\. For **Destination URL**, enter your subdomain to forward to\.  
![\[Screenshot of the Synthetic records section on the Google Domains website.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-google-3Update.png)

**Note**  
 Updates to your DNS settings for a Google domain can take up to 48 hours to take effect\. For help with resolving errors that occur, see [Troubleshooting custom domains](custom-domain-troubleshoot-guide.md)\. 