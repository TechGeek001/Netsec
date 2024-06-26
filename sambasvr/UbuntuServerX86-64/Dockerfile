# Description:
#   This runtime environment example Dockerfile creates a container with a minimal Ubuntu server and an unsecured Samba server
# Usage:
#   From this directory, run $ docker build -t tsambasvr .
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

#install samba
RUN apt-get install samba -y
RUN mkdir -p /home/sambashare
COPY etc_samba_smb.conf /etc/samba/smb.conf
RUN chown nobody:nogroup /home/sambashare
RUN chmod -R 0775 /home/sambashare
#create the shared user
RUN useradd -s /usr/sbin/nologin -M empire
RUN (echo "NOrebelsPLEASE"; echo "NOrebelsPLEASE") | smbpasswd -a -s empire

#copy the important files
COPY home_sambashare_erso /home/sambashare/galen.erso
COPY home_sambashare_ozzel /home/sambashare/kendal.ozzel
COPY home_sambashare_krennic /home/sambashare/orson.krennic

#copy the fake telnet server for the fake login traffic
RUN mkdir -p /root/OFF-LIMITS
COPY empty_room_svr.py /root/OFF-LIMITS/empty_room_svr.py
