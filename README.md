# Real-time Twitter Analytics for Eurovision 2023
Streaming pipeline using Amazon MSK and Amazon EMR with Spark, retrieving the data from Twitter Streams API

**Important Notes:**
- Amazon S3 bucket (holds Spark resources and output);
- Amazon MSK cluster (using IAM Access Control);
- Amazon EKS container or an EC2 instance with the Kafka APIs installed and capable of connecting to Amazon MSK;
- Connectivity between the Amazon EKS cluster or EC2 and Amazon MSK cluster;
- Ensure the Amazon MSK Configuration has auto.create.topics.enable=true; this setting is false by default;
