FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

ARG url=https://github.com/tuimac/tagdns.git

EXPOSE 53/udp

WORKDIR /root

ADD env/vimrc /etc/vim/vimrc.local
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen

ADD requirements.txt /root/requirements.txt

<<<<<<< HEAD
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y tzdata python3 python3-pip vim* iproute2 curl net-tools bind9-utils unzip git tree tcpdump && \
=======
RUN apt update && \
    apt upgrade -y
    apt install -y python3 vim* iproute curl net-tools dnsutils unzip git tree tcpdump && \
>>>>>>> 90b2f212555947bbb10914fa9f061a3c0ed274f3
    pip3 install -r requirements.txt && \
    pip3 install git+$url && \
    git clone $url && \
    rm -rf anaconda-ks.cfg anaconda-post.log original-ks.cfg requirements.txt && \
    mkdir -p /etc/vim/backup && \
    mkdir -p /etc/vim/undo

ENTRYPOINT ["tagdns", "&"]
