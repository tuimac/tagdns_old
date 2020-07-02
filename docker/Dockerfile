FROM centos:latest

ARG url=https://github.com/tuimac/tagdns.git

EXPOSE 53/udp

WORKDIR /root

ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/centos/vim.sh /etc/profile.d/vim.sh

ADD requirements.txt /root/requirements.txt

RUN yum update -y && \
    yum install -y python3 vim* iproute curl net-tools bind-utils unzip git tree tcpdump && \
    pip3 install -r requirements.txt && \
    pip3 install git+$url && \
    git clone $url && \
    rm -rf anaconda-ks.cfg anaconda-post.log original-ks.cfg requirements.txt && \
    mkdir -p /etc/vim/backup && \
    mkdir -p /etc/vim/undo
    
ADD env/vimrc /etc/vim/vimrc

ENTRYPOINT ["tagdns", "&"]
