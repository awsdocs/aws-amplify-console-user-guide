# Access logs<a name="access-logs"></a>

Access logs store information about all requests that are made to your Amplify hosted app\. All sites hosted on Amplify Console have logs retrievable for any two week window\. To view access logs choose **App settings > Access logs** from your app’s left navigation bar\. Choose **Edit time range** to choose the two week interval you wish to access\. The logs are available to download in a CSV format\.

## Analyzing access logs<a name="analyzing-access-logs"></a>

To analyze access logs you can store the CSV files in an Amazon S3 bucket\. One way to analyze your access logs is to use Amazon Athena\. Athena is an interactive query service that can help you analyze data for AWS services\. You can follow the [step\-by\-step instructions here](https://docs.aws.amazon.com/athena/latest/ug/cloudfront-logs.html#create-cloudfront-table) to create a table\. Once your table has been created, you can query data as follows\.

```
SELECT SUM(bytes) AS total_bytes
FROM logs
WHERE "date" BETWEEN DATE '2018-06-09' AND DATE '2018-06-11'
LIMIT 100;
```