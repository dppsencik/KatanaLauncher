#!/usr/bin/env bash
re='^[0-9]+$'
if [[ $# -eq 0 ]]; then
    echo "ERROR: Version is not specified" >&2
    kill -INT $$
elif ! [[ $1 =~ $re ]]; then
    echo "ERROR: Version is not a number" >&2
    kill -INT $$
elif [[ ${#1} -ne 2 && ${#1} -ne 3 ]]; then
    echo "ERROR: Version is not 2 or 3 digits" >&2
    kill -INT $$!
else
    major_version=${1:0:2}
fi

export DEFAULT_RENDERER=Redshift
if [ "$major_version" = '40' ]; then
    export KATANA_RESOURCES=$KATANA_RESOURCES:/usr/redshift/redshift4katana/katana4.0v1
elif [ "$major_version" = '36' ]; then
    export KATANA_RESOURCES=$KATANA_RESOURCES:/usr/redshift/redshift4katana/katana3.5v1
elif [ "$major_version" = '35' ]; then
    export KATANA_RESOURCES=$KATANA_RESOURCES:/usr/redshift/redshift4katana/katana3.5v1
elif [ "$major_version" = '32' ]; then
    export KATANA_RESOURCES=$KATANA_RESOURCES:/usr/redshift/redshift4katana/katana3.2v1
elif [ "$major_version" = '31' ]; then
    export KATANA_RESOURCES=$KATANA_RESOURCES:/usr/redshift/redshift4katana/katana3.2v1
elif [ "$major_version" = '30' ]; then
    export KATANA_RESOURCES=$KATANA_RESOURCES:/usr/redshift/redshift4katana/katana3.0v1
elif [ "$major_version" = '26' ]; then
    export KATANA_RESOURCES=$KATANA_RESOURCES:/usr/redshift/redshift4katana/katana2.6v1
elif [ "$major_version" = '25' ]; then
    export KATANA_RESOURCES=$KATANA_RESOURCES:/usr/redshift/redshift4katana/katana2.5v4
else
    echo "redshift not available for major version $major_version"
    kill -INT $$!
fi

#todo: resolve the LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/redshift/bin