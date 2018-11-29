.. _multi-environments:

#################################################
Managing Multiple Environments and Team Workflows
#################################################

Using Branch-based Environmments
========================
The Amplify Console leverages Git branches to create new environments every time a developer connects a new branch in their repository. After connecting your first branch, you can create a new environment by adding a branch as follows:

1. On the branch list page, choose **Connect branch**.

2. Choose a branch from your repository.

3. Accept the autodetected build settings or modify them according to your app requirements.

4. Save and then deploy your app.

Your app now has two front end environments available at `https://master.appid.amplifyapp.com` and `https://dev.appid.amplifyapp.com`. If your app has a backend provisioned with the Amplify CLI (beta), the Amplify Console deploys separate backends per branch. Connecting a branch creates front end and backend environments, which enables developers to work in sandbox environments and use Git as a mechanism to merge code and resolve conflicts.

.. image:: /images/amplify-environments.png

Using Team Workflows
===========================

For teams that are building serverless apps with the Amplify CLI, we recommend the following:

* That each developer in a team creates a sandbox environment in the cloud that is separate from their local computer. This allows developers to work in isolation from each other without overwriting other team members' changes.

* That your team connects production, test, and feature branches to the Amplify Console. This ensures that the Amplify Console uses the Git repository as a single source of truth from which to deploy changes, rather than relying on developers on the team to manually push their backend or front end to production from their local computers.

The Amplify Console is designed to work with all team workflows such as centralized, feature branch, and GitFlow workflows. 

Using a Centralized Workflow
-----------------------
Teams that transition from SVN to Git practice this workflow. With this workflow, every developer on the team commits code directly to the default branch called `master`. Each developer clones a local copy of the repository, works independently and then pushes code to merge it to the master branch. For example:

1. Connect master to the Amplify Console for continuous deployment.

2. Both Kita and Cody check out the master branch locally and then run the **amplify init** command to set up a cloud backend to make changes to the front end and backend from their local computers. 

3. After the code has been tested locally, Kita pushes the code to the master branch. This kicks off a build in the Amplify Console that updates any front end or backend content that has changed. 

The following command line example and diagram capture the workflow.

.. code-block:: bash

	> git fetch && git checkout master
	> amplify init
		? Do you want to use an existing environment? false
		? Enter a name for the environment kita-sandbox
		// Provide AWS Profile info
	// Test feature locally
	> npm run start
	> git commit -m "New feature" && git push origin master


.. image:: /images/amplify-env-central-workflow.png


Using a Feature Branch Workflow
--------------------------
The main idea behind the feature branch workflow is that feature work happens in a separate branch from the master branch. This enables developers to work on new features in isolation from what is production. When the feature is ready it's merged into the master branch. Similar to the steps in the centralized workflow, all team members work on the feature branch pushing updates to that branch until it's ready to be merged to the master branch. The feature branch is also connected to the Amplify Console (password protected) for continuous deployment so developers can share updates with other stakeholders.

.. image:: /images/amplify-env-feature-workflow.png


Using the GitFlow Workflow
--------------------------
GitFlow uses two branches to record the history of the project. The master branch tracks release code only, and the `develop` branch is used as an integration branch for new features. GitFlow simplifies parallel development by isolating new development from completed work. New development (such as features and non-emergency bug fixes) is done in feature branches. When the developer is satisfied that the code is ready for release, the feature branch is merged back into the integration develop branch. The only commits to the master branch are merges from release branches and hotfix branches (to fix emergency bugs). The diagram below shows which branches are typically connected to the Amplify Console in this model.

.. image:: /images/amplify-env-gitflow-workflow.png
