FROM centos:7

ARG url=https://github.com/tuimac/tagdns.git
ENV LANG C.UTF-8

EXPOSE 53
WORKDIR /root

ADD env/vimrc /root/.vimrc
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/centos/vim.sh /etc/profile.d/vim.sh
ADD requirements.txt /root/requirements.txt
ADD .aws /root/.aws

RUN yum update -y && \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum remove -y vi && \
    yum install -y python36u python36u-libs python36u-devel python36u-pip \
                    vim* iproute curl iputils-ping net-tools unzip git && \
    pip3 install -r requirements.txt && \
    git clone $url
    #python3 /root/tagdns/src/main.py &

ADD env/add_remote_repo /root/tagdns/add_remote_repo
