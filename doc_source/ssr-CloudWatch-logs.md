# Amazon CloudWatch Logs for SSR apps<a name="ssr-CloudWatch-logs"></a>

Amplify sends information about your Next\.js runtime to Amazon CloudWatch Logs in your AWS account\. When you deploy an SSR app, the app requires an IAM service role that Amplify assumes when calling other services on your behalf\. You can either allow Amplify Hosting compute to automatically create a service role for you or you can specify a role that you have created\.

If you choose to allow Amplify to create an IAM role for you, the role will already have the permissions to create CloudWatch Logs\. If you create your own IAM role, you will need to add the following permissions to your policy to allow Amplify to access Amazon CloudWatch Logs\.

```
logs:CreateLogStream
logs:CreateLogGroup
logs:DescribeLogGroups
logs:PutLogEvents
```

For more information about service roles, see [Adding a service role](how-to-service-role-amplify-console.md)\.