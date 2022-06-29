#!/bin/sh -e

source $HOME/.local/bin/neptune-client-env.sh

cluster_ep="https://${NEPTUNE_CLUSTER_ENDPOINT}:${NEPTUNE_CLUSTER_PORT}/loader"

for loadId in $(awscurl --service neptune-db --region ${SERVICE_REGION} "${cluster_ep}?details=true" | jq '.payload.loadIds[]');
do
        clean_loadId=$(echo -n ${loadId} | tr -d '"')
        time=$(date -d@$(awscurl --service neptune-db --region ${SERVICE_REGION} "${cluster_ep}/${clean_loadId}?details=true" | jq '.payload.overallStatus.startTime'))
        echo -n $time '-'
        echo -n ${clean_loadId}: $(awscurl --service neptune-db --region ${SERVICE_REGION} "${cluster_ep}/${clean_loadId}?details=true" | jq '.payload.overallStatus.status')
        echo -n ',S3 LOCATION': $(awscurl --service neptune-db --region ${SERVICE_REGION} "${cluster_ep}/${clean_loadId}?details=true" | jq '.payload.overallStatus.fullUri')
        echo -n ',ERRORS': $(awscurl --service neptune-db --region ${SERVICE_REGION} "${cluster_ep}/${clean_loadId}?details=true&errors=true&page=1&errorsPerPage=3" | jq '.payload.errors.errorLogs')

        echo
done
