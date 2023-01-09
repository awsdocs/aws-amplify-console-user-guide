# Making environment variables accessible to server\-side runtimes<a name="ssr-environment-variables"></a>

Amplify Hosting supports adding environment variables to your application's builds by setting them in the project's configuration in the Amplify console\. However, a Next\.js server component doesn't have access to those environment variables by default\. This behavior is intentional to protect any secrets stored in environment variables that your application uses during the build phase\.

To make specific environment variables accessible to Next\.js, you can modify the Amplify build specification file to set them in the environment files that Next\.js recognizes\. Amplify needs to be able to load these environment variables before it builds the application\. The following build specification example demonstrates how to add environment variables in the build commands section\.

```
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - env | grep -e DB_HOST -e DB_USER -e DB_PASS >> .env.production
        - env | grep -e NEXT_PUBLIC_ >> .env.production
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
      - .next/cache/**/*
```

In this example, the build commands section includes two commands that add environment variables to the `.env.production` file\. Amplify Hosting allows your application to access these variables when the application receives traffic\.

The following line demonstrates how to take a specific variable from the build environment and add it to the `.env.production` file\.

```
- env | grep -e DB_HOST -e DB_USER -e DB_PASS >> .env.production
```

If the variables exist in your build environment, the `.env.production` file will contain the following\.

```
DB_HOST=localhost
DB_USER=myuser
DB_PASS=mypassword
```

The second line demonstrates how to add an environment variable with a specific prefix to the `.env.production` file\.

```
- env | grep -e NEXT_PUBLIC_ >> .env.production
```

If multiple variables with the `NEXT_PUBLIC_` prefix exist in the build environment, your `.env.production` file will look similar to the following\.

```
NEXT_PUBLIC_ANALYTICS_ID=abcdefghijk
NEXT_PUBLIC_GRAPHQL_ENDPOINT=uowelalsmlsadf
NEXT_PUBLIC_SEARCH_KEY=asdfiojslf
NEXT_PUBLIC_SEARCH_ENDPOINT=https://search-url
```