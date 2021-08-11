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

1. Add the environment variable to your build command\. You should now be able to access your environment variable during your next build\. This example changes the npm's behavior \(`BUILD_ENV`\) and adds an API token \(`TWITCH_CLIENT_ID`\) for an external service to an environment file for later use:

   ```
   build:
     commands:
       - npm run build:$BUILD_ENV
       - echo "TWITCH_CLIENT_ID=$TWITCH_CLIENT_ID" >> backend/.env
   ```

Each command in your build configuration is executed inside a Bash shell\. For more information on working with environment variables in Bash, see [Shell Expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html#Shell-Expansions) in the GNU Bash Manual\. 

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

## Frontend framework environment variables<a name="frontend-framework-environment-variables"></a>

If you are developing your app with a frontend framework that supports its own environment variables, it is important to understand that these are not the same as the environment variables you configure in the Amplify Console\. For example, React \(prefixed REACT\_APP\) and Gatsby \(prefixed GATSBY\), enable you to create runtime environment variables that those frameworks automatically bundle into your frontend production build\. To understand the effects of using these environment variables to store values, refer to the documentation for the frontend framework you are using\.

Storing sensitive values, such as API keys, inside these frontend framework prefixed environment variables is not a best practice and is highly discouraged\. For an example of using the Amplify Console's build time environment variables for this purpose, see [Access environment variables](#access-env-vars)\.

## Amplify Console environment variables<a name="amplify-console-environment-variables"></a>

You can use the following environment variables that are accessible by default within the Amplify Console\.


****  

| Variable name | Description | Example value | 
| --- | --- | --- | 
|  AWS\_APP\_ID  |  The app ID of the current build  |  abcd123  | 
|  AWS\_BRANCH  |  The branch name of the current build  |  `main`, `develop`, `beta`, `v2.0`  | 
|  AWS\_BRANCH\_ARN  |  The branch ARN of the current build  |  aws:arn:amplify:us\-west\-2:111122223333:appname/branch/\.\.\.  | 
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
|  AMPLIFY\_DIFF\_DEPLOY  |   Enable or disable diff based frontend deployment\. For more information, see [Enable or disable diff based frontend build and deploy](build-settings.md#enable-diff-deploy)\.  |  true  | 
|  AMPLIFY\_DIFF\_DEPLOY\_ROOT  |  The path to use for diff based frontend deployment comparisons, relative to the root of your repository\.  | dist | 
|  AMPLIFY\_DIFF\_BACKEND  |  Enable or disable diff based backend builds\. For more information, see [Enable or disable diff based backend builds](build-settings.md#enable-diff-backend)  | true | 
|  AMPLIFY\_BACKEND\_PULL\_ONLY  |  The Amplify Console manages this environment variable\. For more information, see [Edit an existing frontend to point to a different backend](reuse-backends.md#reuse-backends-edit-existing)  | true | 
|  AMPLIFY\_BACKEND\_APP\_ID  |  The Amplify Console manages this environment variable\. For more information, see [Edit an existing frontend to point to a different backend](reuse-backends.md#reuse-backends-edit-existing)  | abcd123 | 
|  AMPLIFY\_SKIP\_BACKEND\_BUILD  |  If you do not have a backend section in your build spec and want to disable backend builds, set this environment variable to `true`\.  | true | 
|  AMPLIFY\_MONOREPO\_APP\_ROOT  |  The path to use to specify the app root of a monorepo app, relative to the root of your repository\.  | apps/react\-app | 
|  \_BUILD\_TIMEOUT  |  The build timeout duration in minutes\.  |  30  | 

**Note**  
The `AMPLIFY_AMAZON_CLIENT_ID` and `AMPLIFY_AMAZON_CLIENT_SECRET` environment variables are OAuth tokens, not an AWS access key and secret key\. 

# Environment secrets<a name="environment-secrets"></a>

Environment secrets are similar to environment variables, but they are SSM parameter store key value pairs and can be encrypted. Some values must be encrypted such as the Sign in with Apple private key for Amplify Console.

## Set environment secrets<a name="setting-env-secrets"></a>

**To set environment secrets**

1. Sign in to the AWS Management Console and open the [AWS Systems Manager Console](https://console.aws.amazon.com/systems-manager/)\.

1. In the AWS Systems Manager Console, choose **Parameter Store**, and then choose **Create Parameter**.

1. Create a parameter name in the format `/amplify/{your_app_id}/{your_backend_environment_name}/{your_parameter_name}`

1. Under type, choose **SecureString** for encrypted values

1. Under KMS key source, choose **My current account** to use the default key for your account

1. Under **Value**, enter your secret value to encrypt

1. Click **Create parameter**

1. Repeat to add multiple secrets

**Note**  
Amplify only has access to the keys under the `/amplify/{your_app_id}/{your_backend_environment_name}` for the specific environment build, and the default KMS key needs to be used for Amplify to decrypt the value.


## Access environment secrets<a name="access-env-secrets"></a>

Accessing an environment secret during a build is similar to environment variables, except all environment secrets are in `process.env.secrets` as a JSON string\.


## Amplify Console environment secrets<a name="amplify-console-environment-secrets"></a>

You can use the following environment secrets that are accessible by default within the Amplify Console\.

Example full SSM parameter name:
`/amplify/{your_app_id}/{your_backend_environment_name}/AMPLIFY_SIWA_CLIENT_ID`

| Variable name | Description | Example value | 
| --- | --- | --- | 
|  AMPLIFY\_SIWA\_CLIENT\_ID  |  The Sign in with Apple client ID  |  com.yourapp.auth  | 
|  AMPLIFY\_SIWA\_TEAM\_ID  |  The Sign in with Apple team ID   |  ABCD123  | 
|  AMPLIFY\_SIWA\_KEY\_ID  |  The Sign in with Apple key ID  |  ABCD123  | 
|  AMPLIFY\_SIWA\_PRIVATE\_KEY  |  The Sign in with Apple private key  |  -----BEGIN PRIVATE KEY-----****-----END PRIVATE KEY-----  | 
