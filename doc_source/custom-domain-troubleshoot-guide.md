# Troubleshooting custom domains<a name="custom-domain-troubleshoot-guide"></a>

If you encounter issues when adding a custom domain to an app in the AWS Amplify Console, consult the following topics in this section\.
+  [Understanding DNS terminology and concepts](#understanding-dns-terminology-and-concepts.title) 
+  [How do I verify that my CNAME resolves?](#how-do-i-verify-that-my-cname-resolves.title) 
+  [My domain hosted with a third\-party is stuck in the Pending Verification state](#my-domain-hosted-with-a-third-party-is-stuck-in-the-pending-verification-state.title) 
+  [My domain hosted with Amazon Route 53 is stuck in the Pending Verification state](#my-domain-hosted-with-amazon-route-53-is-stuck-in-the-pending-verification-state.title) 
+  [I get a CNAMEAlreadyExistsException error](#i-get-a-cnamealreadyexistsexception-error.title) 

## Understanding DNS terminology and concepts<a name="understanding-dns-terminology-and-concepts"></a>

If you are unfamiliar with the terms and concepts associated with Domain Name System \(DNS\), the following topics can help you understand the procedures for adding custom domains\.

### DNS terminology<a name="dns-terminology"></a>

Understanding the following list of terms will help you when following the procedures for adding custom domains\.

**CNAME**  
A CNAME \(Canonical Record Name\) is a type of DNS record that masks the domain for a set of webpages and makes them appear as though they are located elsewhere\. A CNAME points a subdomain to a fully qualified domain name \(FQDN\)\. For example, you can create a new CNAME record to map the subdomain *www\.example\.com*, where *www* is the subdomain, to the FQDN domain *branch\-name\.d1m7bkiki6tdw1\.cloudfront\.net* assigned to your app in the Amplify Console\.

**ANAME**  
An ANAME record can also be referred to as an A record\. It is like a CNAME record, but at the root level\. An ANAME will point the root of your domain to a FQDN\. That FQDN will point to an IP address\.

**Nameserver**  
A Nameserver is a server on the internet specialized in handling queries regarding the location of a domain name’s various services\. If you have your domain setup in Amazon Route 53, you will have a list of nameservers assigned to your domain\.

**NS record**  
An NS record points to nameservers that lookup your domain details\.

### DNS verification<a name="dns-verification"></a>

DNS stands for Domain Name System, and is like a phone book that translates human\-readable domain names into computer\-friendly IP addresses\. When you type *https://google\.com* into a browser, a lookup is done in the DNS provider to find the IP Address of the server that hosts the website\.

DNS providers contain records of domains and their corresponding IP Addresses\. The most commonly used DNS records are CNAME, ANAME, and NS records\.

The Amplify Console uses a CNAME record to verify that you own your custom domain\. If you host your domain with Route 53, verification is done automatically on your behalf\. However, if you host your domain with a third\-party provider such as GoDaddy or Google, you have to manually update your domain’s DNS settings and add a new CNAME record provided by the Amplify Console\.

### Amplify Console custom domain setup<a name="amplify-console-custom-domain-setup"></a>

When you add a custom domain in the Amplify Console, there are a number of steps which need to happen before you can view your app via your custom domain\. The following grapic shows the order of the steps that the Amplify Console performs from SSl creation, to SSL configuration and verification, to domain activation\.

![\[Workflow diagram of the steps in the Amplify Console domain activation process.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/1555951758569-803.png)

The following list describes each step in the domain set up process in more detail\.

**SSL create**  
The AWS Amplify Console is issuing an SSL certificate for setting up a secure custom domain\.

**SSL configuration and verification**  
Before issuing an SSL certificate, the Amplify Console must verify that you are the owner of the domain\. For domains managed by Amazon Route 53, Amplify will automatically update the DNS verification record\. For domains managed outside of Route 53, you will need to manually add the DNS verification record displayed by the Amplify console into your domain with a third\-party DNS provider\.

**Domain activation**  
The domain is successfully verified\. For domains managed outside of Route 53, you will need to manually add the CNAME records displayed by the Amplify console into your domain with a third\-party DNS provider\.

## How do I verify that my CNAME resolves?<a name="how-do-i-verify-that-my-cname-resolves"></a>

1. After you update your DNS records with your third\-party domain provider, you can use a tool such as [dig](https://en.wikipedia.org/wiki/Dig_(command)) or a free website such as [https://www\.whatsmydns\.net/](https://www.whatsmydns.net/) to verify that your CNAME record is resolving correctly\. The following screenshot demonstrates how to use whatsmydns\.net to check your CNAME record for the domain *www\.example\.com*\.  
![\[Screenshot of whatsmydns.net where you enter the name of a website to check.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-troubleshooting-whatsmydns-1Update.png)

1. Choose **Search**, and *whatsmydns\.net* displays the results for your CNAME\. The following screenshot is an example of a list of results that verify that the CNAME resolves correctly to a cloudfront\.net URL\.  
![\[Screenshot of whatsmydns.net that displays the results of a resolving CNAME.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-troubleshooting-whatsmydns-2Update.png)

## My domain hosted with a third\-party is stuck in the Pending Verification state<a name="my-domain-hosted-with-a-third-party-is-stuck-in-the-pending-verification-state"></a>

1. If your custom domain is stuck in the *Pending Verification* state, verify that your CNAME records are resolving\. See the previous troubleshooting topic, How do I verify that my CNAME resolves, for instructions on performing this task\.

1. If your CNAME records are not resolving, confirm that the CNAME entry exists in your DNS settings with your domain provider\.
**Important**  
 It is important to update your CNAME records as soon as you create your custom domain\. Once your app is created in the Amplify Console, your CNAME record is checked every few minutes to determine if it resolves\. If it doesn’t resolve after an hour, the check is made every few hours, which can lead to a delay in your domain being ready to use\. If you added or updated your CNAME records a few hours after you created your app, this is the most likely cause for your app to get stuck in the pending verification state\.

1. If you have verified that the CNAME record exists, then there may be an issue with your DNS provider\. You can either contact the DNS provider to diagnose why the DNS verification CNAME is not resolving or you can migrate your DNS to Route 53\. For more information, see [Making Amazon Route 53 the DNS service for an existing domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html)\.

## My domain hosted with Amazon Route 53 is stuck in the Pending Verification state<a name="my-domain-hosted-with-amazon-route-53-is-stuck-in-the-pending-verification-state"></a>

If you transferred your domain to Amazon Route 53, it is possible that your domain has different nameservers than those issued by the Amplify Console when your app was created\. Perform the following steps to diagnose the cause of the error\.

1. Log in to the [Amazon Route 53 console](https://console.aws.amazon.com/route53/home), choose **Hosted Zones** from the Navigation pane, and select the name of the domain you are connecting\. Record the nameserver values from the Hosted Zone Details section\. You will need these values in the next step\. The following screenshot of the Route 53 console displays the location of the nameserver values in the bottom right corner\.  
![\[Screenshot of the Hosted Zone Details section of the Route 53 console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/1555952748759-111.png)

1. Choose **Registered domains** from the Navigation pane\. Verify that the nameservers displayed on the Registered domains section match the nameserver values that you recorded in the previous step from the Hosted Zone Details section\. If they do not match, edit the nameserver values to match the values in your Hosted Zone\. The following screenshot of the Route 53 console displays the location of the nameserver values on the right side\.  
![\[Screenshot of the Registered domains section of the Route 53 console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/1555952748759-607.png)

1. If this does not resolve the issue, see [GitHub Issues](https://github.com/aws-amplify/amplify-console/issues) and open a new issue if it doesn’t already exist\.

## I get a CNAMEAlreadyExistsException error<a name="i-get-a-cnamealreadyexistsexception-error"></a>

If you get a *CNAMEAlreadyExistsException* error, this means that one of the host names that you tried to connect \(a subdomain, or the apex domain\) is already deployed to another Amazon CloudFront distribution\. Perform the following steps to diagnose the cause of the error\.

1. Check the [Amazon CloudFront console](https://console.aws.amazon.com/cloudfront/home?#) to see if you have this domain deployed to any other distribution\. A single CNAME record can be attached to one CloudFront distribution at a time\. If you have previously deployed the domain with Cloudfront, make sure to remove it from the **Alternate Domain Names (CNAMEs)** field under the **General** tab **in the Cloudfront console**.

1. Check to see whether this domain is connected to a different Amplify app that you own\. If so, make sure you are not trying to reuse one of the hostnames\. If you are using *www\.example\.com* on another app, you cannot use *www\.example\.com* with the app that you are currently connecting\. You can use other subdomains, such as *blog\.example\.com*\.

1. If this domain was successfully connected to another app and then deleted within the last hour, try again after at least one hour has passed\. If you still see this exception after 6 hours, see [GitHub Issues](https://github.com/aws-amplify/amplify-console/issues) and open a new issue if it doesn’t already exist\.
