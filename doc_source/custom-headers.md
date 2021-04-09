# Custom headers<a name="custom-headers"></a>

Custom HTTP headers enable you to specify headers for every HTTP response\. Response headers can be used for debugging, security, and informational purposes\. You can specify headers in the AWS Management Console, or by downloading and editing an app’s `customHttp.yml` file and saving it in the project’s root directory\. For detailed procedures, see [Setting custom headers](#setting-custom-headers)\.

Previously, custom HTTP headers were specified for an app either by editing the build specification \(buildspec\) in the AWS Management Console or by downloading and updating the `amplify.yml` file and saving it in the project’s root directory\. Custom headers specified in this way should be migrated out of the buildspec and the `amplify.yml` file\. For instructions, see [Migrating custom headers](#migrate-custom-headers)\.

## Custom header YAML format<a name="custom-header-YAML-format"></a>

Specify custom headers using the following YAML format:

```
customHeaders:
  - pattern: '*.json'
    headers:
    - key: 'custom-header-name-1'
      value: 'custom-header-value-1'
    - key: 'custom-header-name-2'
      value: 'custom-header-value-2'
  - pattern: '/path/*'
    headers:
    - key: 'custom-header-name-1'
      value: 'custom-header-value-2'
```

For a monorepo, use the following YAML format:

```
applications:
  - appRoot: app1
    customHeaders:
    - pattern: '**/*'
      headers:
      - key: 'custom-header-name-1'
        value: 'custom-header-value-1'
  - appRoot: app2
    customHeaders:
    - pattern: '/path/*.json'
      headers:
      - key: 'custom-header-name-2'
        value: 'custom-header-value-2'
```

When you add custom headers to your app, you will specify your own values for the following:

**pattern**  
Custom headers are applied all URL file paths that match the pattern\.

**headers**  
Defines the headers that match the file pattern\.

**key**  
The name of the custom header\.

**value**  
The value of the custom header\.

To learn more about HTTP headers, see Mozilla's list of [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)\.

## Setting custom headers<a name="setting-custom-headers"></a>

There are two ways to specify custom HTTP headers for an AWS Amplify app\. You can specify headers in the AWS Management Console or you can specify headers by downloading and editing an app’s `customHttp.yml` file and saving it in your project’s root directory\. 

**To set custom headers for an app in the AWS Management Console**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app to set custom headers for\.

1. In the navigation pane, choose **App settings**, **Custom headers**\.

1. In the **Custom header specification** section, choose **Edit**\.

1. In the **Edit** window, enter the information for your custom headers using the [custom header YAML format](#custom-header-YAML-format)\.

   1. For `pattern`, enter the pattern to match\.

   1. For `key`, enter the name of the custom header\.

   1. For `value`, enter the value of the custom header\.

1. Choose **Save**\.

1. If you are working with an app in a monorepo, you must redeploy the app to apply the new custom headers\.

**To set custom headers using the customHttp\.yml file**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app to set custom headers for\.

1. In the navigation pane, choose **App settings**, **Custom headers**\.

1. In the **Custom header specification** section, choose **Download**\.

1. Open the downloaded `customHttp.yml` file in the code editor of your choice and enter the information for your custom headers using the [custom header YAML format](#custom-header-YAML-format)\.

   1. For `pattern`, enter the pattern to match\.

   1. For `key`, enter the name of the custom header\.

   1. For `value`, enter the value of the custom header\.

1. Save the edited `customHttp.yml` file in your project's root directory\. If you are working with a monorepo, save the `customHttp.yml` file in the root of your repo\.

1. Deploy your app to apply the new custom headers\.
   + For a CI/CD app, perform a new build from your Git repository that includes the new `customHttp.yml` file\.
   + For a manual deploy app, deploy the app again in the Amplify Console and include the new `customHttp.yml` file with the artifacts that you upload\.

**Note**  
Custom headers set in the `customHttp.yml` file and deployed in the app’s root directory will override custom headers defined in the **Custom headers** section in the AWS Management Console\. 

## Migrating custom headers<a name="migrate-custom-headers"></a>

Previously, custom HTTP headers were specified for an app either by editing the buildspec in the AWS Management Console or by downloading and updating the `amplify.yml` file and saving it in the project’s root directory\. It is strongly recommended that you migrate your custom headers out of the buildspec and the `amplify.yml` file\. 

Specify your custom headers in the **Custom headers** section of the AWS Management Console or by downloading and editing the `customHttp.yml` file\.

**To migrate custom headers stored in the Amplify Console**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app to perform the custom header migration on\.

1. In the navigation pane, choose **App settings**, **Build settings**\. In the **App build specification** section, you can review your app's buildspec\.

1. Choose **Download** to save a copy of your current buildspec\. You can reference this copy later if you need to recover any settings\.

1. When the download is complete, choose **Edit**\.

1. Take note of the custom header information in the file, as you will use it later in step 9\. In the **Edit** window, delete any custom headers from the file and choose **Save**\. 

1. In the navigation pane, choose **App settings**, **Custom headers**\.

1. In the **Custom header specification** section, choose **Edit**\.

1. In the **Edit** window, enter the information for your custom headers that you deleted in step 6\.

1. Choose **Save**\.

1. Redeploy any branch that you want the new custom headers to be applied to\.

**To migrate custom headers from amplify\.yml to customHttp\.yml**

1. Navigate to the `amplify.yml` file currently deployed in your app's root directory\.

1. Open `amplify.yml` in the code editor of your choice\.

1. Take note of the custom header information in the file, as you will use it later in step 8\. Delete the custom headers in the file\. Save and close the file\. 

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app to set custom headers for\.

1. In the navigation pane, choose **App settings**, **Custom headers**\.

1. In the **Custom header specification** section, choose **Download**\.

1. Open the downloaded `customHttp.yml` file in the code editor of your choice and enter the information for your custom headers that you deleted from `amplify.yml` in step 3\.

1. Save the edited `customHttp.yml` file in your project's root directory\. If you are working with a monorepo, save the file in the root of your repo\.

1. Deploy your app to apply the new custom headers\.
   + For a CI/CD app, perform a new build from your Git repository that includes the new `customHttp.yml` file\.
   + For a manual deploy app, deploy the app again in the Amplify Console and include the new `customHttp.yml` file with artifacts that you upload\.

**Note**  
Custom headers set in the `customHttp.yml` file and deployed in the app’s root directory will override the custom headers defined in the **Custom headers** section of the AWS Management Console\. 

## Monorepo custom headers<a name="monorepo-custom-headers"></a>

When you specify custom headers for an app in a monorepo, be aware of the following set up requirements:
+ There is a specific YAML format for a monorepo\. For the correct syntax, see [Custom header YAML format](#custom-header-YAML-format)\. 
+ You can specify custom headers for an application in a monorepo using the **Custom headers** section of the AWS Management Console\. Note that you must redeploy your application to apply the new custom headers\.
+ As an alternative to using the console, you can specify custom headers for an app in a monorepo in a `customHttp.yml` file\. You must save the `customHttp.yml` file in the root of your repo and then redeploy the application to apply the new custom headers\. Custom headers specified in the `customHttp.yml` file will override any custom headers specified using the **Custom headers** section of the AWS Management Console\.

## Security headers example<a name="example-security-headers"></a>

Custom security headers enable enforcing HTTPS, preventing XSS attacks, and defending your browser against clickjacking\. Use the following YAML syntax to apply custom security headers to your app\. 

```
customHeaders:
  - pattern: '**/*'
    headers:
      - key: 'Strict-Transport-Security'
        value: 'max-age=31536000; includeSubDomains'
      - key: 'X-Frame-Options'
        value: 'SAMEORIGIN'
      - key: 'X-XSS-Protection'
        value: '1; mode=block'
      - key: 'X-Content-Type-Options'
        value: 'nosniff'
      - key: 'Content-Security-Policy'
        value: 'default-src self'
```