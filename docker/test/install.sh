#!/bin/bash

yum install -y curl git make gcc ncurses-devel
[ ! -d "/usr/local/src" ] && mkdir -p "/usr/local/src"

cd /usr/local/src
git clone https://github.com/vim/vim.git
cd /usr/local/src/vim

./configure --disable-selinux --enable-cscope --enable-fontset --enable-gpm --enable-multibyte --enable-rubyinterp --enable-xim

make && make install
