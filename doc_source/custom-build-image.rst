.. _custom-build-image:

########################################
Custom Builds
########################################

Custom Build Images can be used to provide a customized build environment. If you have specific dependencies that take a long time to install during a build using our default container, you can create your own Docker image and reference it during a build. Images can be hosted on `Docker Hub <https://hub.docker.com/>`__  or a public `Amazon Elastic Container Registry <https://aws.amazon.com/ecr/>`__. The format expected here is the same as the format Docker pull command (e.g. *node:latest*). In case of a public ECR instance, you are required to provide the full URL (e.g. *aws_account_id.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest*).

.. _setup:

Configuring a Custom Build Image
=================================================

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
