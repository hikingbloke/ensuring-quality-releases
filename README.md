# Ensure Quality Releases

### Introduction
In this project, We will develop and demonstrate skills in using a variety of industry leading tools, especially Microsoft Azure, to create disposable test environments and run a variety of automated tests with the click of a button. Additionally, we monitor and provide insight into your application's behavior, and determine root causes by querying the application’s custom log files.

A high-level walk-through of the project:
The project takes you all the way through the creation of the environment,
the delivery of the software, the automated testing of the software,
and the performance monitoring of the environment under different low conditions.

Following are the steps we will go through
1. The first thing we'll do is start with Terraform.  
   It will create the resources we need, like the VM and the AppService.  
2. Add the execution of the test suites (created using Postman) to the Azure DevOps, CI/CD pipeline.  
3. We'll create the test suite for JMeter.  
4. We'll create the functional UI test suite and output the print statements to a log file.  
   We'll configure log analytics to ingest the Selenium log file.  
5. We'll create the alert for the app service using Azure Monitor.  

### Architectural Diagram
![screenshot - Architectural Diagram](./output_files/1.architecture-diagram.png?raw=true)

### Project Resources
1. Create an [Azure Account](https://portal.azure.com) 
2. Install the [Azure command line interface](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
3. Create a [Github Account](https://www.github.com)
4. Create a disposable [Outlook account](https://outlook.com/)
5. [Create an Azure DevOps account](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)
6. Use your favorite text editor or IDE - for this I used [VS Code](https://code.visualstudio.com/Download)

### Dependencies
- [Terraform](https://www.terraform.io/downloads.html)
- [JMeter](https://jmeter.apache.org/download_jmeter.cgi)
- [Postman](https://www.postman.com/downloads/)
- [Python](https://www.postman.com/downloads/)
- [Selenium](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

### Installation & Configuration:
[Configure the storage account and state backend.](https://docs.microsoft.com/en-us/azure/terraform/terraform-backend) Replace the values below in terraform/environments/test/main.tf with the output from the Azure CLI:
- storage_account_name
- container_name
- access_key

[Create a Service Principal for Terraform](https://www.terraform.io/docs/providers/azurerm/guides/service_principal_client_secret.html) Replace the below values in terraform/environments/test/terraform.tfvars with the output from the Azure CLI:
- subscription_id
- client_id
- client_secret
- tenant_id

### Azure DevOps
[Follow the instructions](https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=java%2Cyaml%2Cbrowser%2Ctfs-2018-2) to create a new Azure Pipeline from the `azure-pipelines.yaml` file.

### Improvements
- Deploy terraform using Azure DevOps.
- Improve writing Postman scripts for more test coverage.
- Improve skills on JMeter, Selenium

### Output
- Teraform files and results
https://github.com/hikingbloke/ensuring-quality-releases/tree/master/terraform
https://github.com/hikingbloke/ensuring-quality-releases/tree/master/terraform/modules

![screenshot - Terraform Init](./output_files/2_terraform_init.png?raw=true)
![screenshot - Terraform plan](./output_files/3_terraform_plan.png?raw=true)

- Azure pipeline execution
https://dev.azure.com/mytechstuffbipin/DevOps/_build/results?buildId=118&view=results

![screenshot - Azure Pipeline Summary](./output_files/4_azure_pipeline-execution_1.png?raw=true)
![screenshot - Azure Pipeline Breakdown 1](./output_files/4_azure_pipeline-execution_2.png?raw=true)
![screenshot - Azure Pipeline Breakdown 2](./output_files/4_azure_pipeline-execution_3.png?raw=true)

- Postman Collection and Environment
    - Data Validation Tests
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/automatedtesting/postman/DataValidationTestSuite.json

    - Regression Test Suite
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/automatedtesting/postman/RegressionTestSuite.json

    - Variabes
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/automatedtesting/postman/MyEnvironment.json

![screenshot - Data Validation test results](./output_files/5_postman-data-validation-test-results.png?raw=true)
![screenshot - Regression test results](./output_files/5_postman-regression-test-results.png?raw=true)

- Selenium
A zip archive of the Selenium python files. A screenshot of the successful execution of the Test Suite on a VM in Azure DevOps should contain which user logged in, which items were added to the cart, and which items were removed from the cart.
![screenshot - Selenium test result](./output_files/6-selenium-test-results.png?raw=true)

- JMeter
![screenshot - Jmeter DevOps test results](./output_files/7_Jmeter-devops-test-results.png?raw=true)

- Endurance Tests
    - Test Report
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/output_files/7_Jmeter-endurance_test_report.7z

    - CSV output
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/output_files/7_Jmeter-csv-edurance-test-output-results.7z

    - PDF report
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/output_files/7_Jmeter-endurance-test-report.pdf

![screenshot - Endurance Test Suite](./output_files/7_Jmeter-endurance-test-suite.png?raw=true)
![screenshot - Endurance Test Suite Report 1](./output_files/7_Jmeter-endurance-test-report_1.png?raw=true)
![screenshot - Endurance Test Suite Report 2](./output_files/7_Jmeter-endurance-test-report_2.png?raw=true)

- Stress Tests
    - Test Report
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/output_files/7_Jmeter-stress_test_report.7z

    - CSV output
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/output_files/7_Jmeter-csv-stress-test-output-results.7z

    - PDF report
        https://github.com/hikingbloke/ensuring-quality-releases/blob/master/output_files/7_Jmeter-stress-test-report.pdf

![screenshot - Stress Test Suite](./output_files/7_Jmeter-stress-test-suite.png?raw=true)
![screenshot - Stress Test Suite Report 1](./output_files/7_Jmeter-stress-test-report_1.png?raw=true)
![screenshot - Stress Test Suite Report 2](./output_files/7_Jmeter-stress-test-report_2.png?raw=true)


- Azure Alert
Screenshots of the email received when the alert is triggered, the graphs of the resource that the alert was triggered for (be sure to include timestamps for the email and the graphs), and the alert rule, which will show the resource, condition, action group, alert name, and severity. Screenshots for the resource’s metrics will correspond to the approximate time that the alert was triggered.
![screenshot - email revceived](./output_files/8_azure-email-alert.png?raw=true)
![screenshot - alert rules](./output_files/8_azure-alert-rules.png?raw=true)
![screenshot - alert graphn](./output_files/8_azure-alert-graph.png?raw=true)
![screenshot - Resource metrics](./output_files/8_web-app-metrics.png?raw=true)

- Log Analytics queries
Screenshots of log analytics queries and result sets which will show specific output of the Azure resource. 
![screenshot - Log Analytics query 1](./output_files/9_log-analytics-query_1.png?raw=true)
![screenshot - Log Analytics query 2](./output_files/9_log-analytics-query_2.png?raw=true)
![screenshot - Log Analytics query 3](./output_files/9_log-analytics-query-webapplogs.png?raw=true)

The result set will include the output of the execution of the Selenium Test Suite.
* currently facing diffcuts fot custom logs not showing for log analaytics to query *
