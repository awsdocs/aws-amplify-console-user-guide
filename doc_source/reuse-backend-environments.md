# Utilize Amplify backends across apps<a name="reuse-backends"></a>

The Amplify Console now allows you to easily reuse existing backend environments, across all of your apps in a given region\. You can do this when creating a new app, connecting a new branch to an existing app, or when updating an existing frontend to point to another backend environment\.

## Creating a new app or connecting a new frontend branch<a name="reuse-backends-create-connect"></a>

The steps below are the same whether you are creating a new Amplify Console app, connecting a new frontend app to an existing Amplify Console app, or connecting a new branch to an existing Amplify Console app\.

1. On the branch list page, choose **Connect branch**\. If creating a new app, choose **New app** > **Host web app** from the app home page\.

1. Choose a branch from your repository\.

1. You can now select an existing backend environment from this app, or using the dropdown, any other app in this region, as well as a backend role to allow Amplify Console to build resources on your behalf\.

1. Additionally, you can also opt out of full-stack CI/CD for this backend, for this app\. Unchecking this option will result in this app running in "pull-only" mode, at build time only an `amplify pull` command is executed so that your full-stack app can build successfully, without modifying the existing backend environment\.


![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/select_env_create_role.png)

## Edit an existing frontend to point to a different backend<a name="reuse-backends-edit-existing"></a>

1. On the branch list page, click the **(Edit)** link on the frontend that you would like to change\.

1. On the resulting modal, your current backend settings are displayed\. Select a different backend within this app, or choose another app and select a backend\.

1. Additionally, you can also opt out of full-stack CI/CD for this backend, for this app\. Unchecking this option will result in this app running in "pull-only" mode, at build time only an `amplify pull` command is executed so that your full-stack app can build successfully, without modifying the existing backend environment\.

1. The results from these changes will be applied on your next Amplify Console build\.


![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/edit_backend_for_frontend.png)