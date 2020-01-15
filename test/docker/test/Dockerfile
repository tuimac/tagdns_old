FROM centos:latest

ENV LANG C.UTF-8
ARG url=https://github.com/tuimac/tagdns.git

RUN yum update -y && \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y python36u python36u-libs python36u-devel python36u-pip && \
    yum install -y vim iproute curl iputils-ping net-tools git

WORKDIR /root
RUN git clone $url && alias vi='vim'

ADD vimrc /root/.vimrc
ADD bashrc /root/.bashrc
ADD login_screen /root/.login_screen
ADD requirements.txt /root/requirements.txt
ADD vim.sh /etc/profile.d/vim.sh
