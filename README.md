# Identity Graph Proof-of-Concept using Amazon Neptune
Proof-of-Concept (PoC) for Identity Graph using Amazon Neptune

## Deployment

### Architecture [WIP]

### Step 1: Clone the github repository

```sh
git clone https://github.com/snypher/aws-poc-identity-graph.git
```

### Step 2: Create S3 bucket to store source datasets and PoC artifacts

```sh
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

Sample execution:

```sh
python3 aws-poc-identity-graph/utils/create-source-datasets.py \
--records 10000
```

Sample output from command execution

```
Creating first-party source dataset
First-party dataset output file /data/first_party_data_full.csv

Creating transactional source dataset
Transactional dataset output file: /data/transactional_data_full.csv

Generating 3000 records for public IP addresses
Generating 3000 records for Device IDs
Creating cookie and clickstream source datasets
Clickstream dataset output file: /data/clickstream_data_full.csv
Cookie dataset output file: /data/cookie_data_full.csv
```

Resulting CSV files with raw data per each dataset

* first-party: `first_party_data_full.csv`
* cookie: `cookie_data_full.csv`
* clickstream: `clickstream_data_full.csv`
* transactional: `transactional_data_full.csv`

Execution time for this process will depends on the compute resources available in your compute environment. Below are some references captured by running the script in different EC2 instance types and sizes

* A volume of 10K first-party records could take 3-4 minutes when using a t3.large EC2 instance
* A volume of 20K first-party records could take 10-11 minutes when using a t3.large EC2 instance
* A volume of 100K first-party records could take about 85 minutes when using a m6i.4xlarge EC2 instance

Additional parameters that can be optionaly used when generating raw data for source datasets:

```sh
usage: create-source-datasets.py [-h] [--records RECORDS]
                                 [--uniqueness UNIQUENESS]
                                 [--incremental {0,1}] [--debug {0,1}]

optional arguments:
  -h, --help            show this help message and exit
  --records RECORDS     Amount of mock data records to generate. Default value
                        is 10000
  --uniqueness UNIQUENESS
                        Uniqueness percentage of mock data generated for IPv4
                        addresses and Device IDs. Default value is 30
  --incremental {0,1}   Switch filenames suffix from "_data_full" to
                        "_data_inc". Suffix is used for output CSV files
                        indicating mock data generated will be used for
                        initial load or incremental loads into the graph.
                        Default value is 0
  --debug {0,1}         Turn On/Off debugging (detailed output with muck data
                        generated). Default value is 0
```

### Step 4: Upload source datasets files to S3 bucket

CSV files with raw data for initial load into the graph will be stored into the `datasets/sources/initial` S3 prefix.

```sh
AWS_ACCOUNT_ID="1234567890"
BUCKET_NAME="poc-identity-graph-${AWS_ACCOUNT_ID}"
PREFIX="datasets/sources/initial"
aws s3 cp first_party_data_full.csv s3://$BUCKET_NAME/$PREFIX/first_party/
aws s3 cp cookie_data_full.csv s3://$BUCKET_NAME/$PREFIX/cookie/
aws s3 cp clickstream_data_full.csv s3://$BUCKET_NAME/$PREFIX/clickstream/
aws s3 cp transactional_data_full.csv s3://$BUCKET_NAME/$PREFIX/transactional/
```

### Step 5: Prepare the base infrastructure (VPC, IAM, Neptune DB and Glue)

#### 5.1: Upload the CloudFormation templates to S3 bucket

```sh
AWS_ACCOUNT_ID="1234567890"
BUCKET_NAME="poc-identity-graph-${AWS_ACCOUNT_ID}"
PREFIX="cloudformation-templates"
aws s3 sync aws-poc-identity-graph/cloudformation-templates/ \
s3://$BUCKET_NAME/$PREFIX/
```

#### 5.2: Generate a new SSH key pair in the selected AWS region

Assign `ssh-key-poc-identity-graph` as key name

#### 5.3: Launch the VPC CloudFormation stack 

* This stack will create VPC resources
* CloudFormation template file: [`vpc-stack.json`](https://github.com/snypher/aws-poc-identity-graph/blob/main/cloudformation-templates/glue-stack.json)
* Use `VPC-Stack-poc-identity-graph` as Stack name

#### 5.4: Launch the IAM CloudFormation stack 

* This stack will create IAM resources
* CloudFormation template file: [`iam-stack.json`](https://github.com/snypher/aws-poc-identity-graph/blob/main/cloudformation-templates/iam-stack.json)
* Use `IAM-Stack-poc-identity-graph` as Stack name

#### 5.5: Launch the Neptune Core CloudFormation stack 

* This stack will create Neptune DB cluster and EC2 client instance
* CloudFormation template file: [`neptune-core-stack.json`](https://github.com/snypher/aws-poc-identity-graph/blob/main/cloudformation-templates/neptune-core-stack.json)
* Use `Neptune-Core-Stack-poc-identity-graph` as Stack name

#### 5.6: Launch the Neptune Workbench CloudFormation stack 

* This stack will create a SageMaker Notebook instance with Neptune Workbench
* CloudFormation template file: [`neptune-workbench-stack.json`](https://github.com/snypher/aws-poc-identity-graph/blob/main/cloudformation-templates/neptune-workbench-stack.json)
* Use `Neptune-Workbench-Stack-poc-identity-graph` as Stack name

#### 5.7: Launch the Glue CloudFormation stack 

* This stack will create:
  * Additional Glue IAM role to connect to Neptune
  * Glue database
  * Glue crawler for source datasets
  * Glue ETL Jobs to generate CSV files formated with Gremlin data format
* CloudFormation template file: [`glue-stack.json`](https://github.com/snypher/aws-poc-identity-graph/blob/main/cloudformation-templates/glue-stack.json)
* Use `Glue-Stack-poc-identity-graph` as Stack name

#### Step 6: Manually run the Glue Crawler `source-datasets-crawler-poc-identity-graph`

The crawler `source-datasets-crawler-poc-identity-graph` is in charge for scanning raw CSV files stored in S3 path `s3://poc-identity-graph-733157031621/datasets/sources/initial/`, discover schema of these source datasets and stored it into the centralized Glue Data Catalog. A glue table definition is created per each source CSV file into the Glue database `database_poc_identity_graph`.


```sh
REGION="us-east-2"
aws glue start-crawler \
--name source-datasets-crawler-poc-identity-graph \
--region $REGION
```

#### Step 7: If necessary, update schema for the Glue tables to define the correct column names

Under some circumstances, the glue crawler built-in CSV classifier can't determine a header from the first row of data in a CSV file. This lead crawler no succesfully infering the column names and types. More details can be found in the public [Glue user guide](https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html#classifier-builtin-rules).

Before running ETL jobs against source datasets stored in the Glue Data Catalog, we would need to update table metadata to set the correct column names and data type. Below are the lists of columns and data types per each source dataset

* Table `poc_identity_graph_first_party`

```
------------------------------
|          GetTable          |
+-----------------+----------+
|      Name       |  Type    |
+-----------------+----------+
|  user_name      |  string  |
|  email          |  string  |
|  phone_number   |  string  |
|  external_id    |  string  |
|  street_address |  string  |
|  postcode       |  bigint  |
|  city           |  string  |
|  country        |  string  |
|  birthday       |  string  |
|  loyalty_points |  bigint  |
|  loyalty_level  |  string  |
+-----------------+----------+
```

* Table `poc_identity_graph_cookie`

```
------------------------------------
|             GetTable             |
+-----------------------+----------+
|         Name          |  Type    |
+-----------------------+----------+
|  cookie_id            |  string  |
|  session_id           |  string  |
|  last_action          |  string  |
|  user_name            |  string  |
|  conversion_id        |  string  |
|  session_duration_sec |  bigint  |
+-----------------------+----------+
```

* Table `poc_identity_graph_clickstream`

```
------------------------------------
|             GetTable             |
+-----------------------+----------+
|         Name          |  Type    |
+-----------------------+----------+
|  session_id           |  string  |
|  client_ip            |  string  |
|  client_platform      |  string  |
|  canonical_url        |  string  |
|  domain_name          |  string  |
|  app_id               |  string  |
|  device_id            |  string  |
|  user_name            |  string  |
|  events               |  bigint  |
|  start_timestamp      |  string  |
|  start_event          |  string  |
|  end_timestamp        |  string  |
|  end_event            |  string  |
|  session_duration_sec |  bigint  |
|  user-agent           |  string  |
+-----------------------+----------+
```

* Table `poc_identity_graph_transactional`

```
--------------------------------
|           GetTable           |
+-------------------+----------+
|       Name        |  Type    |
+-------------------+----------+
|  purchase_id      |  string  |
|  product_name     |  string  |
|  purchased_date   |  string  |
|  product_category |  string  |
|  customer_id      |  string  |
|  reward_points    |  bigint  |
+-------------------+----------+
```

#### Step 8: Manually run the Glue Job `nodes-initial-load-s3-to-s3-poc-identity-graph`

The Glue ETL job `nodes-initial-load-s3-to-s3-poc-identity-graph` create gremlin-formated CSV files related to Property Graph vertices (a.k.a. entities). It extracts data from Glue tables in Glue database `database_poc_identity_graph` (a.k.a. source datasets), apply simple transformations to schema and data like de-duplication and removes nulls, and generates gremlin-formated CSV files to ingest initial data into the identity graph using the Neptune bulk loader

```sh
REGION="us-east-2"
aws glue start-job-run \
--job-name nodes-initial-load-s3-to-s3-poc-identity-graph \
--region $REGION
```

#### Step 9: Manually run the Glue Job `edges-initial-load-s3-to-s3-poc-identity-graph`

The Glue ETL job `edges-initial-load-s3-to-s3-poc-identity-graph` create gremlin-formated CSV files related to Property Graph edges (a.k.a. relationships). It extracts data from Glue tables in Glue database `database_poc_identity_graph` (a.k.a. source datasets), apply simple transformations to schema and data like de-duplication and removes nulls, and generates gremlin-formated CSV files to ingest initial data into the identity graph using the Neptune bulk loader

```sh
REGION="us-east-2"
aws glue start-job-run \
--job-name edges-initial-load-s3-to-s3-poc-identity-graph \
--region $REGION
```

### Step 10: Optionally, generate raw data simulating incremental updates from source datasets

Mock data for the below source datasets will be generated

* First-party database (e.g. CRM)
* Transactional database (e.g. purchases)
* Cookie database
* Click Stream database

Sample execution:

```sh
python3 aws-poc-identity-graph/utils/create-source-datasets.py \
--records 1000 \
--incremental 1
```

Sample output from command execution

```
Creating first-party source dataset
First-party dataset output file /data/first_party_data_inc.csv

Creating transactional source dataset
Transactional dataset output file: /data/transactional_data_inc.csv

Generating 500 records for public IP addresses
Generating 500 records for Device IDs
Creating cookie and clickstream source datasets
Clickstream dataset output file: /data/clickstream_data_inc.csv
Cookie dataset output file: /data/cookie_data_inc.csv
```

Resulting CSV files with raw data per each dataset

* first-party: `first_party_data_full.csv`
* cookie: `cookie_data_full.csv`
* clickstream: `clickstream_data_full.csv`
* transactional: `transactional_data_full.csv`

### Step 11: Optionally, upload source datasets files simulating incremental updates to S3 bucket

CSV files with raw data for incremental loads into the graph will be stored into the `datasets/sources/incremental/<DATASET_NAME>/${TIMESTAMP}` S3 prefix. Timestamp is calculated in UTC using the format `YYYYMMDD_HHmmss`.

```sh
AWS_ACCOUNT_ID="1234567890"
BUCKET_NAME="poc-identity-graph-${AWS_ACCOUNT_ID}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
PREFIX="datasets/sources/incremental"
aws s3 cp first_party_data_inc.csv s3://$BUCKET_NAME/$PREFIX/first_party/${TIMESTAMP}/
aws s3 cp cookie_data_inc.csv s3://$BUCKET_NAME/$PREFIX/cookie/${TIMESTAMP}/
aws s3 cp clickstream_data_inc.csv s3://$BUCKET_NAME/$PREFIX/clickstream/${TIMESTAMP}/
aws s3 cp transactional_data_inc.csv s3://$BUCKET_NAME/$PREFIX/transactional/${TIMESTAMP}/
```

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

[10] Faker: A Python package that generates fake data - https://faker.readthedocs.io/en/master/

[11] Neptune Python Utils: A Python 3 library that simplifies using Gremlin-Python (https://pypi.org/project/gremlinpython/) to connect to Amazon Neptune - https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils#neptune-python-utils

[12] Graph Computing - https://tinkerpop.apache.org/docs/current/reference/#graph-computing

[13] Graph Notebook: easily query and visualize graphs - https://github.com/aws/graph-notebook
