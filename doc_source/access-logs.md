# Monitoring<a name="access-logs"></a>

AWS Amplify emits metrics through Amazon CloudWatch and provides access logs with detailed information about requests made to your app\. Use the topics in this section to learn how to use these metrics and logs to monitor your app\.

**Topics**
+ [Monitoring with CloudWatch](#monitoring-with-cloudwatch)
+ [Access logs](#using-access-logs)

## Monitoring with CloudWatch<a name="monitoring-with-cloudwatch"></a>

AWS Amplify is integrated with Amazon CloudWatch, allowing you to monitor metrics for your Amplify applications in near real\-time\. You can create alarms that send notifications when a metric exceeds a threshold you set\. For more information about how the CloudWatch service works, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)\.

### Metrics<a name="metrics"></a>

Amplify supports six CloudWatch metrics in the `AWS/AmplifyHosting` namespace for monitoring traffic, errors, data transfer, and latency for your apps\. These metrics are aggregated at one minute intervals\. CloudWatch monitoring metrics are free of charge and don't count against the [CloudWatch service quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html)\.

Not all available statistics are applicable for every metric\. In the following table, the most relevant statistics are listed in the description for each metric\.


| Metrics | Description | 
| --- | --- | 
|  Requests  |  The total number of viewer requests received by your app\. The most relevant statistic is `Sum`\. Use the `Sum` statistic to get the total number of requests\.  | 
|  BytesDownloaded  |  The total amount of data transferred out of your app \(downloaded\) in bytes by viewers for `GET`, `HEAD`, and `OPTIONS` requests\.  The most relevant statistic is `Sum`\.  | 
|  BytesUploaded  |  The total amount of data transferred into your app \(uploaded\) in bytes using `POST` and `PUT` requests\. The most relevant statistic is `Sum`\.  | 
|  4XXErrors  |  The number of requests that returned an error in the HTTP status code 400\-499 range\. The most relevant statistic is `Sum`\. Use the `Sum` statistic to get the total occurrences of these errors\.  | 
|  5XXErrors  |  The number of requests that returned an error in the HTTP status code 500\-599 range\. The most relevant statistic is `Sum`\. Use the `Sum` statistic to get the total occurrences of these errors\.  | 
|  Latency  |  The time to first byte in seconds\. This is the total time between when Amplify Console receives a request and when it returns a response to the network\. This doesn't include the network latency encountered for a response to reach the viewer's device\. The most relevant statistics are `Average`, `Maximum`, `Minimum`, `p10`, `p50`, `p90`, `p95`, and `p100`\. Use the `Average` statistic to evaluate expected latencies\.  | 

Amplify provides the following CloudWatch metric dimensions\.


| Dimension | Description | 
| --- | --- | 
|  App  |  Metric data is provided by app\.  | 
|  AWS Account  |  Metric data is provided across all apps in the AWS account\.  | 

You can access CloudWatch metrics in the AWS Management Console at [https://console\.aws\.amazon\.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/)\. Alternatively, you can access metrics in the Amplify console using the following procedure\.

**To access metrics in the Amplify console**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app that you want to view metrics for\.

1. In the navigation pane, choose **App Settings**, **Monitoring**\.

1. On the **Monitoring** page, choose **Metrics**\.

### Alarms<a name="alarms"></a>

You can create CloudWatch alarms in the Amplify console that send notifications when specific criteria are met\. An alarm watches a single CloudWatch metric and sends an Amazon Simple Notification Service notification when the metric breaches the threshold for a specified number of evaluation periods\.

You can create more advanced alarms that use metric math expressions in the CloudWatch console or using the CloudWatch APIs\. For example, you can create an alarm that notifies you when the percentage of 4XXErrors exceeds 15% for three consecutive periods\. For more information, see [Creating a CloudWatch Alarm Based on a Metric Math Expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.html) in the *Amazon CloudWatch User Guide*\. 

Standard CloudWatch pricing applies to alarms\. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/)\.

Use the following procedure to create an alarm in the Amplify console\.

**To create a CloudWatch alarm for an Amplify metric**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app that you want to set an alarm on\.

1. In the navigation pane, choose **App Settings**, **Monitoring**\.

1. On the **Monitoring** page, choose **Alarms**\.

1. Choose **Create alarm**\.

1. In the **Create alarm** window, configure your alarm as follows:

   1. For **Metric**, choose the name of the metric to monitor from the list\. 

   1. For **Name of alarm**, enter a meaningful name for the alarm\. For example, if you are monitoring *Requests*, you could name the alarm **HighTraffic**\. The name must contain only ASCII characters\.

   1. For **Set up notifications**, do one of the following:
      + 

        1. Choose **New** to set up a new Amazon SNS topic\.

        1. For **Email address**, enter the email address for the recipient of the notifications\.

        1. Choose **Add new email address** to add additional recipients\.
      + 

        1. Choose **Existing** to reuse an Amazon SNS topic\.

        1. For **SNS topic**, select the name of an existing Amazon SNS topic from the list\.

   1. For **Whenever the *Statistic* of *Metric***, set the conditions for your alarm as follows:

      1. Specify whether the metric must be greater than, less than, or equal to the threshold value\.

      1. Specify the threshold value\.

      1. Specify the number of consecutive evaluation periods that must be in the alarm state to trigger the alarm\.

      1. Specify the length of time of the evaluation period\.

   1. Choose **Create alarm**\.

**Note**  
Each Amazon SNS recipient that you specify receives a confirmation email from AWS Notifications\. The email contains a link that the recipient must follow to confirm their subscription and receive notifications\.

## Access logs<a name="using-access-logs"></a>

Amplify stores access logs for all of the apps you host in Amplify\. Access logs contain information about requests that are made to your hosted apps\. You can retrieve these access logs for any two week window that you specify\.

**Important**  
We recommend that you use the logs to understand the nature of the requests for your content, not as a complete accounting of all requests\. Amplify delivers access logs on a best\-effort basis\. The log entry for a particular request might be delivered long after the request was actually processed and, in rare cases, a log entry might not be delivered at all\. When a log entry is omitted from access logs, the number of entries in the access logs won't match the usage that appears in the AWS billing and usage reports\.

Use the following procedure to retrieve access logs\.

**To view access logs**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app that you want to view access logs for\.

1. In the navigation pane, choose **App Settings**, **Monitoring**\.

1. On the **Monitoring** page, choose **Access logs**\.

1. Choose **Edit time range**\.

1. In the **Edit time range** window, for **Start date** specify the first day of the two week interval to retrieve logs for\. For **Start time**, choose the time on the first day to start the log retrieval\.

1. The console displays the logs for your specified time range in the **Access logs** section\. Choose **Download** to save the logs in a CSV format\.

### Analyzing access logs<a name="analyzing-access-logs"></a>

To analyze access logs you can store the CSV files in an Amazon S3 bucket\. One way to analyze your access logs is to use Athena\. Athena is an interactive query service that can help you analyze data for AWS services\. You can follow the [step\-by\-step instructions here](https://docs.aws.amazon.com/athena/latest/ug/cloudfront-logs.html#create-cloudfront-table) to create a table\. Once your table has been created, you can query data as follows\.

```
SELECT SUM(bytes) AS total_bytes
FROM logs
WHERE "date" BETWEEN DATE '2018-06-09' AND DATE '2018-06-11'
LIMIT 100;
```