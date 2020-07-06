# Pattern\-based feature branch deployments<a name="pattern-based-feature-branch-deployments"></a>

Pattern\-based branch deployments allow you to automatically deploy branches that match a specific pattern to the Amplify Console\. Product teams using feature branch or GitFlow workflows for their releases, can now define patterns such as ‘release\*\*’ to automatically deploy Git branches that begin with ‘release’ to a shareable URL\. [This blog post](https://dev.to/kkemple/branch-based-deployment-strategies-with-aws-amplify-console-1n3c) describes using this feature with different team workflows\.

1. Choose **App settings > General > Edit**\.

1. Flip the branch autodetection switch to **Enabled**\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/autobranch.png)

1. Define patterns for automatically deploying branches\.
   + **`*`** – Deploys all branches in your repository\.
   + **`release*`**’ – Deploys all branches that being with the word ‘release\.
   + **`release*/`** – Deploys all branches that match a ‘release /’ pattern\.
   + Specify multiple patterns in a comma\-separated list\. For example, `release*, feature*`\.

1. Set up automatic password protection for all branches that are automatically created by setting **Branch autodetection \- access control** to **Enabled**\.

1. For applications built with an Amplify backend, you can choose to create a new environment or point all branches to an existing backend\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/autobranch.png)

## Pattern\-based feature branch deployments for an app connected to a custom domain<a name="standard"></a>

You can use pattern\-based feature branch deployments for an app connected to an Amazon Route 53 custom domain\. 
+ For instructions on setting up pattern\-based feature branch deployments, see [Set up automatic subdomains for a Amazon Route 53 custom domain](to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md)
+ For instructions on connecting an Amplify app to a custom domain managed in Route 53, see [Add a custom domain managed by Amazon Route 53](to-add-a-custom-domain-managed-by-amazon-route-53.md)
+ For more information about using Route 53, see [What is Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)\.