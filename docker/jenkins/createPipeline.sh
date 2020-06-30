#!/bin/bash

cat tagdns-config.xml | java -jar jenkins-cli.jar -s http://node-master:8000 create-job tagdns
