
.. _welcome:

################################
What is the AWS Amplify Console?
################################

The AWS Amplify Console is a continuous delivery and hosting service for modern web applications. The AWS Amplify Console simplifies the deployment of your application front end and backend. Connect to your code repository and your front end and backend are deployed in a single workflow, on every code commit. This ensures that your web application is only updated after the deployment is successfully completed, eliminating inconsistencies between your application front end and backend. AWS Amplify Console makes it easier for you to build, deploy, and host your mobile web applications, enabling you to quickly iterate on feedback and get new features to your users faster.

What are Modern Web Applications?
---------------------------------
Modern web applications are constructed as single page web applications that package all application components into static files. Traditional client-server web architectures led to poor experiences--every button click or search required a round trip to the server, re-rendering the entire application. Modern web apps offer a native app-like user experience by serving the app front end, or user interface, efficiently to browsers as prebuilt HTML/JavaScript files that can then invoke backend functionality without reloading the page. 

Modern web applications functionality is often spread across multiple places--such as databases, authentication services, front end code running in the browser, and backend business logic, or AWS Lambda functions, running in the cloud. This makes application deployments complex and time-consuming as developers need to carefully coordinate deployments across the front end and backend to avoid partial or failed deployments. The AWS Amplify Console simplifies deployment of the front end and backend in a single workflow.

AWS Amplify Console supports common Single Page App (SPA) frameworks (e.g. React, Angular, Vue.js, Ionic, Ember), as well as static-site generators like Gatsby, Eleventy, Hugo, VuePress, and Jekyll.

Amplify Console Features
------------------------
With the Amplify Console, you can do the following: 

* Connect your repository (GitHub, BitBucket, GitLab, and AWS CodeCommit), and the Amplify Console automatically detects the front end build settings along with any backend functionality provisioned with the Amplify CLI (command-line toolchain for creating serverless backends). 

* Manage production and staging environments for your front end and backend by connecting new branches.

* Atomic deployments eliminate maintenance windows by ensuring that the web app is only updated when the entire deployment has finished. This eliminates scenarios where files fail to upload properly.

* Connect your custom domain. If you manage your domain in Amazon Route 53, the Amplify Console automatically connects the root (yourdomain.com), www subdomains (www.yourdomain.com), and branch (https://dev.yourdomain.com) subdomains.

* Get screen shots of your app rendered on different mobile devices to pinpoint layout issues.

* Set up rewrites and redirects to maintain SEO rankings.

* Password protect your web app so you can work on new features without making them publicly accessible.

Next Step
---------
:ref:`Get started <getting-started>` with the Amplify Console.
