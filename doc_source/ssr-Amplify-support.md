# Amplify support for Next\.js SSR<a name="ssr-Amplify-support"></a>

Amplify supports deployment and hosting for server\-side rendered \(SSR\) web apps created using Next\.js only\. Next\.js is a React framework for developing SPAs with JavaScript\. You can deploy apps built with Next\.js 13 with features such as image and script optimization, Incremental Static Regeneration \(ISR\), and middleware\.

Developers can use Next\.js to combine static site generation \(SSG\), and SSR in a single project\. SSG pages are prerendered at build time, and SSR pages are prerendered at request time\. 

Prerendering can improve performance and search engine optimization\. Because Next\.js prerenders all pages on the server, the HTML content of each page is ready when it reaches the client's browser\. This content can also load faster\. Faster load times improve the end user's experience with a website and positively impact the site's SEO ranking\. Prerendering also improves SEO by enabling search engine bots to find and crawl a website's HTML content easily\.

Next\.js provides built\-in analytics support for measuring various performance metrics, such as Time to first byte \(TTFB\) and First contentful paint \(FCP\)\. For more information about Next\.js, see [Getting started](https://nextjs.org/docs/getting-started) on the Next\.js website\.

## Next\.js feature support<a name="supported-unsupported-features"></a>

Amplify Hosting compute fully manages server\-side rendering \(SSR\) for apps built with Next\.js 12 or later\. If you deployed a Next\.js app to Amplify prior to the release of Amplify Hosting compute, your app is using Amplify's previous SSR provider, Classic \(Next\.js 11 only\)\. Amplify Hosting compute doesn't support apps created using Next\.js version 11 or earlier\. We strongly recommend that you migrate your Next\.js 11 apps to the Amplify Hosting compute managed SSR provider\.

The following list describes the specific features that the Amplify Hosting compute SSR provider supports\.

**Supported features**
+ Server\-side rendered pages \(SSR\)
+ Static pages
+ API routes
+ Dynamic routes
+ Catch all routes
+ SSG \(Static generation\)
+ Incremental Static Regeneration \(ISR\)
+ Internationalized \(i18n\) sub\-path routing
+ Internationalized \(i18n\) domain routing
+ Middleware
+ Environment variables
+ Image optimization\.

**Unsupported features**
+ Edge API routes
+ On\-Demand Incremental Static Regeneration \(ISR\)
+ Internationalized \(i18n\) automatic locale detection
+ Next\.js 13 app directory \(beta\)

### Using Next\.js image optimization<a name="image-optimization"></a>

The Next\.js documentation advises you to install the Sharp image processing module to enable image optimization to work correctly in production\. However, this isn't necessary for Amplify deployments\. Amplify automatically deploys Sharp for you\.

The maximum output size of the image can't exceed 4\.3 MB\. You can have a larger image file stored somewhere and use the `next/image` component to resize and optimize it into a Webp or AVIF format and then serve it as a smaller size\.