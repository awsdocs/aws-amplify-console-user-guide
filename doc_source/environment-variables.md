# Environment Variables<a name="environment-variables"></a>

Environment variables are key\-value pairs that are available at build time\. These configurations can be anything, including:
+ Database connection details
+ Third\-party API keys
+ Different customization parameters
+ Secrets

As a best practice, you can use environment variables to expose these configurations\. All environment variables that you add are encrypted to prevent rogue access so you can use them to store secret information\.

## Setting Environment Variables<a name="setting-env-vars"></a>

1. In the Amplify console, choose **App Settings** and then choose **Environment Variables**\.

1. In the **key** and **value** fields, enter all your app environment variables\. By default, the Amplify console applies the environment variables across all branches, so you don’t have to re\-enter variables when you connect a new branch\.

1. Choose **Save**\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/envvars.png)

If you need to customize a variable specifically for a branch, you can add a branch override\. To do this, choose **Actions** and then choose **Add variable override**\. You now have a set of environment variables specific to your branch\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/reuse-backend.gif)

## Accessing Environment Variables<a name="access-env-vars"></a>

To access an environment variable during a build, edit your build settings to include the environment variable in your build commands\.

1. In the Amplify console, choose **App Settings**, choose **Build settings**, and then choose **Edit**\.

1. Add the environment variable to your build command\. You should now be able to access your environment variable during your next build\.

   ```
   build:
     commands:
       - npm run build:$BUILD_ENV
   ```

## Creating a new backend environment with authentication parameters<a name="creating-a-new-backend-environment-with-authentication-parameters"></a>

**To create a new backend environment with authentication parameters**

1. When connecting a branch, choose **Create new environment**, and enter the name of your backend environment\. The following screenshot shows the Backend deployments section of the Amplify console with *backend* entered for the backend environment name\.  
![\[Screenshot of the Backend deployments section in the Amplify console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-newenvironment-1.png)

1. To set the environment variables for the new backend environment, choose **AppSettings**, **Environment variables** in the Navigation pane\. In the **Environment variables** section, choose **Manage variables**\.

1. In the **Environment variables** section, choose **Manage variables**\.

1. In the **Manage variables** section, for the **Variable** \(key\) field, enter your client id\. For the **Value** field, enter your client secret\. See the table in the next topic for the list of Amplify system environment variables that are available by default\. 

## Amplify Console Environment Variables<a name="amplify-console-environment-variables"></a>

You can use environment variables that are accessible by default within the Amplify Console\.


****  

| Variable name | Description | Example value | 
| --- | --- | --- | 
|  AWS\_APP\_ID  |  The app ID of the current build  |  abcd123  | 
|  AWS\_BRANCH  |  The branch name of the current build  |  master  | 
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