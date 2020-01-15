FROM centos:7

ARG url=https://github.com/tuimac/tagdns.git
ENV LANG C.UTF-8

RUN yum update -y && \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y python36u python36u-libs python36u-devel python36u-pip && \
    yum install -y vim iproute curl iputils-ping net-tools unzip git

EXPOSE 53
WORKDIR /root
RUN git clone $url

ADD vimrc /root/.vimrc
ADD bashrc /root/.bashrc
ADD login_screen /root/.login_screen
ADD requirements.txt /root/requirements.txt
ADD vim.sh /etc/profile.d/vim.sh

RUN pip3 install -r requirements.txt
#RUN python3 tagdns/src/main.py
