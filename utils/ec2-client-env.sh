# Setting env with AWS temporary credentials
ROLE_NAME=$(curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/)
CREDS_JSON=$(curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/${ROLE_NAME})

export AWS_ACCESS_KEY_ID=$(echo ${CREDS_JSON} | jq .AccessKeyId | tr -d '"')
export AWS_SECRET_ACCESS_KEY=$(echo ${CREDS_JSON} | jq .SecretAccessKey | tr -d '"')
export AWS_SESSION_TOKEN=$(echo ${CREDS_JSON} | jq .Token | tr -d '"')
export SERVICE_REGION=us-east-2
export NEPTUNE_CLUSTER_ENDPOINT=$(aws neptune describe-db-clusters --region ${SERVICE_REGION} --query 'DBClusters[0].Endpoint' --output text)
export NEPTUNE_CLUSTER_PORT=$(aws neptune describe-db-clusters --region ${SERVICE_REGION} --query 'DBClusters[0].Port' --output text)

alias neptune-status="awscurl https://${NEPTUNE_CLUSTER_ENDPOINT}:${NEPTUNE_CLUSTER_PORT}/status --service neptune-db --region ${SERVICE_REGION}"