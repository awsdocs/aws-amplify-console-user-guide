# Troubleshooting custom domains<a name="custom-domain-troubleshoot-guide"></a>

If you encounter issues when adding a custom domain to an app in the AWS Amplify Console, consult the following topics in this section\.

**Topics**
+ [How do I verify that my CNAME resolves?](#how-do-i-verify-that-my-cname-resolves)
+ [My domain hosted with a third\-party is stuck in the Pending Verification state](#my-domain-hosted-with-a-third-party-is-stuck-in-the-pending-verification-state)
+ [My domain hosted with Amazon Route 53 is stuck in the Pending Verification state](#my-domain-hosted-with-amazon-route-53-is-stuck-in-the-pending-verification-state)
+ [I get a CNAMEAlreadyExistsException error](#i-get-a-cnamealreadyexistsexception-error)

## How do I verify that my CNAME resolves?<a name="how-do-i-verify-that-my-cname-resolves"></a>

1. After you update your DNS records with your third\-party domain provider, you can use a tool such as [dig](https://en.wikipedia.org/wiki/Dig_(command)) or a free website such as [https://www\.whatsmydns\.net/](https://www.whatsmydns.net/) to verify that your CNAME record is resolving correctly\. The following screenshot demonstrates how to use whatsmydns\.net to check your CNAME record for the domain **www\.example\.com**\.  
![\[Screenshot of whatsmydns.net where you enter the name of a website to check.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-troubleshooting-whatsmydns-1Update.png)

1. Choose **Search**, and **whatsmydns\.net** displays the results for your CNAME\. The following screenshot is an example of a list of results that verify that the CNAME resolves correctly to a cloudfront\.net URL\.  
![\[Screenshot of whatsmydns.net that displays the results of a resolving CNAME.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-troubleshooting-whatsmydns-2Update.png)

## My domain hosted with a third\-party is stuck in the Pending Verification state<a name="my-domain-hosted-with-a-third-party-is-stuck-in-the-pending-verification-state"></a>

1. If your custom domain is stuck in the **Pending Verification** state, verify that your CNAME records are resolving\. See the previous troubleshooting topic, How do I verify that my CNAME resolves, for instructions on performing this task\.

1. If your CNAME records are not resolving, confirm that the CNAME entry exists in your DNS settings with your domain provider\.
**Important**  
 It is important to update your CNAME records as soon as you create your custom domain\. After your app is created in the Amplify Console, your CNAME record is checked every few minutes to determine if it resolves\. If it doesn’t resolve after an hour, the check is made every few hours, which can lead to a delay in your domain being ready to use\. If you added or updated your CNAME records a few hours after you created your app, this is the most likely cause for your app to get stuck in the **Pending Verification** state\.

1. If you have verified that the CNAME record exists, then there may be an issue with your DNS provider\. You can either contact the DNS provider to diagnose why the DNS verification CNAME is not resolving or you can migrate your DNS to Route 53\. For more information, see [Making Amazon Route 53 the DNS service for an existing domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html)\.

## My domain hosted with Amazon Route 53 is stuck in the Pending Verification state<a name="my-domain-hosted-with-amazon-route-53-is-stuck-in-the-pending-verification-state"></a>

If you transferred your domain to Amazon Route 53, it is possible that your domain has different name servers than those issued by the Amplify Console when your app was created\. Perform the following steps to diagnose the cause of the error\.

1. Sign in to the [Amazon Route 53 console](https://console.aws.amazon.com/route53/home)

1. In the navigation pane, choose **Hosted Zones** and then choose the name of the domain you are connecting\.

1. Record the name server values from the **Hosted Zone Details** section\. You need these values to complete the next step\. The following screenshot of the Route 53 console displays the location of the name server values in the lower\-right corner\.  
![\[Screenshot of the Hosted Zone Details section of the Route 53 console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/1555952748759-111.png)

1. In the navigation pane, choose **Registered domains**\. Verify that the name servers displayed on the **Registered domains** section match the name server values that you recorded in the previous step from the **Hosted Zone** Details section\. If they do not match, edit the name server values to match the values in your **Hosted Zone**\. The following screenshot of the Route 53 console displays the location of the name server values on the right side\.  
![\[Screenshot of the Registered domains section of the Route 53 console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/1555952748759-607.png)

1. If this doesn't resolve the issue, see [GitHub Issues](https://github.com/aws-amplify/amplify-console/issues) and open a new issue if it doesn’t already exist\.

## I get a CNAMEAlreadyExistsException error<a name="i-get-a-cnamealreadyexistsexception-error"></a>

If you get a **CNAMEAlreadyExistsException** error, this means that one of the host names that you tried to connect \(a subdomain, or the apex domain\) is already deployed to another Amazon CloudFront distribution\. Perform the following steps to diagnose the cause of the error\.

1. Sign in to the [Amazon CloudFront console](https://console.aws.amazon.com/cloudfront/home?#) and verify that you don't have this domain deployed to any other distribution\. A single CNAME record can be attached to one CloudFront distribution at a time\.

1. If you previously deployed the domain to a CloudFront distribution you must remove it\.

   1. Choose **Distributions** on the left navigation menu\.

   1. Select the checkbox next to the name of the distribution to edit, then choose **Distribution Settings**\.

   1. Choose the **General** tab, and then choose **Edit**\.

   1. Remove the domain name from **Alternate Domain Names \(CNAMEs\)**\. Then choose, **Yes, Edit** to save your change\.

1. Check to see whether this domain is connected to a different Amplify app that you own\. If so, make sure you are not trying to reuse one of the hostnames\. If you are using **www\.example\.com** for another app, you cannot use **www\.example\.com** with the app that you are currently connecting\. You can use other subdomains, such as **blog\.example\.com**\.

1. If this domain was successfully connected to another app and then deleted within the last hour, try again after at least one hour has passed\. If you still see this exception after 6 hours, see [GitHub Issues](https://github.com/aws-amplify/amplify-console/issues) and open a new issue if it doesn’t already exist\.