#!/bin/bash

ID=$(docker container ls --filter name=tagdns)

if [ $ID != "" ]; then
    echo hello
fi
