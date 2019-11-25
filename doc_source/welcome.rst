
.. _welcome:

################################
Welcome to the AWS Amplify Console
################################

The AWS Amplify Console provides a Git-based workflow for hosting fullstack serverless web apps with continuous deployment. A fullstack serverless app consists of a backend built with cloud resources such as GraphQL or REST APIs, file and data storage, and a frontend built with single page application frameworks such as React, Angular, Vue, or Gatsby.

AWS Amplify Console supports common Single Page App (SPA) frameworks (e.g. React Angular, Vue.js, Ionic, Ember), as well as static-site generators like Gatsby, Eleventy Hugo, VuePress, and Jekyll.

Get started
---------
To get started with Amplify Console :ref:`connect your repository <getting-started>` to set up continuous deployment. Alternatively, start with one of our :ref:`fullstack samples <deploy-backend>`.

Amplify Console Features
------------------------
With the Amplify Console, you can do the following: 

* Connect your repository (GitHub, BitBucket, GitLab, and AWS CodeCommit), and the Amplify Console automatically detects the front end build settings along with any backend functionality provisioned with the Amplify CLI (command-line toolchain for creating serverless backends). 

* Manage production and staging environments for your frontend and backend by connecting new branches. :ref:`See feature branch deployments <multi-environments>`. 

* Connect your custom domain. If you manage your domain in Amazon Route 53, the Amplify Console automatically connects the root (yourdomain.com), www subdomains (www.yourdomain.com), and branch (https://dev.yourdomain.com) subdomains. :ref:`See custom domains <custom-domains>`.

* Preview changes during code reviews by setting up :ref:`Pull-Request Previews <previews>`.

* Improve your app quality with end to end tests. :ref:`See End-to-End Testing <running-tests>`.

* Password protect your web app so you can work on new features without making them publicly accessible. :ref:`See restricting access <access-control>`.

* Set up rewrites and redirects to maintain SEO rankings and route traffic based on your client app requirements. :ref:`See redirects <redirects>`.

Also:

* Instant cache invalidations ensure your app is updated on every code commit instantly.

* Atomic deployments eliminate maintenance windows by ensuring that the web app is only updated when the entire deployment has finished. This eliminates scenarios where files fail to upload properly.

* Get screen shots of your app rendered on different mobile devices to pinpoint layout issues.


Modern Web Applications
---------------------------------
Modern web applications are constructed as single page web applications that package all application components into static files. Traditional client-server web architectures led to poor experiences--every button click or search required a round trip to the server, re-rendering the entire application. Modern web apps offer a native app-like user experience by serving the app front end, or user interface, efficiently to browsers as prebuilt HTML/JavaScript files that can then invoke backend functionality without reloading the page. 

Modern web applications functionality is often spread across multiple places--such as databases, authentication services, front end code running in the browser, and backend business logic, or AWS Lambda functions, running in the cloud. This makes application deployments complex and time-consuming as developers need to carefully coordinate deployments across the front end and backend to avoid partial or failed deployments. The AWS Amplify Console simplifies deployment of the front end and backend in a single workflow.

