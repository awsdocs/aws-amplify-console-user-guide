.. _ttl:

###############################
Managing Your App's Performance
###############################

You can control how long your objects stay in a CDN cache before the CDN forwards another request to your origin. Reducing the duration enables you to serve dynamic content. Increasing the duration means your users get better performance because your objects are more likely to be served directly from the edge cache. A longer duration also reduces the load on your origin.

You can set the default TTL for your web app in the console:

1. In the console, choose **App settings** and then choose **General**. 

2. From the list of branches, choose a branch, choose **Action**, and then choose **Adjust TTL**. 

The longer you set the TTL, the better your performance. The shorter you set the TTL, the faster you can deploy. During development, we recommend setting a default TTL of 5 seconds for your branch. After your app is in production, you can increase the TTL based on your preference. We recommend that you set it to anything about 60 seconds for production traffic.
