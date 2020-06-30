FROM jenkins/jenkins:lts

MAINTAINER tuimac

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

USER root
WORKDIR /root

EXPOSE 8080
EXPOSE 50000

ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/vimrc /etc/vim/vimrc.local
ADD plugins.txt /usr/share/jenkins/ref/plugins.txt
ADD requirements.txt /root/requirements.txt
ADD jenkins-cli.jar /root/jenkins-cli.jar
ADD tagdns-config.xml /root/tagdns-config.xml
ADD createPipeline.sh /root/createPipeline.sh

RUN apt update && \
    apt upgrade -y && \
    apt install -y vim* traceroute net-tools dnsutils python-pip python3-pip && \
    /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt && \
    mkdir -p /etc/vim/undo && \
    mkdir -p /etc/vim/backup && \
    mkdir -p /usr/share/jenkins/ref/casc_configs && \
    pip3 install -r requirements.txt

ADD env/vimrc /etc/vim/vimrc.local
ADD jenkins.yaml /usr/share/jenkins/ref/casc_configs/jenkins.yaml
