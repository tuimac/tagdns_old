#!/bin/bash

target="tagdns"

docker build -t $target ${HOME}/tagdns/docker/${target}
docker run -itd \
    --publish 53:53 \
    --name $target \
    --network=br0 \
    --tty yes \
    $target /bin/bash
docker start $target
