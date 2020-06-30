#!/bin/bash

cat config/tagdns-config.xml | java -jar lib/jenkins-cli.jar -s http://localhost:8000 create-job tagdns
