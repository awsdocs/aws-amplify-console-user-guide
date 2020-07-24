# Welcome to the AWS Amplify Console<a name="welcome"></a>

The AWS Amplify Console provides a Git\-based workflow for hosting fullstack serverless web apps with continuous deployment\. A fullstack serverless app consists of a backend built with cloud resources such as GraphQL or REST APIs, file and data storage, and a frontend built with single\-page application \(SPA\) frameworks such as React, Angular, Vue, or Gatsby\.

AWS Amplify Console supports common SPA frameworks \(e\.g\. React, Angular, Vue\.js, Ionic, Ember\), as well as static\-site generators like Gatsby, Eleventy, Hugo, VuePress, and Jekyll\.

## Get started<a name="get-started"></a>

To get started with Amplify Console [connect your repository](getting-started.md) \(GitHub, BitBucket Cloud, GitLab, and AWS CodeCommit\) to set up continuous deployment\. Alternatively, start with one of our [fullstack samples](deploy-backend.md)\. Amplify Console automatically detects the frontend build settings along with any backend functionality provisioned with the Amplify CLI \(command\-line toolchain for creating serverless backends\)\.

## Amplify Console Features<a name="amplify-console-features"></a>

With the Amplify Console, you can do the following:
+ Manage production and staging environments for your frontend and backend by connecting new branches\. [See feature branch deployments](multi-environments.md)\.
+ Connect your custom domain\. If you manage your domain in Amazon Route 53, the Amplify Console automatically connects the root domain \(yourdomain\.com\), www subdomains \(www\.yourdomain\.com\), and branch subdomains \(https://dev\.yourdomain\.com\)\. [See custom domains](custom-domains.md)\.
+ Preview changes during code reviews by setting up [Pull\-Request Previews](pr-previews.md)\.
+ Improve your app quality with end to end tests\. [See End\-to\-End Testing](running-tests.md)\.
+ Password protect your web app so you can work on new features without making them publicly accessible\. [See restricting access](access-control.md)\.
+ Set up rewrites and redirects to maintain SEO rankings and route traffic based on your client app requirements\. [See redirects](redirects.md)\.

Also:
+ Instant cache invalidations ensure your app is updated on every code commit instantly\.
+ Atomic deployments eliminate maintenance windows by ensuring that the web app is only updated when the entire deployment has finished\. This eliminates scenarios where files fail to upload properly\.
+ Get screen shots of your app rendered on different mobile devices to pinpoint layout issues\.

## Modern Web Applications<a name="modern-web-applications"></a>

Modern web applications are constructed as single\-page applications \(SPA\) that package all application components into static files\. Traditional client\-server web architectures led to poor experiences; every button click or search required a round trip to the server, re\-rendering the entire application\. Modern web apps offer a native app\-like user experience by serving the app frontend, or user interface, efficiently to browsers as prebuilt HTML/JavaScript files that can then invoke backend functionality without reloading the page\.

Modern web applications functionality is often spread across multiple places, such as databases, authentication services, frontend code running in the browser, and backend business logic, or AWS Lambda functions, running in the cloud\. This makes application deployments complex and time\-consuming as developers need to carefully coordinate deployments across the frontend and backend to avoid partial or failed deployments\. The AWS Amplify Console simplifies deployment of the frontend and backend in a single workflow\.