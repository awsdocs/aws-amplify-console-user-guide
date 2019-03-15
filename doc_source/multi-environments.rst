.. _multi-environments:

#################################################
Feature branch deployments and team workflows
#################################################

The Amplify Console is designed to work with feature branch and GitFlow workflows. The Amplify Console leverages Git branches to create new deployments every time a developer connects a new branch in their repository. After connecting your first branch, you can create a new feature branch deployment by adding a branch as follows:

1. On the branch list page, choose **Connect branch**.

2. Choose a branch from your repository.

3. Save and then deploy your app.

Your app now has two deployments available at `https://master.appid.amplifyapp.com` and `https://dev.appid.amplifyapp.com`. This may vary from team-to-team, but typically the **master branch** tracks release code and is your production branch. The **develop branch** is used as an integration branch to test new features. This way beta testers can test unreleased features on the develop branch deployment, without affecting any of the production end users on the master branch deployment.

.. image:: images/amplify-environments-1.png
   :align: center


Team workflows with Amplify CLI backend environments
===============================

A feature branch deployment can consist of a **frontend** and [(optionally) a **backend**](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-backend.html). The frontend is built and deployed to a global CDN, while the backend is deployed by the Amplify CLI to AWS.
You can use the Amplify Console to continuously deploy backend resources such as GraphQL APIs and Lambda functions with your feature branch deployment. You can use the following models to deploy your backend and frontend with the Amplify Console:

.. contents::
   :local:
   :depth: 1

.. _standard:

Feature branch workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Create **prod**, **test**, and **dev** backend environments with the Amplify CLI.
* Map **prod** and **test** to **master** and **develop** branches.
* Teammates can use the **dev** backend environment to test against **feature** branches.

.. image:: images/amplify-environments-2.png
   :align: center
   :width: 500px

1. Install the Amplify CLI to initialize a new Amplify project.

    .. code-block:: none

        npm install -g @aws-amplify/cli

2. Initialize a `prod` backend environment for your project. If you don't have a project, create one using bootstrap tools like create-react-app or Gatsby.

    .. code-block:: none

        create-react-app next-unicorn
        cd next-unicorn
        amplify init
         ? Do you want to use an existing environment? (Y/n): n 
         ? Enter a name for the environment: prod
        ...
        amplify push

3. Add `test` and `dev` backend environments.

    .. code-block:: none

        amplify env add
         ? Do you want to use an existing environment? (Y/n): n 
         ? Enter a name for the environment: test
        ...
        amplify push

        amplify env add
         ? Do you want to use an existing environment? (Y/n): n 
         ? Enter a name for the environment: dev
        ...
        amplify push

4. Push code to a Git repository of your choice (in this example we'll assume you pushed to master).

    .. code-block:: none

        git commit -am 'Added dev, test, and prod environments'
        git push origin master

5. Connect your repo > branch `master` to the Amplify Console.

6. The Amplify Console will detect backend environments created by the Amplify CLI. Choose `prod` from the dropdown and grant the service role to Amplify Console. Choose **Save and deploy**. After the build completes you will get a master branch deployment available at `https://master.appid.amplifyapp.com`.

	.. image:: images/reuse-backend-2.png

7. Connect `develop` branch in Amplify Console (assume `develop` and `master` branch are the same at this point). Choose the `test` backend environment.

	.. image:: images/reuse-backend-4.png

8. The Amplify Console is now setup. You can start working on new features in a feature branch. Add backend functionality by using the `dev` backend environment from your local workstation.

    .. code-block:: none

    	git checkout -b newinternet
        amplify env checkout dev
        amplify add api
        ...
        amplify push

9. After you finish working on the feature, commit your code, create a pull request to review internally.

    .. code-block:: none

    	git commit -am 'Decentralized internet v0.1'
        git push origin newinternet

10. To preview what the changes will look like, go to the Console and connect your feature branch. Note: If you have the AWS CLI installed on your system (Not the Amplify CLI), you can connect a branch directly from your terminal. You can find your appid by going to App settings > General > AppARN: `arn:aws:amplify:<region>:<region>:apps/<appid>` 

    .. code-block:: none

    	aws amplify create-branch --app-id <appid> --branch-name <branchname>
    	aws amplify start-job --app-id <appid> --branch-name <branchname> --job-type RELEASE

11. Your feature will be accessible at `https://newinternet.appid.amplifyapp.com` to share with your teammates. If everything looks good merge the PR to the develop branch.

    .. code-block:: none

    	git checkout develop
    	git merge newinternet
    	git push

12. This will kickoff a build that will update the backend as well as the frontend in the Amplify Console with a branch deployment at `https://dev.appid.amplifyapp.com`. You can share this link with internal stakeholders so they can review the new feature.

13. Delete your feature branch from Git, Amplify Console, and remove the backend environment from the cloud (you can always spin up a new one based on by running 'amplify env checkout prod' and running 'amplify env add').

    .. code-block:: none

    	git push origin --delete newinternet
    	aws amplify delete-branch --app-id <appid> --branch-name <branchname>
    	amplify env remove dev

.. _gitflow:

GitFlow workflow
~~~~~~~~~~~~~~~~~

GitFlow uses two branches to record the history of the project. The `master` branch tracks release code only, and the `develop` branch is used as an integration branch for new features. GitFlow simplifies parallel development by isolating new development from completed work. New development (such as features and non-emergency bug fixes) is done in `feature` branches. When the developer is satisfied that the code is ready for release, the `feature` branch is merged back into the integration `develop` branch. The only commits to the master branch are merges from `release` branches and `hotfix` branches (to fix emergency bugs). 

The diagram below shows a recommended setup with GitFlow. You can follow the same process as described in the feature branch workflow section above.

.. image:: images/amplify-environments-3.png
   :align: center
   :width: 600px

.. _sandbox:

Per-developer sandbox
~~~~~~~~~~~~~~~~~~~~~~

* Each developer in a team creates a sandbox environment in the cloud that is separate from their local computer. This allows developers to work in isolation from each other without overwriting other team members' changes.
* Each branch in the Amplify Console has its own backend. This ensures that the Amplify Console uses the Git repository as a single source of truth from which to deploy changes, rather than relying on developers on the team to manually push their backend or front end to production from their local computers.

.. image:: images/amplify-env-central-workflow.png
   :align: center
   :width: 300px

1. Install the Amplify CLI to initialize a new Amplify project.

    .. code-block:: none

        npm install -g @aws-amplify/cli

2. Initialize a `kita` backend environment for your project. If you don't have a project, create one using bootstrap tools like create-react-app or Gatsby.

    .. code-block:: none

        cd next-unicorn
        amplify init
         ? Do you want to use an existing environment? (Y/n): n 
         ? Enter a name for the environment: kita
        ...
        amplify push

4. Push code to a Git repository of your choice (in this example we'll assume you pushed to master).

    .. code-block:: none

        git commit -am 'Added kita sandbox'
        git push origin master

5. Connect your repo > `master` to the Amplify Console.

6. The Amplify Console will detect backend environments created by the Amplify CLI. Choose `Create new environment` from the dropdown and grant the service role to Amplify Console. Choose **Save and deploy**. After the build completes you will get a master branch deployment available at `https://master.appid.amplifyapp.com` with a new backend environment that is linked to the branch.

	.. image:: images/reuse-backend-3.png

7. Connect `develop` branch in Amplify Console (assume `develop` and `master` branch are the same at this point) and choose `Create new environment`. After the build completes you will get a develop branch deployment available at `https://develop.appid.amplifyapp.com` with a new backend environment that is linked to the branch.
