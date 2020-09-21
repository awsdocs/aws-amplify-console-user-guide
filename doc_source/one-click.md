# Deploy to Amplify Console Button<a name="one-click"></a>

The **Deploy to Amplify Console** button enables you to share GitHub projects publicly or within your team\. The button looks like:

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/button.png)

## Add ‘Deploy to Amplify Console’ button to your repository or blog<a name="add-deploy-to-amplify-console-button-to-your-repository-or-blog"></a>

Add this button to your GitHub README\.md file, blog post, or any other markup page that renders HTML\. The button has two components:

1. An SVG image: `https://oneclick.amplifyapp.com/button.svg` 

1. The Amplify Console URL with a link to your GitHub repository\. Please copy your repo URL \(e\.g\. `https://github.com/username/repository`\) only or provide a deep link into a specific folder \(e\.g\. `https://github.com/username/repository/tree/branchname/folder`\)\. The Amplify Console will deploy the default branch in your repository\. Additional branches can be connected after the app is connected\.

1. Add the button to a markdown file \(e\.g\. your GitHub README\.md\)\. **Please replace https://github\.com/username/repository with your repository name**\.

```
[![amplifybutton](https://oneclick.amplifyapp.com/button.svg)](https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/username/repository)
```

1. You can also add the button to any HTML document:

```
<a href="https://console.aws.amazon.com/amplify/home#/deploy?repo=https://github.com/username/repository">
    <img src="https://oneclick.amplifyapp.com/button.svg" alt="Deploy to Amplify Console">
</a>
```