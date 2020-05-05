# To manage subdomains<a name="to-manage-subdomains"></a>

A subdomain is the part of your URL that appears before your domain name\. For example, *www* is the subdomain of *www\.amazon\.com* and *aws* is the subdomain of *aws\.amazon\.com*\. If you already have a production website, you might want to only connect a subdomain\. Subdomains can also be multi\-level, for example *beta\.alpha\.example\.com* has the multi\-level subdomain *beta\.alpha*\.

## To add a subdomain only<a name="to-add-a-subdomain-only"></a>

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to add a subdomain only to\.

1. In the Navigation pane, choose **App Settings**, **Domain management**, and then in the Domain management page choose **Add domain**\.

1. For **Domain**, enter the name of your root domain\. For example, if the name of your domain is *https://example\.com*, enter *example\.com* for **Domain** and then choose **Configure domain**\.

1. Choose **Exclude root** and modify the name of the subdomain\. The following screenshot demonstrates how to modify the domain *example\.com* to only add the subdomain *alpha*\.  
![\[Screenshot of the Add domain section in the Amplify console configured to add a subdomain.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomain-configure-2Update.png)

## To add a multi\-level subdomain<a name="to-add-a-multi-level-subdomain"></a>

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to add a multi\-level subdomain to\.

1. In the Navigation pane, choose **App Settings**, **Domain management**, and then in the Domain management page choose **Add domain**\.

1. For **Domain**, enter the name of a domain with a subdomain\. For example, *alpha\.example\.com*\. Choose **Exclude root**, and modify the subdomain to add a new level, for example *beta*\. The following screenshot demonstrates how to modify *alpha\.example\.com* to add the multilevel subdomain *beta\.alpha\.example\.com*\.  
![\[Screenshot of the Add domain section in the Amplify console configured to add a multi-level subdomain.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomain-configure-3Update.png)

## To add or edit a subdomain<a name="to-add-or-edit-a-subdomain"></a>

After adding a custom domain to an app, you can edit an existing subdomain or add a new subdomain\.

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to manage subdomains for\.

1. In the Navigation pane, choose **App Settings**, **Domain management**\.

1. Choose **Manage subdomains** from the Domain management screen\. In the **Edit domain** screen, you can edit your existing subdomains\. Choose **Add**, to add a new subdomain\. When you are finished, choose **Update** to save your changes\.