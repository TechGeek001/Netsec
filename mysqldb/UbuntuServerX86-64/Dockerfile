# Description:
#   This runtime environment example Dockerfile creates a container with a minimal Ubuntu server and a vulnerable MySQL database server
# Usage:
#   From this directory, run $ docker build -t tnetsecdb .
#   By default, runs as root

FROM ubuntu:22.04

#https://grigorkh.medium.com/fix-tzdata-hangs-docker-image-build-cdb52cc3360d
ENV TZ=US/Eastern
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#avoid question/dialog during apt-get installs
ARG DEBIAN_FRONTEND noninteractive

# Setup container's ENV for systemd
ENV container docker

#update
RUN apt-get update

#install utilities
RUN apt-get install apt-utils dpkg-dev debconf debconf-utils -y
RUN apt-get install net-tools iputils-ping iptables iproute2 wget nmap bind9-dnsutils dnsutils inetutils-traceroute isc-dhcp-common -y
RUN apt-get install vim acl sudo telnet ssh netcat nfs-common -y
#I like Nano
RUN apt-get install nano

#install dependencies for systemd and syslog
RUN apt-get install systemd systemd-sysv syslog-ng syslog-ng-core syslog-ng-mod-sql syslog-ng-mod-mongodb -y

#start systemd
CMD ["/usr/lib/systemd/systemd", "--system"]

#install the outdated MySQL server
RUN apt-get install libaio1 libc6 libmecab2 libgcc1 libstdc++6 libtinfo5 perl libnuma1 python3 python-is-python3 psmisc -y
RUN mkdir -p /root/temp
RUN cd /root/temp
RUN wget https://downloads.mysql.com/archives/get/p/23/file/mysql-server_5.7.20-1ubuntu16.04_amd64.deb-bundle.tar
RUN tar xopf mysql-server_5.7.20-1ubuntu16.04_amd64.deb-bundle.tar
RUN dpkg -i mysql-common_5.7.20-1ubuntu16.04_amd64.deb
RUN dpkg -i mysql-community-client_5.7.20-1ubuntu16.04_amd64.deb
RUN dpkg -i mysql-client_5.7.20-1ubuntu16.04_amd64.deb
#RUN export DEBIAN_FRONTEND="noninteractive"
RUN dpkg -i mysql-community-server_5.7.20-1ubuntu16.04_amd64.deb

#run MySQL as root and disable secure_file_priv
COPY lib_systemd_system_mysql.service /lib/systemd/system/mysql.service
COPY etc_mysql_mysqlconfd_mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
COPY create_users.sql /root/temp/create_users.sql
COPY eadu.sql /root/temp/eadu.sql
COPY scarif.sql /root/temp/scarif.sql

#this is the setup script that has to be run after MySQL is running
RUN chmod 777 /usr/lib/mysql/plugin
COPY setup.sh /root/setup.sh

#plant the flag
COPY "Death-Star-Plans.png" "/root/Death-Star-Plans.png"
