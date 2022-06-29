#!/bin/sh -e

source $HOME/.local/bin/neptune-client-env.sh

cluster_ep="https://${NEPTUNE_CLUSTER_ENDPOINT}:${NEPTUNE_CLUSTER_PORT}/loader"

last_loadId=$(awscurl --service neptune-db --region ${SERVICE_REGION} "${cluster_ep}?details=true" | jq '.payload.loadIds[0]')
clean_loadId=$(echo -n ${last_loadId} | tr -d '"')
awscurl --service neptune-db --region ${SERVICE_REGION} "${cluster_ep}/${clean_loadId}?details=true&errors=true&page=1&errorsPerPage=3"

echo
