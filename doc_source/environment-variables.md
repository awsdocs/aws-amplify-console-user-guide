# Environment variables<a name="environment-variables"></a>

Environment variables are key\-value pairs that are available at build time\. These configurations can be anything, including the following:
+ Database connection details
+ Third\-party API keys
+ Different customization parameters
+ Secrets

As a best practice, you can use environment variables to expose these configurations\. All environment variables that you add are encrypted to prevent rogue access, so you can use them to store secret information\.

**Note**  
**Environment variables** is visible in the Amplify Console’s App settings menu only when an app is set up for continuous deployment and connected to a git repository\. For instructions on this type of deployment, see [Getting started with existing code](getting-started.md)\.

## Set environment variables<a name="setting-env-vars"></a>

**To set environment variables**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. In the Amplify Console, choose **App Settings**, and then choose **Environment variables**\.

1. In the **Environment variables** section, choose **Manage variables**\.

1. In the **Manage variables** section, under **Variable**, enter your key\. For **Value**, enter your value\. By default, the Amplify console applies the environment variables across all branches, so you don’t have to re\-enter variables when you connect a new branch\.  
![\[Screenshot of the Manage variables section.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/envvars.png)

1. \(Optional\) To customize an environment variable specifically for a branch, add a branch override as follows: 

   1. Choose **Actions** and then choose **Add variable override**\.

   1. You now have a set of environment variables specific to your branch\.  
![\[An animated gif demonstrating how to add a branch override.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/reuse-backend.gif)

1. Choose **Save**\.

## Access environment variables<a name="access-env-vars"></a>

To access an environment variable during a build, edit your build settings to include the environment variable in your build commands\.

**To edit build settings to include an environment variable**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. In the Amplify Console, choose **App Settings**, then choose **Build settings**\.

1. In the **App build specification** section, choose **Edit**\.

1. Add the environment variable to your build command\. You should now be able to access your environment variable during your next build\.

   ```
   build:
     commands:
       - npm run build:$BUILD_ENV
   ```

## Create a new backend environment with authentication parameters for social sign\-in<a name="creating-a-new-backend-environment-with-authentication-parameters"></a>

**To connect a branch to an app**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1.  The procedure for connecting a branch to an app varies depending on whether you are connecting a branch to a new app or an existing app\.
   + **Connecting a branch to a new app**

     1. When connecting a branch to a new app, in the **Configure build settings** step of the wizard, choose **Create new environment**, and enter the name of your backend environment\. The following screenshot shows the **Backend deployments** section of the Amplify console with **backend** entered for the backend environment name\.  
![\[Screenshot of the Backend deployments section in the Amplify Console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-newenvironment-1.png)

     1. Expand the **Advanced settings** section in the build settings configuration wizard and add environment variables for social sign\-in keys\. For example, **AMPLIFY\_FACEBOOK\_CLIENT\_SECRET** is a valid environment variable\. For the list of Amplify system environment variables that are available by default, see the table in [Amplify Console environment variables](#amplify-console-environment-variables)\.
   + **Connecting a branch to an existing app**

     1. If you are connecting a new branch to an existing app, set the social sign\-in environment variables before connecting the branch\. In the navigation pane, choose **App Settings**, **Environment variables**\.

     1. In the **Environment variables** section, choose **Manage variables**\.

     1. In the **Manage variables** section, for **Variable** \(key\), enter your client ID\. For **Value**, enter your client secret\. For the list of Amplify system environment variables that are available by default, see the table in [Amplify Console environment variables](#amplify-console-environment-variables)\. 

## Amplify Console environment variables<a name="amplify-console-environment-variables"></a>

You can use the following environment variables that are accessible by default within the Amplify Console\.


****  

| Variable name | Description | Example value | 
| --- | --- | --- | 
|  AWS\_APP\_ID  |  The app ID of the current build  |  abcd123  | 
|  AWS\_BRANCH  |  The branch name of the current build  |  main  | 
|  AWS\_BRANCH\_ARN  |  The branch ARN of the current build  |  arn:xxxxx/xxxx/xxxxx  | 
|  AWS\_CLONE\_URL  |  The clone URL used to fetch the git repository contents  |   [git@github\.com](mailto:git@github.com):<user\-name>/<repo\-name>\.git  | 
|  AWS\_COMMIT\_ID  |  The commit ID of the current build\. “HEAD” for rebuilds  |  xxxxxxxxxxxxxxxxxx  | 
|  AWS\_JOB\_ID  |  The job ID of the current build\. This includes some padding of ‘0’ so it always has the same length\.  |  0000000001  | 
|  \_LIVE\_UPDATES  |  The tool will be upgraded to the latest version\.  |  \[\{“name”:”Amplify CLI”,”pkg”:”@aws\-amplify/cli”,”type”:”npm”,”version”:”latest”\}\]  | 
|  AMPLIFY\_FACEBOOK\_CLIENT\_ID  |  The Facebook client ID\.  |  123456  | 
|  AMPLIFY\_FACEBOOK\_CLIENT\_SECRET  |  The Facebook client secret\.  |  example123456  | 
|  AMPLIFY\_GOOGLE\_CLIENT\_ID  |  The Google client ID\.  |  123456  | 
|  AMPLIFY\_GOOGLE\_CLIENT\_SECRET  |  The Google client secret\.  |  example123456  | 
|  AMPLIFY\_AMAZON\_CLIENT\_ID  |  The Amazon client ID\.  |  123456  | 
|  AMPLIFY\_AMAZON\_CLIENT\_SECRET  |  The Amazon client secret\.  |  example123456  | 
|  \_BUILD\_TIMEOUT  |  The build timeout duration in minutes\.  |  30  | 