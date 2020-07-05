#!/bin/bash

ID=$(docker container ls --filter name=tagdns -q)
echo $ID

if [ ! $ID == "" ]; then
    echo hello
fi
