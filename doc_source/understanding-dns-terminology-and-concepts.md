# Understanding DNS terminology and concepts<a name="understanding-dns-terminology-and-concepts"></a>

If you are unfamiliar with the terms and concepts associated with Domain Name System \(DNS\), the following topics can help you understand the procedures for adding custom domains\.

## DNS terminology<a name="dns-terminology"></a>

The following are a list of terms common to DNS\. They can help you understand the procedures for adding custom domains\.

**CNAME**  
A Canonical Record Name \(CNAME\) is a type of DNS record that masks the domain for a set of webpages and makes them appear as though they are located elsewhere\. A CNAME points a subdomain to a fully qualified domain name \(FQDN\)\. For example, you can create a new CNAME record to map the subdomain **www\.example\.com**, where **www** is the subdomain, to the FQDN domain **branch\-name\.d1m7bkiki6tdw1\.cloudfront\.net** assigned to your app in the Amplify Console\.

**ANAME**  
An ANAME record is like a CNAME record, but at the root level\. An ANAME points the root of your domain to an FQDN\. That FQDN points to an IP address\.

**Name server**  
A name server is a server on the internet that's specialized in handling queries regarding the location of a domain name’s various services\. If you set up your domain in Amazon Route 53, a list of name servers are already assigned to your domain\.

**NS record**  
An NS record points to name servers that look up your domain details\.

## DNS verification<a name="dns-verification"></a>

A Domain Name System \(DNS\) is like a phone book that translates human\-readable domain names into computer\-friendly IP addresses\. When you type **https://google\.com** into a browser, a lookup operation is performed in the DNS provider to find the IP Address of the server that hosts the website\.

DNS providers contain records of domains and their corresponding IP Addresses\. The most commonly used DNS records are CNAME, ANAME, and NS records\.

The Amplify Console uses a CNAME record to verify that you own your custom domain\. If you host your domain with Route 53, verification is done automatically on your behalf\. However, if you host your domain with a third\-party provider such as GoDaddy or Google, you have to manually update your domain’s DNS settings and add a new CNAME record provided by the Amplify Console\.

## Amplify Console custom domain setup<a name="amplify-console-custom-domain-setup"></a>

When you add a custom domain in the Amplify Console, there are a number of steps that need to completed before you can view your app using your custom domain\. The following grapic shows the order of the steps that the Amplify Console performs from SSl creation, to SSL configuration and verification, and finally, domain activation\.

![\[Workflow diagram of the steps in the Amplify Console domain activation process.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/1555951758569-803.png)

The following list describes each step in the domain set up process in detail\.

**SSL create**  
The AWS Amplify Console issues an SSL certificate for setting up a secure custom domain\.

**SSL configuration and verification**  
Before issuing an SSL certificate, the Amplify Console verifies that you are the owner of the domain\. For domains managed by Amazon Route 53, Amplify automatically updates the DNS verification record\. For domains managed outside of Route 53, you need to manually add the DNS verification record displayed by the Amplify console into your domain with a third\-party DNS provider\.

**Domain activation**  
The domain is successfully verified\. For domains managed outside of Route 53, you need to manually add the CNAME records displayed by the Amplify console into your domain with a third\-party DNS provider\.