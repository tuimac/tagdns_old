FROM centos:7

ARG url=https://github.com/tuimac/tagdns.git

EXPOSE 53/udp

WORKDIR /root

ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/centos/vim.sh /etc/profile.d/vim.sh
ADD env/tmux.conf /root/.tmux.conf

ADD requirements.txt /root/requirements.txt

RUN yum update -y && \
    yum install -y epel-release && \
    yum remove -y vi && \
    yum install -y python3 python-pip vim* iproute curl iputils-ping net-tools unzip git tree && \
    pip3 install -r requirements.txt && \
    pip3 install git+$url && \
    mkdir -p /etc/vim/backup && \
    mkdir -p /etc/vim/undo
    
ADD env/vimrc /etc/vim/vimrc

ENTRYPOINT ["tagdns", "&"]
