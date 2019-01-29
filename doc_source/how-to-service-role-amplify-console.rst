.. _how-to-service-role-amplify-console:

####################################################################
Adding a Service Role to the Amplify Console When You Connect an App
####################################################################

The Amplify Console requires permissions to deploy backend resources with your front end. You use a service role to accomplish this. A service role is the IAM role that Amplify Console assumes when calling other services on your behalf.

Step 1: Create a Service Role
-----------------------------
Right-click the following link and choose **Open link in new tab**. It opens the CloudFormation console with pre-selected defaults.

.. image:: images/amplify-cloudformation-launch-stack.png
   :target: /amplify/latest/userguide/launch-stack

Step 2: Accept All Defaults in the AWS CloudFormation Console
-------------------------------------------------------------

In the CloudFormation console, accept all defaults on the four screens to create a role. This role allows the Amplify Console to deploy backend resources during a build.


Step 3: Return to the Amplify Console
-------------------------------------

In the Amplify Console onboarding screen, choose **refresh**, and then pick the role you just created. It should look like **AmplifyConsoleServiceRole-AmplifyRole-XXXXXXXXXXX**.

.. image:: images/amplify-servicerole.png

If you already have an existing app, you can find the service role setting in **App settings > General** and then choose **Edit** from the top right corner of the box. Pick the service role you just created from the dropdown and choose **Save**.

.. image:: images/amplify-servicerole2.png

The Amplify Console now has permissions to deploy backend resources.