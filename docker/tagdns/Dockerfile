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

RUN yum update -y && \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum install -y python36u python36u-libs python36u-devel python36u-pip \
                    vim* iproute curl iputils-ping net-tools unzip git && \
    yum remove -y vi && \
    git clone $url && \
    pip3 install -r requirements.txt && \
    alias vi='vim'
    #python3 tagdns/src/main.py
