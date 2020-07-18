FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

ARG url=https://github.com/tuimac/tagdns.git

EXPOSE 53/udp

WORKDIR /root

ADD env/vimrc /etc/vim/vimrc.local
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD requirements.txt /root/requirements.txt
ADD .aws /root/.aws

RUN apt update && \
    apt upgrade -y && \
    apt install -y tzdata python3 python3-pip git && \
    pip3 install -r requirements.txt && \
    git clone -b v2.0.0-beta $url && \
    rm -rf anaconda-ks.cfg anaconda-post.log original-ks.cfg requirements.txt && \
    mkdir -p /etc/vim/backup && \
    mkdir -p /etc/vim/undo

#apt install -y tzdata python3 python3-pip vim* iproute2 curl net-tools dnsutils unzip git tree tcpdump iputils-ping

#WORKDIR /root/tagdns

#ENTRYPOINT ["tagdns", "&"]
