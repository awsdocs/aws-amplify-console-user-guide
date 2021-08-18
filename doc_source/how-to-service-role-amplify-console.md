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