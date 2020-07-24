# Add a custom domain managed by GoDaddy<a name="to-add-a-custom-domain-managed-by-godaddy"></a>

**To add a custom domain managed by GoDaddy**

1. Follow steps one through six of the procedure [Add a custom domain managed by a third\-party DNS provider](to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md)\.

1. Log in to your GoDaddy account\.

1. In your list of domains, find the domain to add and choose **DNS**\. GoDaddy displays a list of records for your domain\. You need to add two new CNAME records\.

1. Create the first CNAME record to point your subdomains to the Amplify domain\.

   1. For **Host**, enter only the subdomain\. For example, if your subdomain is **www\.example\.com**, enter **www** for **Host**\.

   1. For **Points to**, look at your DNS records in the Amplify Console and then enter the value\. If the Amplify Console displays the domain for your app as **xxxxxxxxxxxxxx\.cloudfront\.net**, enter **xxxxxxxxxxxxxx\.cloudfront\.net** for **Points to**\.   
![\[Screenshot of the section for creating a CNAME record on the GoDaddy website.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-godaddy-2Update.png)

1. Create the second CNAME record to point to the AWS Certificate Manager \(ACM\) validation server\. A single validated ACM generates an SSL certificate for your domain\.

   1. For **Host**, enter the subdomain\.

      For example, if the DNS record in the Amplify Console for verifying ownership of your subdomain is **\_c3e2d7eaf1e656b73f46cd6980fdc0e\.example\.com**, enter only **\_c3e2d7eaf1e656b73f46cd6980fdc0e** for **Host**\.

   1. For **Points to**, enter the ACM validation certificate\.

       For example, if the validation server is **\_cjhwou20vhu2exampleuw20vuyb2ovb9\.j9s73ucn9vy\.acm\-validations\.aws **, enter **\_cjhwou20vhu2exampleuw20vuyb2ovb9\.j9s73ucn9vy\.acm\-validations\.aws** for **Points to**\.  
![\[Screenshot of the section for creating a CNAME record on the GoDaddy website.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-godaddy-3.png)

1. This step is not required for subdomains\. GoDaddy doesn’t support ANAME/ALIAS records\. For DNS providers that do not have ANAME/ALIAS support, we strongly recommend migrating your DNS to Amazon Route 53\. For more information, see [Configuring Amazon Route 53 as your DNS service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html)\.

   If you want to keep GoDaddy as your provider and update the root domain, add **Forwarding** and set up a domain forward:

   1. Scroll down to the bottom of the **DNS Management** page to find the **Forwarding** box\.

   1. For **Forward to**, choose **http://**, and then enter the name of your subdomain to foward to \(for example, **www\.example\.com**\)\.

   1. For **Forward Type**, choose **Temporary \(302\)**\. 

   1. For **Settings**, choose **Forward only**\.  
![\[Screenshot of the Forwarding pane on GoDaddy website.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-godaddy-4Update.png)