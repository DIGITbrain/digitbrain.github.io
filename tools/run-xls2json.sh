#!/bin/bash

set +ex

if [ -z "$1" ] ; then
	echo "Argument is missing. Please, specify an excel file (describing a dma) as argument!"
  exit 1
fi

SCRIPTDIR=`dirname "$0"`
source $SCRIPTDIR/env/xls2json/bin/activate

python $SCRIPTDIR/exceltojson.py $1

