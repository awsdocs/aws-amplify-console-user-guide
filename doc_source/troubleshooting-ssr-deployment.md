# Troubleshooting SSR deployments<a name="troubleshooting-ssr-deployment"></a>

If you experience unexpected issues when deploying an SSR app with Amplify Hosting compute, review the following troubleshooting topics\.

**Topics**
+ [Edge API routes cause your Next\.js build to fail](#nextjs-edge-API-route-not-supported)

## Edge API routes cause your Next\.js build to fail<a name="nextjs-edge-API-route-not-supported"></a>

Currently, Amplify doesn't support Next\.js Edge API routes\. You must use non\-edge APIs and middleware when hosting your app with Amplify\.