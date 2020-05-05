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