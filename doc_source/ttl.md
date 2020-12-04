# Managing app performance<a name="ttl"></a>

Amplify Console's default hosting architecture optimizes the balance between hosting performance and deployment availability\. For more information, see [Instant cache invalidation with instant deploys](#Instant-cache-invalidation-with-instant-deploys)\. 

For advanced users that require finer control over an app's performance, Amplify Console supports *performance mode*\. Performance mode optimizes for faster hosting performance by keeping content cached at the content delivery network \(CDN\) edge for a longer interval\. For more information, see [Performance mode](#Performance-mode)\.

## Instant cache invalidation with instant deploys<a name="Instant-cache-invalidation-with-instant-deploys"></a>

Amplify Console supports instant cache invalidation of the CDN on every code commit\. This enables you to deploy updates to your single page or static app instantly, without giving up the performance benefits of CDN caching\.

 For more information about how the Amplify Console handles cache invalidations, see the blog post [AWS Amplify Console supports instant cache invalidation and delta deployments on every code commit](http://aws.amazon.com/blogs/mobile/aws-amplify-console-supports-instant-cache-invalidation-and-delta-deployments/)\.

![\[The instant deploy mode logic for serving a content request from the origin or the CDN cache.\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/instant-cache-invalidation.png)

## Performance mode<a name="Performance-mode"></a>

Amplify Console performance mode optimizes for faster hosting performance by keeping content cached at the edge of the CDN for a longer interval\. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to be deployed and available\.

Performance mode is intended for advanced customers that require finer control over an app's performance\. To optimize the balance between hosting performance and deployment availability, the default [Instant cache invalidation with instant deploys](#Instant-cache-invalidation-with-instant-deploys) hosting architecture is recommended\.

**To enable performance mode for an app**

1. Sign in to the AWS Management Console and open the [Amplify Console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app to enable performance mode for\.

1. In the navigation pane, choose **App settings**, **General**\.

1. In the **Branches** section, select the branch that you want to to enable performance mode for\.

1. Choose **Action**, **Enable performance mode**\.

### Using headers to control cache duration<a name="Using-headers-to-control-cache-duration"></a>

HTTP `Cache-Control` header `max-age` and `s-maxage` directives affect the content caching duration for your app\. The `max-age` directive tells the browser how long \(in seconds\) that you want content to remain in the cache before it is refreshed from the origin server\. The `s-maxage` directive overrides `max-age` and lets you specify how long \(in seconds\) that you want content to remain at the CDN edge before it is refreshed from the origin server\.

You can manually adjust the `s-maxage` directive to have more control over the performance and deployment availability of your app\. For example, to increase the length of time that your content stays cached at the edge, you can manually increase the time to live \(TTL\) by updating `s-maxage` to a value longer than the default 600 seconds \(10 minutes\)\.

You can define custom headers for an app in the **Custom headers** section of the Amplify Console\. For more information, see [Setting custom headers](custom-headers.md#setting-custom-headers)\. To specify a custom value for `s-maxage`, use the following YAML format\. This example keeps the associated content cached at the edge for 3600 seconds \(one hour\)\.

```
customHeaders:
  - pattern: '/img/*'
    headers:
      - key: 'Cache-Control' 
        value: 's-maxage=3600'
```