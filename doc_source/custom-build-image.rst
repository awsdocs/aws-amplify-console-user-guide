.. _custom-build-image:

########################################
Custom Build Images and Live Package Updates
########################################

.. contents::
   :local:
   :depth: 1

.. _setup:

Custom Build Images
=================================================

Custom Build Images can be used to provide a customized build environment. If you have specific dependencies that take a long time to install during a build using our default container, you can create your own Docker image and reference it during a build. Images can be hosted on `Docker Hub <https://hub.docker.com/>`__  or a public `Amazon Elastic Container Registry <https://aws.amazon.com/ecr/>`__. The format expected here is the same as the format Docker pull command (e.g. *node:latest*). In case of a public ECR instance, you are required to provide the full URL (e.g. *aws_account_id.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest*).

Configuring a Custom Build Image
----------------------------------

1. From your App Detail page, choose **App Settings > Build Settings**.

2. From the **Build image settings** container, choose **Edit**.

   .. image:: images/custom-build-1.png

3. Specify your custom build image and choose **Save**.

   .. image:: images/custom-build-2.png

Custom Build Image Requirements
----------------------------------
In order for a custom build image to work as an Amplify Console build image there are a few requirements for the image:

1. **cURL**: When we launch your custom image, we download our build runner into your container, and therefore we require cURL to be present. If this dependency is missing, the build will instantly fail without any output as our build-runner was unable to produce any output.

2. **Git**: In order to clone your Git repository we require Git to be installed in the image. If this dependency is missing, the ‘Cloning repository’ step will fail.

3. **OpenSSH**: In order to securely clone your repository we require OpenSSH to set up the SSH key temporarily during the build, the OpenSSH package provides the commands that the build runner requires to do this.

4. **(NPM-based builds)Node.JS+NPM**: Our build runner does not install Node, but instead relies on Node and NPM being installed in the image. This is only required for builds that require NPM packages or Node specific commands.

.. _setup-live-updates:

Live Package Updates
=================================================

Live Package Updates allows you to specify versions of packages and dependencies to use in our default build image. Our default build image comes with several packages and dependencies pre-installed (e.g. Hugo, Amplify CLI, Yarn, etc). Live Package Updates allows you to override the version of these dependencies and specify either a specific version, or always ensure the latest version is installed. If Live Package Updates is enabled, before your build is executed, the build runner will first update (or downgrade) the specified dependencies. This will increase the build time proportional to the time it takes to update the dependencies, but the benefit is that you can ensure the same version of a dependency is used to build your app.

Configuring Live Updates
----------------------------------

1. From your App Detail page, choose **App Settings > Build Settings**.

2. From the **Build image settings** section, choose **Edit**.

   .. image:: images/custom-build-1.png

3. Select a package you’d like to change from the **Add package version override** list.

   .. image:: images/live-updates1.png

4. Input either a specific version of this dependency, or keep the default (**latest**). If **latest** is used, the dependency will always be upgraded to the latest version available. Choose **Save** to apply the settings.

   .. image:: images/live-updates2.png