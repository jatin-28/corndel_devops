#!/bin/bash
export DATA_FOLDER=/opt/chimera/data
FILE=$HOME/all_hour.psv

FEED_FILE=$2
DATASET_NAME=$1

curl https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/$FEED_FILE | jq -r '.features[] | "\(.geometry.coordinates[1])|\(.geometry.coordinates[0])|\(.properties.place)|\(.properties.mag)"'  > $FILE

/opt/chimera/bin/cliapp --dataset-name $DATASET_NAME -i $FILE
