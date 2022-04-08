# Welcome to AWS Amplify Hosting<a name="welcome"></a>

AWS Amplify is a set of purpose\-built tools and features that enables frontend web and mobile developers to quickly and easily build full\-stack applications on AWS\. Amplify provides two services: Amplify Hosting and Amplify Studio\. Amplify Hosting provides a git\-based workflow for hosting full\-stack serverless web apps with continuous deployment\. This user guide provides the information you need to get started with Amplify Hosting\.

## Amplify Hosting features<a name="amplify-console-features"></a>
+ Amplify Hosting supports the common SPA frameworks, for example, React, Angular, Vue\.js, Ionic, and Ember, as well as static site generators like Gatsby, Eleventy, Hugo, VuePress, and Jekyll\.
+ Manage production and staging environments for your frontend and backend by connecting new branches\. See, [feature branch deployments](multi-environments.md)\.
+ Connect your application to a custom domain\. See, [set up custom domains](custom-domains.md)\.
+ [Deploy and host SSR web apps](server-side-rendering-amplify.md) created using the Next\.js\. framework\.
+ Preview changes during code reviews by setting up [pull request previews](pr-previews.md)\.
+ Improve your app quality with end to end tests\. See, [end\-to\-end testing](running-tests.md)\.
+ Password protect your web app so you can work on new features without making them publicly accessible\. See, [restricting access](access-control.md)\.
+ Set up rewrites and redirects to maintain SEO rankings and route traffic based on your client app requirements\. See, [using redirects](redirects.md)\.
+ Instant cache invalidations ensure your app is updated instantly on every code commit\.
+ Atomic deployments eliminate maintenance windows by ensuring that the web app is updated only after the entire deployment finishes\. This eliminates scenarios where files fail to upload properly\.
+ Get screen shots of your app rendered on different mobile devices to identify layout issues\.

## Getting started with Amplify Hosting<a name="get-started-hosting"></a>

To get started with Amplify's hosting features, see the [Getting started with existing code](getting-started.md) tutorial\. After completing the tutorial, you will be able to connect your git repository \(GitHub, BitBucket Cloud, GitLab, and AWS CodeCommit\) to set up continuous deployment\. Alternatively, you can get started with one of the [fullstack continuous deployment samples](deploy-backend.md)\.

## Amplify Studio<a name="about-amplify-studio"></a>

You can access Amplify Studio from the AWS Amplify console in the AWS Management Console\. Amplify Studio is a visual development environment that simplifies the creation of scalable, full\-stack web and mobile apps\. Use Studio to build your frontend UI with a set of ready\-to\-use UI components, create an app backend, and then connect the two together\. See the user guide for [Amplify Studio](https://docs.amplify.aws/console) in the *Amplify docs*\.

### Amplify Studio features<a name="studio-features"></a>
+ Visual data modeling enables you to focus on your domain\-specific objects instead of cloud infrastructure\.
+ Set up authentication for your app\.
+ Powerful and easy to understand authorization\.
+ Infrastructure\-as\-code configures all backend capabilities with AWS CloudFormation\.
+ Works with the Amplify Command Line Interface \(CLI\)\. All updates you make in Studio can be pulled into the CLI\. 
+ Invite users via email to configure and manage the backend\. These users will also be able to log in to the Amplify CLI with their email\.
+ Content management with markdown support\.
+ Manage users and groups for your app\.
+ Use Studio's visual designer to build frontend UI components\. Choose from dozens of designs in the pre\-built UI component library\.
+ Import Figma prototypes built by designers into Studio as React code\.
+ Customize your frontend UI with themes to apply global styles to your app's components\.
+ Configure and test your UI components directly within Studio to see how they update and display data\.
+ Bind your cloud\-connected backend to your frontend UI in a few simple steps\.

### Getting started with Amplify Studio<a name="get-started-adminui"></a>

You don't need an AWS account to get started using Studio to create a backend\. Without an AWS account, you can begin modeling data for your backend locally\.

With an AWS account, you have access to an expanded set of Studio features for managing your backend environment as well as the visual designer for creating frontend UI components that you can connect to your app's backend\. For more information, see [Getting started](https://docs.amplify.aws/console/adminui/start) in the *Amplify docs*\.

## Modern SPA web applications<a name="modern-web-applications"></a>

This user guide is intended for customers who have a basic understanding of modern single\-page web applications \(SPA\)\. Modern web applications are constructed as SPAs that package all application components into static files\. Traditional client\-server web architectures led to poor experiences; every button click or search required a round trip to the server, re\-rendering the entire application\. Modern web apps offer a native app\-like user experience by serving the app frontend, or user interface, efficiently to browsers as prebuilt HTML/JavaScript files that can then invoke backend functionality without reloading the page\.

A modern web application's functionality is often spread across multiple places, such as databases, authentication services, frontend code running in the browser, and backend business logic, or AWS Lambda functions, running in the cloud\. This makes application deployments complex and time\-consuming as developers need to carefully coordinate deployments across the frontend and backend to avoid partial or failed deployments\. Amplify simplifies deployment of the frontend and backend in a single workflow\.