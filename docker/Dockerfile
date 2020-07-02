FROM ubuntu:latest

ARG url=https://github.com/tuimac/tagdns.git

EXPOSE 53/udp

WORKDIR /root

ADD env/vimrc /etc/vim/vimrc.local
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen

ADD requirements.txt /root/requirements.txt

RUN apt update && \
    apt upgrade -y
    apt install -y python3 vim* iproute curl net-tools bind-utils unzip git tree tcpdump && \
    pip3 install -r requirements.txt && \
    pip3 install git+$url && \
    git clone $url && \
    rm -rf anaconda-ks.cfg anaconda-post.log original-ks.cfg requirements.txt && \
    mkdir -p /etc/vim/backup && \
    mkdir -p /etc/vim/undo

ENTRYPOINT ["tagdns", "&"]
