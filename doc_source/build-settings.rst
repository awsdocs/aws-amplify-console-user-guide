.. _build-settings:

###################
Configuring Build Settings
###################

The Amplify Console automatically detects the front end framework and associated build settings by inspecting the package.json file in your repository. You have the following options:

* Save the build settings in the Amplify Console - The Amplify Console autodetects build settings and saves it so that they can be accessed via the Amplify Console. These settings are applied to all of your branches unless there is a YML file found in your repository.

* Save the build settings in your repository - Download the amplify.yml file and add it to the root of your repository (or root of the app folder for monorepos).

You can edit these settings in the Amplify Console by choosing **App Settings>Build settings**. These build settings are applied to all the branches in your app, except for the branches that have a YML file saved in the repository.

.. _yml-specification-syntax: 
 
YML Specification Syntax
======================

The build specification YML contains a collection of build commands and related settings that the Amplify Console uses to run your build. The YML is structured as follows:

.. code-block:: yaml

    version: 1.0
    env:
      variables:
          key: value
    backend:
      phases:
        preBuild:
          commands:
            - *enter command*
        build:
          commands:
            - *enter command*
        postBuild:
            commands:
            - *enter command*
    frontend:
      phases:
        preBuild:
          commands:
            - cd react-app
            - npm ci
        build:
          commands:
            - npm run build
      artifacts:
        files:
            - location
            - location
        discard-paths: yes
        baseDirectory: location
      cache:
        paths:
            - path
            - path


* **version** - Represents the Amplify Console YML version number.
* **env** - Add environment variables to this section. You can also add environment variables using the console.
* **backend** - Run Amplify CLI commands to provision a backend, update Lambda functions, or  GraphQL schemas as part of continuous deployment. Learn how to :ref:`deploy a backend with your frontend <deploy-backend>`.
* **frontend** - Run frontend build commands.
* Both the frontend and backend have three **phases** that represent the commands run during each sequence of the build.
    * **preBuild** - The preBuild script runs before the actual build starts, but after we have installed dependencies.
    * **build** - Your build commands.
    * **postBuild** - The post-build script runs after the build has finished and we have copied all the necessary artifacts to the output directory.
* **artifacts>base-directory** - The directory in which your build artifacts exist.
* **artifacts>files** - Specify files from your artifact you want to deploy. `**/*` is to include all files.

Build Scenarios
======================

The following scenarios describe how to write your build YML. 

Using Branch-Specific Build Settings
---------------------------------
To set branch-specific build settings, add the buildspec YML to the root of your repository. You can do this any of the following ways:

* When connecting a new branch, choose **Edit**. Make your edits and then choose **Save and add to my repo**. The Amplify Console  automatically adds the YML to your repository when you deploy the branch. **Note:** If you do not want these settings to apply to all branches, make sure you don't merge this file into the other branches.

* In the Amplify Console, choose **App settings**, choose **Build settings**, and then choose **Download**. Make your edits and then add this file to the root of your repository.

Navigating to a Subfolder
-------------------------

For monorepos, users want to be able to cd into a folder to run the build. After you run the cd command, it applies to all stages of your build so you don't need to repeat the command in separate phases.

.. code-block:: yaml

    version: 1.0
    env:
      variables:
          key: value
    frontend:
      phases:
        preBuild:
          commands:
            - cd react-app
            - npm ci
        build:
          commands:
            - npm run build

.. _frontend-with-backend:

Deploying the Backend with Your Front End
-------------------------

Use the Amplify CLI to deploy a backend with your front end. :ref:`Learn more <deploy-backend>` about how envCache and amplifyPush commands help you with backend deployments. The $AWS_BRANCH is a system defined environment variable that picks up the current branch. The build settings below will deploy a new backend environment linked to each feature branch.

.. code-block:: yaml

    version: 1.0
    env:
      variables:
          key: value
    backend:
      phases:
        build:
          commands:
            - export STACKINFO="$(envCache --get stackInfo)"
            - amplifyPush --environment $AWS_BRANCH
            - envCache --set stackInfo "$(amplify env get --json --name $AWS_BRANCH)"
     

Setting the Output Folder
-------------------------

The following build settings set the output directory to the public folder.

.. code-block:: yaml

    frontend:
      phases:
        commands:
          build:
            - yarn run build
      artifacts:
        baseDirectory: public


Installing Packages as Part of Your Build
--------------------------------------------
You can use npm or yarn to install packages during the build.

.. code-block:: yaml

    frontend:
      phases:
        build:
          commands:
            - npm install -g pkg-foo
            - pkg-foo deploy
            - yarn run build
      artifacts:
        baseDirectory: public

Using a Private npm Registry
--------------------------------------------
You can add references to a private registry in your build settings or add it as an environment variable.

.. code-block:: yaml

    build:
      phases:
        preBuild:
          commands:
            - npm config set <key> <value>
            - npm config set registry https://registry.npmjs.org
            - npm config set always-auth true
            - npm config set email hello@amplifyapp.com
            - yarn install
 
Installing OS packages
--------------------------------------------
You can install OS packages for missing dependencies.

.. code-block:: yaml

    build:
      phases:
        preBuild:
          commands:
            - yum install -y <package>