#!/bin/bash
PROG=$0
DIR="$(cd "$(dirname "${PROG}")" > /dev/null && pwd)"

cd ${DIR}/..

for image_path in images/*; do
	# TODO Should check if the image has changed, if not skip build
	image=$(basename ${image_path})
	(
		cd ${image_path}
		docker build -t anidata/twitter-data:${image} .
		cd -
	)
done
