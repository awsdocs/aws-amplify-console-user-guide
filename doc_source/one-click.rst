.. _one-click:

###################################
Deploy to Amplify Console Button
###################################

The **Deploy to Amplify Console** button enables you to share GitHub projects publicly or within your team. For example, clicking the button below will fork and deploy a create-react-app GitHub repository that implements a basic authentication flow for signing up/signing in users.

.. image:: images/button.png
   :target: https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/aws-samples/create-react-app-auth-amplify


Add 'Deploy to Amplify Console' button to your site
========================

Add this button to your GitHub README.md file, blog post, or any other markup page that renders HTML. The button has two components:

1. An SVG image: ``https://oneclick.amplifyapp.com/button.svg``
2. The Amplify Console URL with a link to your GitHub repository. Please copy your repo URL (e.g. ``https://github.com/username/repository``) only or provide a deep link into a specific folder (e.g. ``https://github.com/username/repository/tree/master/folder``). The Amplify Console will deploy the default branch in your repository. Additional branches can be connected after the app is connected.

3. Add the button to a markdown file (e.g. your GitHub README.md). **Please replace https://github.com/username/repository with your repository name**.

.. code-block:: md

    [![amplifybutton](https://oneclick.amplifyapp.com/button.svg)](https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/username/repository)

4. You can also add the button to any HTML document:

.. code-block:: html

    <a href="https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/username/repository">
        <img src="https://oneclick.amplifyapp.com/button.svg" alt="Deploy to Amplify Console">
    </a> 
