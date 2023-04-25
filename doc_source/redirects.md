# Using redirects<a name="redirects"></a>

Redirects enable a web server to reroute navigation from one URL to another\. Common reasons for using redirects include to customize the appearance of a URL, to avoid broken links, to move the hosting location of an app or site without changing its address, and to change a requested URL to the form needed by a web app\.

## Types of redirects<a name="types-of-redirects"></a>

There are several types of redirects that support specific scenarios\.

 **Permanent redirect \(301\)** 

301 redirects are intended for lasting changes to the destination of a web address\. Search engine ranking history of the original address applies to the new destination address\. Redirection occurs on the client\-side, so a browser navigation bar shows the destination address after redirection\.

Common reasons to use 301 redirects include:
+ To avoid a broken link when the address of a page changes\.
+ To avoid a broken link when a user makes a predictable typo in an address\.

 **Temporary redirect \(302\)** 

302 redirects are intended for temporary changes to the destination of a web address\. Search engine ranking history of the original address doesn’t apply to the new destination address\. Redirection occurs on the client\-side, so a browser navigation bar shows the destination address after redirection\.

Common reasons to use 302 redirects include:
+ To provide a detour destination while repairs are made to an original address\.
+ To provide test pages for A/B comparison of a user interface\.

 **Rewrite \(200\)** 

200 redirects \(rewrites\) are intended to show content from the destination address as if it were served from the original address\. Search engine ranking history continues to apply to the original address\. Redirection occurs on the server\-side, so a browser navigation bar shows the original address after redirection\. Common reasons to use 200 redirects include:
+ To redirect an entire site to a new hosting location without changing the address of the site\.
+ To redirect all traffic to a single page web app \(SPA\) to its index\.html page for handling by a client\-side router function\.

 **Not Found \(404\)** 

404 redirects occur when a request points to an address that doesn’t exist\. The destination page of a 404 is displayed instead of the requested one\. Common reasons a 404 redirect occurs include:
+ To avoid a broken link message when a user enters a bad URL\.
+ To point requests to nonexistent pages of a web app to its index\.html page for handling by a client\-side router function\.

## Creating and editing redirects<a name="parts-of-a-redirect"></a>

You can create and edit redirects for an app in the Amplify console\. Before you get started, you will need the following information about the parts of a redirect\.

**An original address**  
The address the user requested\.

**A destination address**  
The address that actually serves the content that the user sees\.

**A redirect type**  
Types include a permanent redirect \(301\), a temporary redirect \(302\), a rewrite \(200\), or not found \(404\)\.

**A two letter country code \(optional\)**  
A value you can include to segment the user experience of your app by geographical region\.

**To create a redirect in the Amplify console**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/)\.

1. Choose the app you want to create a redirect for\.

1. In the navigation pane, choose **App settings**, and then choose **Rewrites and redirects**\.

1. In the **Rewrites and redirects** section, choose **Edit**\.

1. The procedure for adding a redirect varies depending on whether you want to add rules individually or do a bulk edit:
   + To create an individual redirect, choose **Add rule**\.

     1. For **Source address**, enter the original address the user requested\.

     1. For **Target address**, enter the destination address that renders the content to the user\.

     1. For **Type**, choose the type of redirect from the list\.

     1. \(Optional\) For **Country code**, enter a two letter country code condition\.
   + To bulk edit redirects, choose **Open text editor**\.

     1. Manually add or update redirects in the **Bulk add rewrites and redirects** JSON editor\.

1. Choose **Save**\.

## Order of redirects<a name="order-of-redirects"></a>

Redirects are executed from the top of the list down\. Make sure that your ordering has the effect you intend\. For example, the following order of redirects causes all requests for a given path under */docs/* to redirect to the same path under */documents/*, except */docs/specific\-filename\.html* which redirects to */documents/different\-filename\.html*:

```
/docs/specific-filename.html /documents/different-filename.html 301
/docs/<*> /documents/<*>
```

The following order of redirects ignores the redirection of *specific\-filename\.html* to *different\-filename\.html*:

```
/docs/<*> /documents/<*>
/docs/specific-filename.html /documents/different-filename.html 301
```

## Query parameters<a name="query-parameters"></a>

You can use query parameters for more control over your URL matches\. Amplify forwards all query parameters to the destination path for 301 and 302 redirects, with the following exceptions:
+ If the original address includes a query string set to a specific value, Amplify doesn't forward query parameters\. In this case, the redirect only applies to requests to the destination URL with the specified query value\. 
+ If the destination address for the matching rule has query parameters, query parameters aren't forwarded\. For example, if the destination address for the redirect is `https://example-target.com?q=someParam`, query parameters aren't passed through\.

## Simple redirects and rewrites<a name="simple-redirects-and-rewrites"></a>

In this section we include example code for common redirect scenarios\.

You can use the following example code to permanently redirect a specific page to a new address\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `/original.html`   |   `/destination.html`   |   `permanent redirect (301)`   |  | 

JSON \[\{"source": "/original\.html", "status": "301", "target": "/destination\.html", "condition": null\}\] 

You can use the following example code to redirect any path under a folder to the same path under a different folder\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `docs/<*>`   |   `/documents/<*>`   |   `permanent redirect (301)`   |  | 

 JSON \[\{"source": "/docs/<\*>", "status": "301", "target": "/documents/<\*>", "condition": null\}\] 

You can use the following example code to redirect all traffic to index\.html as a rewrite\. In this scenario, the rewrite makes it appear to the user that they have arrived at the original address\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `/<*>`   |   `/index.html`   |   `rewrite (200)`   |  | 

 JSON \[\{"source": "/<\*>", "status": "200", "target": "/index\.html", "condition": null\}\] 

You can use the following example code to use a rewrite to change the subdomain that appears to the user\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `https://mydomain.com`   |   `https://www.mydomain.com`   |   `rewrite (200)`   |  | 

 JSON \[\{"source": "https://mydomain\.com", "status": "200", "target": "https://www\.mydomain\.com", "condition": null\}\] 

You can use the following example code to redirect paths under a folder that can’t be found to a custom 404 page\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `/<*>`   |   `/404.html`   |   `not found (404)`   |  | 

 JSON \[\{"source": "/<\*>", "status": "404", "target": "/404\.html", "condition": null\}\] 

## Redirects for single page web apps \(SPA\)<a name="redirects-for-single-page-web-apps-spa"></a>

Most SPA frameworks support HTML5 history\.pushState\(\) to change browser location without triggering a server request\. This works for users who begin their journey from the root \(or */index\.html*\), but fails for users who navigate directly to any other page\. 

The following example uses regular expressions to set up a 200 rewrite for all files to index\.html, except for the file extensions specified in the regular expression\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `</^[^.]+$\|\.(?!(css\|gif\|ico\|jpg\|js\|png\|txt\|svg\|woff\|woff2\|ttf\|map\|json\|webp)$)([^.]+$)/>`   |   `/index.html`   |   `200`   |  | 

JSON \[\{"source": "</^\[^\.\]\+$\|\\\.\(?\!\(css\|gif\|ico\|jpg\|js\|png\|txt\|svg\|woff\|woff2\|ttf\|map\|json\|webp\)$\)\(\[^\.\]\+$\)/>", "status": "200", "target": "/index\.html", "condition": null\}\]

## Reverse proxy rewrite<a name="reverse-proxy-rewrite"></a>

The following example uses a rewrite to proxy content from another location so that it appears to the user that the domain hasn’t changed\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `/images/<*>`   |   `https://images.otherdomain.com/<*>`   |   `rewrite (200)`   |  | 

JSON \[\{"source": "/images/<\*>", "status": "200", "target": "https://images\.otherdomain\.com/<\*>", "condition": null\}\]

## Trailing slashes and clean URLs<a name="trailing-slashes-and-clean-urls"></a>

To create clean URL structures like *about* instead of *about\.html*, static site generators such as Hugo generate directories for pages with an index\.html \(*/about/index\.html*\)\. Amplify automatically creates clean URLs by adding a trailing slash when required\. The table below highlights different scenarios:


****  

| User inputs in browser | URL in the address bar | Document served | 
| --- | --- | --- | 
|   `/about`   |   `/about`   |   `/about.html`   | 
|   `/about (when about.html returns 404)`   |   `/about/`   |   `/about/index.html`   | 
|   `/about/`   |   `/about/`   |   `/about/index.html`   | 

## Placeholders<a name="placeholders"></a>

You can use the following example code to redirect paths in a folder structure to a matching structure in another folder\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `/docs/<year>/<month>/<date>/<itemid>`   |   `/documents/<year>/<month>/<date>/<itemid>`   |   `permanent redirect (301)`   |  | 

 JSON \[\{"source": "/docs/<year>/<month>/<date>/<itemid>", "status": "301", "target": "/documents/<year>/<month>/<date>/<itemid>", "condition": null\}\] 

## Query strings and path parameters<a name="query-strings-and-path-parameters"></a>

You can use the following example code to redirect a path to a folder with a name that matches the value of a query string element in the original address:


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `/docs?id=<my-blog-id-value`   |   `/documents/<my-blog-post-id-value>`   |   `permanent redirect (301)`   |  | 

 JSON \[\{"source": "/docs?id=<my\-blog\-id\-value>", "status": "301", "target": "/documents/<my\-blog\-id\-value>", "condition": null\}\] 

**Note**  
Amplify forwards all query string parameters to the destination path for 301 and 302 redirects\. However, if the original address includes a query string set to a specific value, as demonstrated in this example, Amplify doesn't forward query parameters\. In this case, the redirect applies only to requests to the destination address with the specified query value `id`\.

You can use the following example code to redirect all paths that can’t be found at a given level of a folder structure to index\.html in a specified folder\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `/documents/<folder>/<child-folder>/<grand-child-folder>`   |   `/documents/index.html`   |   `404`   |  | 

 JSON \[\{"source": "/documents/<x>/<y>/<z>", "status": "404", "target": "/documents/index\.html", "condition": null\}\] 

## Region\-based redirects<a name="region-based-redirects"></a>

You can use the following example code to redirect requests based on region\.


****  

| Original address | Destination Address | Redirect Type | Country Code | 
| --- | --- | --- | --- | 
|   `/documents`   |   `/documents/us/`   |   `302`   |   `<US>`   | 

JSON \[\{"source": "/documents", "status": "302", "target": "/documents/us/", "condition": "<US>"\}\]