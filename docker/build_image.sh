#!/bin/bash

target="jenkins"

docker build -t tagdns /home/tuimac/github/tagdns/docker/${target}
docker run -d -it --name ${target} $target /bin/bash
docker start $target
