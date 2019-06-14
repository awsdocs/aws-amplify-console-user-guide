.. _environment-variables:

#############################
Environment Variables
#############################

Environment variables are key-value pairs that are available at build time. These configurations can be anything, including:

* Database connection details
* Third-party API keys
* Different customization parameters
* Secrets

As a best practice, you can use environment variables to expose these configurations. All environment variables that you add are encrypted to prevent rogue access so you can use them to store secret information.

.. _setting_env_vars: 
 
Setting Environment Variables
========================

#. In the Amplify console, choose **App Settings** and then choose **Environment Variables**.

#. In the **key** and **value** fields, enter all your app environment variables. By default, the Amplify console applies the environment variables across all branches, so you don't have to re-enter variables when you connect a new branch. 

#. Choose **Save**.


.. image:: images/envvars.png
   :width: 600px

If you need to customize a variable specifically for a branch, you can add a branch override. To do this, choose **Actions** and then choose **Add variable override**. You now have a set of environment variables specific to your branch. 

.. image:: images/reuse-backend.gif
   :width: 600px

.. _access_env_vars: 

Accessing Environment Variables
========================

To access an environment variable during a build, edit your build settings to include the environment variable in your build commands.

#. In the Amplify console, choose **App Settings**, choose **Build settings**, and then choose **Edit**.
   
#. Add the environment variable to your build command. You should now be able to access your environment variable during your next build.

    .. code-block:: yaml

	    build:
	      commands:
	        - npm run build:$BUILD_ENV

Amplify Console Environment Variables
======================================

You can use environment variables that are accessible by default within the Amplify Console.

  .. list-table::
     :widths: 1, 1, 1

     * - Variable name
       - Description
       - Example

     * - AWS_APP_ID
       - The app ID of the current build
       - abcd123

     * - AWS_BRANCH
       - The branch name of the current build
       - master

     * - AWS_BRANCH_ARN
       - The branch ARN of the current build
       - arn:aws:amplify:us-west-2:0123456789:apps/abcd123/branches/master

     * - AWS_CLONE_URL
       - The clone URL used to fetch the git repository contents
       - git@github.com:<user-name>/<repo-name>.git

     * - AWS_COMMIT_ID
       - The commit ID of the current build. "HEAD" for rebuilds
       - b41849e9cfc6447b0833a58e5c76fe2ce57094fb

     * - AWS_JOB_ID
       - The job ID of the current build. This includes some padding of '0' so it always has the same length.
       - 0000000001
