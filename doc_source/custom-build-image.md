# Custom build images and live package updates<a name="custom-build-image"></a>

**Topics**
+ [Custom build images](#setup)
+ [Live package updates](#setup-live-updates)

## Custom build images<a name="setup"></a>

You can use a custom build image to provide a customized build environment for an Amplify app\. If you have specific dependencies that take a long time to install during a build using Amplify Console's default container, you can create your own Docker image and reference it during a build\. Images can be hosted on [Docker Hub](https://hub.docker.com/) or Amazon Elastic Container Registry Public\.

**Note**  
**Build settings** is visible in the Amplify Console’s App settings menu only when an app is set up for continuous deployment and connected to a git repository\. For instructions on this type of deployment, see [Getting started with existing code](getting-started.md)\.

### Configuring a custom build image<a name="configuring-a-custom-build-image"></a>

**To configure a custom build image**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app that you want to configure a custom build image for\.

1. In the navigation pane, choose **App Settings**, **Build settings**\.

1. On the **Build settings** page, in the **Build image settings** section, choose **Edit**\.

1. In the **Edit build image settings** dialog box, expand the **Build image** menu, and choose **Build image**\.

1. Enter the name of your build image\. For example, if the name of your Docker Hub repo is *exampledockerrepo*, and your image name is *exampleimage* you would enter **exampledockerrepo/exampleimage:latest**\.

1. Choose **Save**\.

**To configure a custom build image hosted in Amazon ECR**

1. See [Getting started](https://docs.aws.amazon.com/AmazonECR/latest/public/public-getting-started.html) in the *Amazon ECR Public User guide* to set up an Amazon ECR Public repository with a Docker image\.

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app that you want to configure a custom build image for\.

1. In the navigation pane, choose **App Settings**, **Build settings**\.

1. On the **Build settings** page, in the **Build image settings** section, choose **Edit**\.

1. In the **Edit build image settings** dialog box, expand the **Build image** menu, and choose **Build image**\.

1. Enter the name of the Amazon ECR Public repo that you created in step one\. This is where your build image is hosted\. For example, if the name of your repo is *ecr\-examplerepo*, you would enter **public\.ecr\.aws/xxxxxxxx/ecr\-examplerepo**\.

1. Choose **Save**\.

### Custom build image requirements<a name="custom-build-image-requirements"></a>

For a custom build image to work as an Amplify Console build image, it must meet the following requirements:

1.  **cURL**: When we launch your custom image, we download our build runner into your container, and therefore we require cURL to be present\. If this dependency is missing, the build will instantly fail without any output as our build\-runner was unable to produce any output\.

1.  **Git**: In order to clone your Git repository we require Git to be installed in the image\. If this dependency is missing, the ‘Cloning repository’ step will fail\.

1.  **OpenSSH**: In order to securely clone your repository we require OpenSSH to set up the SSH key temporarily during the build, the OpenSSH package provides the commands that the build runner requires to do this\.

1.  **\(NPM\-based builds\) Node\.JS\+NPM**: Our build runner does not install Node, but instead relies on Node and NPM being installed in the image\. This is only required for builds that require NPM packages or Node specific commands\.

## Live package updates<a name="setup-live-updates"></a>

Live package updates enable you to specify versions of packages and dependencies to use in the Amplify Console default build image\. The default build image comes with several packages and dependencies pre\-installed \(e\.g\. Hugo, Amplify CLI, Yarn, etc\)\. With live package updates you can override the version of these dependencies and specify either a specific version, or ensure that the latest version is always installed\. If live package updates is enabled, before your build runs, the build runner first updates \(or downgrades\) the specified dependencies\. This increases the build time proportional to the time it takes to update the dependencies, but the benefit is that you can ensure the same version of a dependency is used to build your app\.

### Configuring live package updates<a name="configuring-live-updates"></a>

**To configure live package updates**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app that you want to configure live package updates for\.

1. In the navigation pane, choose **App Settings**, **Build settings**\.

1. On the **Build settings** page, in the **Build image settings** section, choose **Edit**\.

1. In the **Edit build image settings** dialog box, expand the **Add package version override** list, and choose the package you want to change\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/live-updates-1.png)

1. For **Version**, either keep the default **latest** or enter a specific version of the dependency\. If you use **latest**, the dependency will always be upgraded to the latest version available\.

1. Choose **Save**\.