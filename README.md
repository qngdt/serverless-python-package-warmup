# Example with serverless-package-python-functions and serverless-plugin-warmup

Running `serverless package` would output this error
```
Packaging aws-python-http-api-project for stage dev (us-east-1)
WarmUp: Creating warmer "default" to warm up 1 function
[serverless-package-python-functions] Packaging hello...
Environment: darwin, node 16.13.1, framework 3.8.0, plugin 6.1.6, SDK 4.3.2
Docs:        docs.serverless.com
Support:     forum.serverless.com
Bugs:        github.com/serverless/serverless/issues

Error:
Cannot access package artifact at "_build/aws-python-http-api-project-dev-warmup-plugin-default.zip" (for "warmUpPluginDefault"): ENOENT: no such file or directory, access 'aws-python-http-api-project/_build/aws-python-http-api-project-dev-warmup-plugin-default.zip'
```