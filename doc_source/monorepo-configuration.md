# Monorepo build settings<a name="monorepo-configuration"></a>

When you store multiple projects or microservices in a single repository, it is called a monorepo\. You can use Amplify to deploy applications in a monorepo without creating multiple build configurations or branch configurations\.

You can save the build settings for a monorepo in the Amplify console or you can download the `amplify.yml` file and add it to the root of your repository\. Amplify applies the settings saved in the console to all of your branches unless it finds an `amplify.yml` file in your repository\. When an `amplify.yml` file is present, its settings override any build settings saved in the Amplify console\.

## Monorepo build specification YAML syntax<a name="monorepo-yml-syntax"></a>

The YAML syntax for a monorepo build specification differs from the YAML syntax for a repo that contains a single application\. For a monorepo, you declare each project in a list of applications\. You must provide the following additional information for each application you declare in your monorepo build specification:

**appRoot**  
The root, within the repository, that the application starts in\. This key must exist, and have the same value as the `AMPLIFY_MONOREPO_APP_ROOT` environment variable\. For instructions on setting this environment variable, see [Setting the AMPLIFY\_MONOREPO\_APP\_ROOT environment variable](#setting-monorepo-environment-variable)\.

The following monorepo build specification example demonstrates how to declare multiple Amplify applications in the same repo\. The two apps, `react-app`, and `angular-app` are declared in the `applications` list\. The `appRoot` key for each app indicates that the app is located in the `apps` root folder in the repo\.

```
version: 1
applications:
  - appRoot: apps/react-app
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
            - *enter command*
            - *enter command*
        build:
          commands:
            - *enter command*
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
    test:
      phases:
        preTest:
          commands:
            - *enter command*
        test:
          commands:
            - *enter command*
        postTest:
          commands:
            - *enter command*
      artifacts:
        files:
            - location
            - location
        configFilePath: *location*
        baseDirectory: *location*
  - appRoot: apps/angular-app
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
            - *enter command*
            - *enter command*
        build:
          commands:
            - *enter command*
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
    test:
      phases:
        preTest:
          commands:
            - *enter command*
        test:
          commands:
            - *enter command*
        postTest:
          commands:
            - *enter command*
      artifacts:
        files:
            - location
            - location
        configFilePath: *location*
        baseDirectory: *location*
```

## Setting the AMPLIFY\_MONOREPO\_APP\_ROOT environment variable<a name="setting-monorepo-environment-variable"></a>

When you deploy an app stored in a monorepo, the app's `AMPLIFY_MONOREPO_APP_ROOT` environment variable must have the same value as the path of the app root, relative to the root of your repository\. For example, a monorepo named `ExampleMonorepo` with a root folder named `apps`, that contains, `app1`, `app2`, and `app3` has the following directory structure:

```
ExampleMonorepo
  apps
    app1
    app2
    app3
```

In this example, the value of the `AMPLIFY_MONOREPO_APP_ROOT` environment variable for `app1` is `apps/app1`\.

When you deploy a monorepo app using the Amplify console, the console automatically sets the `AMPLIFY_MONOREPO_APP_ROOT` environment variable using the value that you specify for the path to the app's root\. However, if your monorepo app already exists in Amplify or is deployed using AWS CloudFormation, you must manually set the `AMPLIFY_MONOREPO_APP_ROOT` environment variable in the **Environment variables** section in the Amplify console\.

### Setting the AMPLIFY\_MONOREPO\_APP\_ROOT environment variable automatically during deployment<a name="setting-monorepo-environmnet-variable-automatically"></a>

The following instructions demonstrate how to deploy a monorepo app with the Amplify console\. Amplify automatically sets the `AMPLIFY_MONOREPO_APP_ROOT` environment variable using the app's root folder that you specify in the console\.

**To deploy a monorepo app with the Amplify console**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose **New app**, **Host web app** in the upper right corner\.

1. On the **Host your web app** page, choose your Git provider, then choose **Continue**\.

1. On the **Add repository branch** page, do the following:

   1. Choose the name of your repository from the list of **Recently updated repositories**\.

   1. For **Branch**, choose the name of the branch to use\.

   1. Select **Connecting a monorepo? Pick a folder\.**

   1. Enter the path to your app in your monorepo, for example, **apps/app1**\.

   1. Choose **Next**\.

1. On the **Configure build settings** page you can use the default settings or customize the build settings for your app\. In the following example screenshot, Amplify detects an `amplify.yml` file in the repository to use for the build settings\. In the **Environment variables** section, Amplify has set `AMPLIFY_MONOREPO_APP_ROOT` to `apps/app1`, using the path you specified in step 4d\.  
![\[Screenshot of the Configure build settings page in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-buildsettings-monorepo1.png)

1. Choose **Next**\.

1. On the **Review** page, choose **Save and deploy**\.

### Setting the AMPLIFY\_MONOREPO\_APP\_ROOT environment variable for an existing app<a name="setting-monorepo-environmnet-variable-manually"></a>

Use the following instructions to manually set the `AMPLIFY_MONOREPO_APP_ROOT` environment variable for an app that is already deployed to Amplify, or has been created using CloudFormation\.

**To set the AMPLIFY\_MONOREPO\_APP\_ROOT environment variable for an existing app**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the name of the app to set the environment variable for\.

1. In the navigation pane, choose **App Settings**, and then choose **Environment variables**\.

1. On the **Environment variables** page, choose **Manage variables**\.

1. In the **Manage variables** section, do the following:

   1. Choose **Add variable**\.

   1. For **Variable**, enter the key `AMPLIFY_MONOREPO_APP_ROOT`\.

   1. For **Value**, enter the path to the app, for example **apps/app1**\.

   1. For **Branch**, by default Amplify applies the environment variable to all branches\.

1. Choose **Save**\.