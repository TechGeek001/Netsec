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

#install dependencies for systemd and syslog
RUN apt-get install systemd systemd-sysv syslog-ng syslog-ng-core syslog-ng-mod-sql syslog-ng-mod-mongodb -y

#start systemd
CMD ["/usr/lib/systemd/systemd", "--system"]

#install the outdated MySQL server
RUN apt-get install libaio1 libc6 libmecab2 libgcc1 libstdc++6 libtinfo5 perl -y
RUN mkdir /root/temp
RUN cd /root/temp
RUN wget https://downloads.mysql.com/archives/get/p/23/file/mysql-server_5.7.20-1ubuntu16.04_amd64.deb-bundle.tar
RUN tar xopf mysql-server_5.7.20-1ubuntu16.04_amd64.deb-bundle.tar
RUN dpkg -i mysql-common_5.7.20-1ubuntu16.04_amd64.deb
RUN dpkg -i mysql-community-client_5.7.20-1ubuntu16.04_amd64.deb
RUN dpkg -i mysql-client_5.7.20-1ubuntu16.04_amd64.deb
RUN dpkg -i *.deb
#RUN export DEBIAN_FRONTEND="noninteractive"
#RUN debconf-set-selections <<< "mysql-server mysql-server/root_password password virus"
#RUN debconf-set-selections <<< "mysql-server mysql-server/root_password_again password virus"
#RUN dpkg -i mysql-community-server_5.7.20-1ubuntu16.04_amd64.deb
#--------------------------------------------

# Finished!
RUN echo $'\n\
* Container is ready