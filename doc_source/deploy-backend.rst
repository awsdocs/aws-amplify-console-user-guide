.. _deploy-backend:

########################################################
Deploying Serverless Backends with Your Front End (Beta)
########################################################

**Note: This feature is currently only available to users of the beta version of the Amplify CLI, which supports multiple environments. Get started with the feature by installing the Amplify CLI.**

.. code-block:: none

	npm install -g @aws-amplify/cli@multienv

The Amplify Console enables developers building apps with the Amplify Framework to continuously deploy updates to their backend and front end on every code commit. With the Amplify Console you can deploy serverless backends with GraphQL APIs, authentication, analytics, and storage created by the Amplify CLI.

1. Connect any repository and branch that was initialized by the Amplify CLI (Note: Install the beta version of the CLI: **npm install -g @aws-amplify/cli@multienv**).

2. The Amplify Console automatically detects backends provisioned with the Amplify CLI and adds a backend stage to the build YML that looks like this:

    .. code-block:: yaml

        version: 1.0
        env:
            variables:
                key: value
        backend:
            phases:
                build:
                    - export STACKINFO="$(envCache --get stackInfo)"
                    - amplifyPush --environment $AWS_BRANCH
                    - envCache --set stackInfo "$(amplify env get --json --name $AWS_BRANCH)"
                  
    **amplifyPush** - The `amplifyPush script <https://gist.github.com/swaminator/7408de774e24ecf031d0d9928f1fbae5>`__ is a helper script that enables users to specify an environment name as an input and runs the Amplify CLI to create or update an environment. On first build, we create a backend environment that corresponds to the name of the connected branch. ($AWS_BRANCH is a system-defined environment variable). If you want to reuse an existing Amplify environment, modify the $AWS_BRANCH to point to the env-name.

    Example usage:

    .. code-block:: bash
    	
    	amplifyPush --environment ENV_NAME

    **envCache** - The envCache provides key-value storage at build time. The envCache can only be modified during a build and can be re-used at the next build. Using the envCache, we can store information on the deployed environment and make it available to the build container in successive builds. Environment variables in comparison, cannot be modified during a build.

    Example usage: 

    .. code-block:: bash
    	
    	envCache --set <key> <value>
    	envCache --get <key> <value>

3. Choose **Next** and **Save and deploy**. Your app build will start by deploying the backend followed by the front end.