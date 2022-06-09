# Identity Graph Proof-of-Concept using Amazon Neptune
Proof-of-Concept (PoC) for Identity Graph using Amazon Neptune

## Deployment

### Architecture [WIP]

### Step 1: Clone the github repository

```
git clone https://github.com/snypher/aws-poc-identity-graph.git
```

### Step 2: Create S3 bucket to store source datasets and PoC artifacts

```
BUCKET_NAME="poc-identity-graph-733157031621"
REGION="us-east-2"
aws s3 mb s3://$BUCKET_NAME \
--region $REGION
aws s3api put-bucket-encryption \
--bucket $BUCKET_NAME \
--server-side-encryption-configuration '{"Rules": 
[{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'
aws s3api put-bucket-tagging \
--bucket $BUCKET_NAME \
--tagging 'TagSet=[{Key=auto-delete,Value=never},
{Key=Environment,Value=ab3},{Key=CreatedBy,Value=chvezk}]'
aws s3api put-bucket-versioning \
--bucket $BUCKET_NAME \
--versioning-configuration Status=Enabled
```

### Step 3: Generate raw data for source datasets

Mock data for the below source datasets will be generated

* First-party database (e.g. CRM)
* Transactional database (e.g. purchases)
* Cookie database
* Click Stream database

Generating a volume of 10K first-party records could take 3-4 minutes. A volume of 20K first-party records could take 10-11 minutes.

```
python3 aws-poc-identity-graph/utils/create-source-datasets.py \
--records 10000
```

Sample output from command execution

```
Creating first-party source dataset
First-party dataset output file /data/first_party_data_full.csv

Creating transactional source dataset
Transactional dataset output file: /data/transactional_data_full.csv

Creating cookie and clickstream source datasets
Clickstream dataset output file: /data/clickstream_data_full.csv
Cookie dataset output file: /data/cookie_data_full.csv
```

Resulting CSV files with raw data per each dataset

* `first_party_data_full.csv`
* `cookie_data_full.csv`
* `clickstream_data_full.csv`
* `transactional_data_full.csv`

### Step 4: Upload source datasets files to S3 bucket

CSV files with raw data will be stored into the `datasets` S3 prefix

```
BUCKET_NAME="poc-identity-graph-733157031621"
PREFIX="datasets"
aws s3 cp first_party_data_full.csv s3://$BUCKET_NAME/$PREFIX/first_party/
aws s3 cp cookie_data_full.csv s3://$BUCKET_NAME/$PREFIX/cookie/
aws s3 cp clickstream_data_full.csv s3://$BUCKET_NAME/$PREFIX/clickstream/
aws s3 cp transactional_data_full.csv s3://$BUCKET_NAME/$PREFIX/transactional/
```

### Step 5: Prepare the base infrastructure (VPC, IAM, Neptune DB and Glue)

* Upload the base CloudFormation templates to S3 bucket

```
BUCKET_NAME="poc-identity-graph-733157031621"
PREFIX="cloudformation-templates"
aws s3 sync aws-poc-identity-graph/cloudformation-templates/ \
s3://$BUCKET_NAME/$PREFIX/
```

* Generate a new SSH key pair in the selected AWS region. Assign `ssh-key-poc-identity-graph` as key name.
* Launch the CloudFormation stack `s3://poc-identity-graph-733157031621/cloudformation-templates/vpc-stack.json` to create VPC resources. Use `VPC-Stack-poc-identity-graph` as Stack name

* Launch the CloudFormation stack `s3://poc-identity-graph-733157031621/cloudformation-templates/iam-stack.json` to create IAM resources. Use `IAM-Stack-poc-identity-graph` as Stack name

* Launch the CloudFormation stack `s3://poc-identity-graph-733157031621/cloudformation-templates/neptune-core-stack.json` to create Neptune DB cluster and EC2 client instance. Use `Neptune-Core-Stack-poc-identity-graph` as Stack name
* Launch the CloudFormation stack `s3://poc-identity-graph-733157031621/cloudformation-templates/neptune-workbench-stack.json` to create Neptune DB cluster and EC2 client instance. Use `Neptune-Workbench-Stack-poc-identity-graph` as Stack name
* Launch the CloudFormation stack `s3://poc-identity-graph-733157031621/cloudformation-templates/glue-stack.json` to create additional Glue IAM role to connect to Neptune, Glue database and Glue crawler for source datasets. Use `Glue-Stack-poc-identity-graph` as Stack name

## References

[1] Identity Graphs on AWS - https://aws.amazon.com/neptune/identity-graphs-on-aws/

[2] Building a customer identity graph with Amazon Neptune - https://aws.amazon.com/blogs/database/building-a-customer-identity-graph-with-amazon-neptune/

[3] Data Modeling for Identity Graphs - https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/03-Sample-Applications/03-Identity-Graphs/02-Data-Modeling-for-Identity-Graphs.ipynb

[4] Graph Data Modelling - https://github.com/aws-samples/aws-dbs-refarch-graph/tree/master/src/graph-data-modelling#graph-data-modelling

[5] Reference Architectures for Graph Databases on AWS - https://github.com/aws-samples/aws-dbs-refarch-graph/

[6] Data Models and Query Languages - https://github.com/aws-samples/aws-dbs-refarch-graph/tree/master/src/data-models-and-query-languages

[7] Accessing Amazon Neptune from AWS Lambda Functions - https://aws-samples.github.io/aws-dbs-refarch-graph/src/accessing-from-aws-lambda/

[8] Migrating from MySQL to Amazon Neptune using AWS Glue - https://github.com/aws-samples/amazon-neptune-samples/tree/master/gremlin/glue-neptune

[9] Amazon Neptune Tools - https://github.com/awslabs/amazon-neptune-tools

[10] Graph Computing - https://tinkerpop.apache.org/docs/current/reference/#graph-computing

[11] Populating your graph in Amazon Neptune from a relational database using AWS Database Migration Service (DMS)

* https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-1-setting-the-stage/
* https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-2-designing-the-property-graph-model/
* https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-3-designing-the-rdf-model/
* https://aws.amazon.com/blogs/database/populating-your-graph-in-amazon-neptune-from-a-relational-database-using-aws-database-migration-service-dms-part-4-putting-it-all-together/

[12] Graph Notebook: easily query and visualize graphs - https://github.com/aws/graph-notebook

