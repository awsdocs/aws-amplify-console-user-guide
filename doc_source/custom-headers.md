# Custom Headers<a name="custom-headers"></a>

Custom HTTP headers allow you to specify headers for every HTTP response\. Response headers can be used for debugging, security, and informational purposes\. Define custom header rules for your app as follows:

1. From the navigation bar on the left, choose App Settings > Build Settings, and then choose *Edit* to edit your buildspec\.

1. In the *frontend* section of the YML file, add the custom headers for your app as follows:

```
version: 0.1
frontend:
    phases:
        build:
        post_build:
    artifacts:
        baseDirectory:
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
+  **pattern** \- Headers applied to all URL file paths that match the pattern\.
+  **headers** \- Define headers that match the file pattern\. The **key** is the custom header name and the **value** is the custom header value\.
+ To learn more about HTTP headers, please see Mozilla’s [documentation for a list of HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)\.

1. Choose **Save**\. Your custom header settings will now be applied to your app\.

## Example: Security Headers<a name="example-security-headers"></a>

The following security headers enable enforcing HTTPS, preventing XSS attacks, and defending your browser against clickjacking\. Add it to your app’s buildspec and choose **Save** to apply the custom header settings\.

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