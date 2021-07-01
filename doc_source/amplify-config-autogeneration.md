# Automatic build\-time generation of Amplify config<a name="amplify-config-autogeneration"></a>

Amplify now supports the automatic build\-time generation of the Amplify config `aws-exports.js` file\. By turning off full stack CI/CD deployments, you enable your app to autogenerate the `aws-exports.js` file and ensure that updates are not made to your backend at build\-time\.

**To autogenerate `aws-exports.js` at build\-time**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app to edit\.

1. Choose the **Frontend environments** tab\.

1. Locate the branch to edit and choose **Edit**\.  
![\[The location of the Edit link for a branch in the Amplify Console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify_edit_backend.png)

1. On the **Edit target background** page, uncheck **Enable full\-stack continuous deployments \(CI/CD\)** to turn off full\-stack CI/CD for this backend\.  
![\[The location of the checkbox to turn off CI/CD in the Amplify Console.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify_turnoff_CICD.png)

1. Select an existing service role to give Amplify the permissions it requires to make changes to your app backend\. If you need to create a service role, choose **Create new role**\. For more information about creating a service role, see [Adding a service role to the Amplify Console when you connect an app](how-to-service-role-amplify-console.md)\.

1. Choose **Save**\. The Amplify Console applies these changes the next time you build the app\.