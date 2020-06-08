# Manage subdomains<a name="to-manage-subdomains"></a>

A subdomain is the part of your URL that appears before your domain name\. For example, **www** is the subdomain of **www\.amazon\.com** and **aws** is the subdomain of **aws\.amazon\.com**\. If you already have a production website, you might want to only connect a subdomain\. Subdomains can also be multilevel, for example **beta\.alpha\.example\.com** has the multilevel subdomain **beta\.alpha**\.

## To add a subdomain only<a name="to-add-a-subdomain-only"></a>

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to add a subdomain to\.

1. In the navigation pane, choose **App Settings**, and then choose **Domain management**\.

1. On the **Domain management** page, choose **Add domain**\.

1. For **Domain**, enter the name of your root domain and then choose **Configure domain**\. For example, if the name of your domain is **https://example\.com**, enter **example\.com** for **Domain**\.

1. Choose **Exclude root** and modify the name of the subdomain\. For example if the domain is **example\.com** you can modify it to only add the subdomain **alpha**\.  
![\[Screenshot of the Add domain section in the Amplify Console configured to add a subdomain.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomain-configure-2Update.png)

## To add a multilevel subdomain<a name="to-add-a-multi-level-subdomain"></a>

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to add a multilevel subdomain to\.

1. In the navigation pane, choose **App Settings**, and then choose **Domain management**\.

1. On the **Domain management** page, choose **Add domain**\.

1. For **Domain**, enter the name of a domain with a subdomain, choose **Exclude root**, and modify the subdomain to add a new level\.

   For example, if you have a domain called **alpha\.example\.com** and you want to create a multilevel subdoman **beta\.alpha\.example\.com**, you would enter **beta** as the subdomain value, as shown in the following screenshot\.  
![\[Screenshot of the Add domain section in the Amplify Console configured to add a multilevel subdomain.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomain-configure-3Update.png)

## To add or edit a subdomain<a name="to-add-or-edit-a-subdomain"></a>

After adding a custom domain to an app, you can edit an existing subdomain or add a new subdomain\.

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose your app that you want to manage subdomains for\.

1. In the navigation pane, choose **App Settings**, and then choose **Domain management**\.

1. On the **Domain management** page, choose **Manage subdomains**\.

1. In **Edit domain**, you can edit your existing subdomains as needed\. 

1. \(Optional\) To add a new subdomain, choose **Add**\. 

1. Choose **Update** to save your changes\.