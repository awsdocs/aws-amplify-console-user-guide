# Add End\-to\-End tests to your app<a name="running-tests"></a>

You now run end\-to\-end \(E2E\) tests in the test phase of your Amplify app to catch regressions before pushing code to production\. The test phase can be configured in the build specification YML and can be used to run any testing framework of your choice during a build\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/cypress.png)

## Tutorial: Set up end\-to\-end tests with Cypress<a name="tutorial-set-up-end-to-end-tests-with-cypress"></a>

Cypress is a JavaScript\-based framework that allows you to run E2E tests on a browser\. [This tutorial](http://aws.amazon.com/blogs/mobile/run-end-to-end-cypress-tests-for-your-fullstack-ci-cd-deployment-with-amplify-console/) will demonstrate how to set up E2E tests from scratch\.

## Add tests to your existing Amplify app<a name="add-tests-to-your-existing-amplify-app"></a>

You can use the test step to run any test commands at build time\. For E2E tests, the Amplify Console offers a deeper integration with Cypress that allows you to generate a UI report for your tests\. To add Cypress tests to an existing app, update your amplify\.yml build settings with the following values\.

```
test:
  phases:
    preTest:
      commands:
        - npm ci
        - npm install wait-on
        - npm install mocha@5.2.0 mochawesome mochawesome-merge mochawesome-report-generator
        - 'npm start & npx wait-on http://localhost:8080'
    test:
      commands:
        - 'npx cypress run --reporter mochawesome --reporter-options "reportDir=cypress/report/mochawesome-report,overwrite=false,html=false,json=true,timestamp=mmddyyyy_HHMMss"'
    postTest:
      commands:
        - npx mochawesome-merge cypress/report/mochawesome-report/mochawesome*.json > cypress/report/mochawesome.json
  artifacts:
    baseDirectory: cypress
    configFilePath: '**/mochawesome.json'
    files:
      - '**/*.png'
      - '**/*.mp4'
```
+  **preTest** \- Install all the dependencies required to run Cypress tests\. Amplify Console uses [mochaawesome](https://github.com/adamgruber/mochawesome) to generate a report to view your test results and [wait\-on](https://github.com/jeffbski/wait-on) to set up the localhost server during the build\.
+  **test** \- Run cypress commands to execute tests using mochawesome\.
+  **postTest** \- The mochawesome report is generated from the output JSON\.
+  **artifacts>baseDirectory** \- The directory from which tests are run\.
+ **artifacts>configFilePath** \- The generated test report data\.
+  **artifacts>files** \- The generated artifacts \(screenshots and videos\) available for download\.

## Disabling tests<a name="disabling-tests"></a>

Once the “test” config has been added to your amplify\.yml build settings, the test step will be executed for every build, on every branch\. If you would like to globally disable tests from running, or you would only like tests to run for specific branches, you can use the “USER\_DISABLE\_TESTS” environment variable to do so without modifying your build settings\.

To **globally** disable tests for all branches, add the USER\_DISABLE\_TESTS environment variable with a value of true for all branches, as shown below:

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/disable-test-global.png)

To disable tests for a **specific branch**, add the USER\_DISABLE\_TESTS environment variable with a value of false for all branches, and then add an override for each branch you would like to disable with a value of true\. In the following example, tests are disabled on the “main” branch, and enabled for every other branch:

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/amplify/latest/userguide/images/disable-test-branch.png)

Disabling tests with this variable will cause the test step to be skipped altogether during a build\. To re\-enable tests, set this value to *false*, or delete the environment variable\.