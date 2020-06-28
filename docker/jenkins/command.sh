#!/bin/bash

cat /root/tagdns/docker/jenkins/tagdns-config.xml | java -jar /root/tagdns/docker/jenkins/jenkins-cli.jar -s http://localhost:8080 create-job tagdns

java -jar jenkins-cli.jar -s http://node-master:8000 get-job tagdns > tagdns-config.xml


# Access "http://localhost:8080/script"

Jenkins.instance.pluginManager.plugins.each{
  plugin -> 
    println ("${plugin.getShortName()}")
}
