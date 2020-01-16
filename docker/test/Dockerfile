FROM centos:7

ENV LANG C.UTF-8
ARG url=https://github.com/tuimac/tagdns.git

RUN yum update -y && \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y python36u python36u-libs python36u-devel python36u-pip && \
    yum install -y vim iproute curl iputils-ping net-tools git

WORKDIR /root
RUN git clone $url

ADD env/vimrc /root/.vimrc
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/vim.sh /etc/profile.d/vim.sh
ADD requirements.txt /root/requirements.txt
