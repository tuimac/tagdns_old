#!/bin/bash

target="tagdns"

docker build -t $target ${HOME}/tagdns/docker/${target}
docker container create -it \
    --name $target \
    --network=br0 \
    $target /bin/bash
docker start $target
