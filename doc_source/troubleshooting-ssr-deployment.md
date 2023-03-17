# Troubleshooting SSR deployments<a name="troubleshooting-ssr-deployment"></a>

If you experience unexpected issues when deploying an SSR app with Amplify Hosting compute, review the following troubleshooting topics\.

**Topics**
+ [Edge API routes cause your Next\.js build to fail](#nextjs-edge-API-route-not-supported)
+ [On\-Demand Incremental Static Regeneration isn't working for your app](#on-demand-isr-not-supported)
+ [The size of the build output is too large](#build-output-too-large)
+ [Your build fails with an out of memory error](#out-of-memory)

## Edge API routes cause your Next\.js build to fail<a name="nextjs-edge-API-route-not-supported"></a>

Currently, Amplify doesn't support Next\.js Edge API routes\. You must use non\-edge APIs and middleware when hosting your app with Amplify\.

## On\-Demand Incremental Static Regeneration isn't working for your app<a name="on-demand-isr-not-supported"></a>

Starting with version 12\.2\.0, Next\.js supports On\-Demand Incremental Static Regeneration \(ISR\) to manually purge the Next\.js cache for a specific page\. However, Amplify doesn't currently support On\-Demand ISR\. If your app is using using Next\.js on\-demand revalidation, this feature won't work when you deploy your app to Amplify\.

## The size of the build output is too large<a name="build-output-too-large"></a>

Currently, the maximum build output size that Amplify supports for Next\.js 12 and 13 apps using the Web Compute platform is 200 MB\.

If you get an error that the size of your build output exceeds the max allowed size, you might be able to reduce the size of your build output using the esbuild JavaScript bundler\. Add the following commands to the build step in your app's `amplify.yml` file\.

```
- find ./.next/standalone -type f -name "*.js" | xargs npx esbuild --minify --outdir=.next/standalone --platform=node --target=node16 --format=cjs --allow-overwrite
```

This command first runs the `find` command to search for .js files within the .next/standalone directory and its subdirectories. Then, it pipes the output of the find command to `xargs`, which takes the list of files and passes them as arguments to the `esbuild` command.

## Your build fails with an out of memory error<a name="out-of-memory"></a>

Next\.js enables you to cache build artifacts to improve performance on subsequent builds\. In addition, Amplify's AWS CodeBuild container compresses and uploads this cache to Amazon S3, on your behalf, to improve subsequent build performance\. This could cause your build to fail with an out of memory error\.

Perform the following actions to prevent your app from exceeding the memory limit during the build phase\. First, remove `.next/cache/**/*` from the cache\.paths section of your build settings\. Next, remove the `NODE_OPTIONS` environment variable from your build settings file\. Instead, set the `NODE_OPTIONS` environment variable in the Amplify console to define the Node maximum memory limit\. For more information about setting environment variables using the Amplify console, see [Set environment variables](environment-variables.md#setting-env-vars)\.

After making these changes, try your build again\. If it succeeds, add `.next/cache/**/*` back to the cache\.paths section of your build settings file\.

For more information about Next\.js cache configuration to improve build performance, see [AWS CodeBuild](https://nextjs.org/docs/advanced-features/ci-build-caching#aws-codebuild) on the Next\.js website\.
