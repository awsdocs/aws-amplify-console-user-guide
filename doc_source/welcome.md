# Welcome to the AWS Amplify Console<a name="welcome"></a>

The AWS Amplify Console is the control center for fullstack web and mobile application deployments in AWS\. Amplify Console provides two main services, hosting and the Admin UI\. Amplify Console hosting provides a git\-based workflow for hosting fullstack serverless web apps with continuous deployment\. The Admin UI is a visual interface for frontend web and mobile developers to create and manage app backends outside the AWS Management Console\.

A fullstack serverless web app consists of a backend built with cloud resources such as GraphQL or REST APIs, file and data storage, and a frontend built with a single\-page application \(SPA\) framework such as React, Angular, Vue, or Gatsby\. Amplify Console supports the common SPA frameworks \(e\.g\. React, Angular, Vue\.js, Ionic, Ember\), as well as static site generators like Gatsby, Eleventy, Hugo, VuePress, and Jekyll\.

## Amplify Console features<a name="amplify-console-features"></a>

**Hosting features**
+ Manage production and staging environments for your frontend and backend by connecting new branches\. [See feature branch deployments](multi-environments.md)\.
+ Connect your application to a custom domain\. See [Set up custom domains](custom-domains.md)\.
+ Preview changes during code reviews by setting up [pull request previews](pr-previews.md)\.
+ Improve your app quality with end to end tests\. [See End\-to\-end testing](running-tests.md)\.
+ Password protect your web app so you can work on new features without making them publicly accessible\. See [Restricting access](access-control.md)\.
+ Set up rewrites and redirects to maintain SEO rankings and route traffic based on your client app requirements\. See [Using redirects](redirects.md)\.
+ Instant cache invalidations ensure your app is updated instantly on every code commit\.
+ Atomic deployments eliminate maintenance windows by ensuring that the web app is updated only after the entire deployment finishes\. This eliminates scenarios where files fail to upload properly\.
+ Get screen shots of your app rendered on different mobile devices to identify layout issues\.

**Admin UI features**
+ Visual data modeling enables you to focus on your domain\-specific objects instead of cloud infrastructure\.
+ Set up authentication for your app\.
+ Powerful and easy to understand authorization\.
+ Infrastructure\-as\-code configures all backend capabilities with AWS CloudFormation\.
+ Works with the Amplify Command Line Interface \(CLI\)\. All updates you make in the Admin UI can be pulled into the CLI\. 
+ Invite users via email to configure and manage the backend\. These users will also be able to log in to the Amplify CLI with their email\.
+ Content management with markdown support\.
+ Manage users and groups for your app\.

## Getting started<a name="get-started"></a>

### Getting started with hosting<a name="get-started-hosting"></a>

To get started with Amplify Console's hosting features, see the [Getting started with existing code](getting-started.md) tutorial\. You will be able to connect your git repository \(GitHub, BitBucket Cloud, GitLab, and AWS CodeCommit\) to set up continuous deployment\. Alternatively, you can get started with one of the [fullstack continuous deployment samples](deploy-backend.md)\.

### Getting started with the Admin UI<a name="get-started-adminui"></a>

You don't need an AWS account to get started using the Admin UI\. Without an AWS account, you can begin modeling data for your backend locally\. With an AWS account, an expanded set of features are available for managing your backend environment\. For more information, see [Getting started with Admin UI](https://docs.amplify.aws/console/adminui/start)\.

## Modern SPA web applications<a name="modern-web-applications"></a>

This user guide is intended for customers who have a basic understanding of modern single\-page web applications \(SPA\)\. Modern web applications are constructed as SPAs that package all application components into static files\. Traditional client\-server web architectures led to poor experiences; every button click or search required a round trip to the server, re\-rendering the entire application\. Modern web apps offer a native app\-like user experience by serving the app frontend, or user interface, efficiently to browsers as prebuilt HTML/JavaScript files that can then invoke backend functionality without reloading the page\.

A modern web application's functionality is often spread across multiple places, such as databases, authentication services, frontend code running in the browser, and backend business logic, or AWS Lambda functions, running in the cloud\. This makes application deployments complex and time\-consuming as developers need to carefully coordinate deployments across the frontend and backend to avoid partial or failed deployments\. The Amplify Console simplifies deployment of the frontend and backend in a single workflow\.