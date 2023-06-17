# Infrastructure as Code with Terraform

We have already seen how to deploy a spark job in [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html) manually. 
Now, we will see how to deploy the infrastructure using Terraform.


## Pre-requisites

- [Terraform](https://www.terraform.io/downloads.html)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [AWS Account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Getting Started

You need to pack your dependencies in a `tar.gz` file and upload it to S3. This is done by running the following command:

```bash
cd dependencies
DOCKER_BUILDKIT=1 docker build --output . .
```

You will see the output file under the `dependencies` directory.

But first, you need to have an AWS account and a bucket. So let's deploy the infrastructure.


## Deploying the infrastructure

Locate yourself under the `terraform` directory and run the following commands:

```bash
aws configure  # enter your AWS credentials

terraform init
terraform plan  # this is optional, it will show you what will be deployed - check that 4 resources will be created
terraform apply
```

You will see the following output:

```bash
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

spark_arn = "arn:aws:emr-serverless:eu-west-1:xx:/applications/xx"
spark_id = "xx"
```

Now, check on your AWS Account that everything has been created. You should see two folders, `artifacts` and `code` under your
S3 bucket. Also, you should see a new EMR Serverless Application called `spark-emr-serverless` and a new EMR Serverless 
Cluster called `spark-emr-serverless-cluster`.


Now, you have to upload the `pyspark_ge.tar.gz` file to the `artifacts` folder in your S3 bucket and your python file to 
the `code` folder. You can do this manually or using the aws cli.

We'll be using the `dates_solution.py` as the sample file to upload to S3 and run the Spark Job.

```bash
aws s3 cp pyspark_ge.tar.gz s3://<your-bucket-name>/artifacts/pyspark_ge.tar.gz
aws s3 cp dates_solution.py s3://<your-bucket-name>/code/dates_solution.py
```


## Running the Spark Job

Now, you can run the Spark Job by going to Amazon EMR > EMR Serverless (new) and click on `Get Started`, make sure 
you're in the right AWS region. Click on `Applications` under `Serverless` and `Submit job`.

`Name`: The name you want to give to your Spark Job

`Runtime role`: Select/create one with the default settings

`Script location`: s3://<your-bucket-name>/code/dates_solution.py

`Script arguments`: s3://<your-bucket-name>/output/dates/ (this is the output folder where the results will be stored)

Spark properties *(edit as text)*: --conf spark.driver.cores=1 --conf spark.driver.memory=2g --conf spark.executor.cores=4 --conf spark.executor.memory=4g --conf spark.executor.instances=2 --conf spark.archives=s3://<your-bucket-name>/artifacts/pyspark_ge.tar.gz#environment --conf spark.emr-serverless.driverEnv.PYSPARK_DRIVER_PYTHON=./environment/bin/python --conf spark.emr-serverless.driverEnv.PYSPARK_PYTHON=./environment/bin/python --conf spark.emr-serverless.executorEnv.PYSPARK_PYTHON=./environment/bin/python --conf spark.hadoop.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory


Finally, click on `Submit job` and wait for the results. You can check the logs by clicking on the `Job ID` and then on `Logs`.

Check the `output` folder in your S3 bucket to see the results.
