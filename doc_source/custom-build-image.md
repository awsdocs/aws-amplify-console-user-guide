# Custom Build Images and Live Package Updates<a name="custom-build-image"></a>

**Topics**
+ [Custom Build Images](#setup)
+ [Live Package Updates](#setup-live-updates)

## Custom Build Images<a name="setup"></a>

Custom Build Images can be used to provide a customized build environment\. If you have specific dependencies that take a long time to install during a build using our default container, you can create your own Docker image and reference it during a build\. Images can be hosted on [Docker Hub](https://hub.docker.com/)\. The format expected here is the same as the format Docker pull command \(e\.g\. *node:latest*\)\.

**Note**  
**Build settings** is visible in the Amplify Console’s App settings menu only when an app is set up for continuous deployment and connected to a git repository\. For instructions on this type of deployment, see [Getting started with existing code](getting-started.md)\.

### Configuring a Custom Build Image<a name="configuring-a-custom-build-image"></a>

1. From your App Detail page, choose **App settings > Build settings**\.

1. From the **Build image settings** container, choose **Edit**\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/custom-build-1.png)

1. Specify your custom build image and choose **Save**\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/custom-build-2.png)

### Custom Build Image Requirements<a name="custom-build-image-requirements"></a>

In order for a custom build image to work as an Amplify Console build image there are a few requirements for the image:

1.  **cURL**: When we launch your custom image, we download our build runner into your container, and therefore we require cURL to be present\. If this dependency is missing, the build will instantly fail without any output as our build\-runner was unable to produce any output\.

1.  **Git**: In order to clone your Git repository we require Git to be installed in the image\. If this dependency is missing, the ‘Cloning repository’ step will fail\.

1.  **OpenSSH**: In order to securely clone your repository we require OpenSSH to set up the SSH key temporarily during the build, the OpenSSH package provides the commands that the build runner requires to do this\.

1.  **\(NPM\-based builds\)Node\.JS\+NPM**: Our build runner does not install Node, but instead relies on Node and NPM being installed in the image\. This is only required for builds that require NPM packages or Node specific commands\.

## Live Package Updates<a name="setup-live-updates"></a>

Live Package Updates allows you to specify versions of packages and dependencies to use in our default build image\. Our default build image comes with several packages and dependencies pre\-installed \(e\.g\. Hugo, Amplify CLI, Yarn, etc\)\. Live Package Updates allows you to override the version of these dependencies and specify either a specific version, or always ensure the latest version is installed\. If Live Package Updates is enabled, before your build is executed, the build runner will first update \(or downgrade\) the specified dependencies\. This will increase the build time proportional to the time it takes to update the dependencies, but the benefit is that you can ensure the same version of a dependency is used to build your app\.

### Configuring Live Updates<a name="configuring-live-updates"></a>

1. From your App Detail page, choose **App Settings > Build Settings**\.

1. From the **Build image settings** section, choose **Edit**\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/custom-build-1.png)

1. Select a package you’d like to change from the **Add package version override** list\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/live-updates-1.png)

1. Input either a specific version of this dependency, or keep the default \(**latest**\)\. If **latest** is used, the dependency will always be upgraded to the latest version available\. Choose **Save** to apply the settings\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/live-updates-2.png)