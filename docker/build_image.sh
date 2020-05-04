#!/bin/bash

target="jenkins"

cd jenkins

docker build -t $target /home/tuimac/github/tagdns/docker/${target}
docker run -itd \
    --volume volume:/tmp \
    --publish 8000:8080 \
    --publish 50000:50000 \
    --name $target \
    --network=br0 \
    --tty yes \
    $target /bin/bash
docker start $target
