FROM jenkins/jenkins

USER root
WORKDIR /root

EXPOSE 8080
EXPOSE 50000

ADD env/vimrc /root/.vimrc
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/tmux.conf /root/.tmux.conf

RUN apt update && \
    apt upgrade -y && \
    apt install -y vim* traceroute net-tools dnsutils && \
    mkdir -p /etc/vim/undo && \
    mkdir -p /etc/vim/backup
