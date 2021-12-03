# Adding a service role to the Amplify Console when you connect an app<a name="how-to-service-role-amplify-console"></a>

The Amplify Console requires permissions to deploy backend resources with your front end\. You use a service role to accomplish this\. A service role is the AWS Identity and Access Management \(IAM\) role that Amplify Console assumes when calling other services on your behalf\. In this guide, you will create an Amplify service role that has account administrative permissions and explicity allows direct access to resources that Amplify applications require to deploy any Amplify CLI resources, and create and manage backends \. For more information, about the Amplify CLI, see [Amplify CLI](https://docs.amplify.aws/cli) in the *Amplify Framework Documentation*\.

## Step 1: Sign in to the IAM console<a name="step-1-login-to-the-iam-console"></a>

 [Open the IAM console](https://console.aws.amazon.com/iam/home?#/roles) and choose **Roles** from the left navigation bar, then choose **Create role**\.

## Step 2: Create Amplify role<a name="step-2-create-amplify-role"></a>

In the role selection screen find **Amplify** and choose the **Amplify\-Backend Deployment** role\. Accept all the defaults and choose a name for your role, such as **AmplifyConsoleServiceRole\-AmplifyRole**\.

## Step 3: Return to the Amplify Console<a name="step-3-return-to-the-amplify-console"></a>

Open the [Amplify Console](https://console.aws.amazon.com/amplify/)\. If you are in the process of deploying a new app, choose **refresh**, and then choose the role you just created\. It should look like **AmplifyConsoleServiceRole\-AmplifyRole**\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-servicerole.png)

If you already have an existing app, you can find the service role setting in **App settings > General** and then choose **Edit** from the top right corner of the box\. Pick the service role you just created from the dropdown and choose **Save**\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-servicerole2.png)

The Amplify Console now has permissions to deploy backend resources\.

## Confused deputy prevention<a name="confused-deputy-prevention"></a>

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more\-privileged entity to perform the action\. For more information, see [Cross\-service confused deputy prevention](cross-service-confused-deputy-prevention.md)\.

Currently, the default trust policy for the `Amplify-Backend Deployment` service role enforces the `aws:SourceArn` and `aws:SourceAccount` global context condition keys to prevent against confused deputy\. However, if you previously created an `Amplify-Backend Deployment` role in your account, you can update the role's trust policy to add these conditions to protect against confused deputy\.

Use the following example to restrict access to apps in your account\. Replace the red italicized text in the example with your own information\.

```
"Condition": {
      "ArnLike": {
        "aws:SourceArn": "arn:aws:amplify:us-east-1:123456789012:apps/*"
      },
      "StringEquals": {
        "aws:SourceAccount": "123456789012"
      }
    }
```

For instructions on editing the trust policy for a role using the AWS Management Console, see [Modifying a role \(console\)](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html) in the *IAM User Guide*\.