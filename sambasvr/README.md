# Overview
These instructions will create a MySQL 5.7.20 instance inside a Docker container on a Ubuntu 22.04 server. The server is vulnerable to the /multi/mysql/mysql_udf_payload exploit in Metasploit. The MySQL service is running as root, allowing an attacker to gain privilege escalation on the target system. I shouldn't have to say this out loud, but this should ABSOLUTELY NOT under any circumstances be used in a production environment.
# Setup
1. Download files to build container
    ```
    $ wget https://raw.githubusercontent.com/TechGeek001/Netsec/main/sambasvr/sambasvr-UbuntuServerX86-64.sh
    $ chmod +x sambasvr-UbuntuServerX86-64.sh
    $ ./sambasvr-UbuntuServerX86-64.sh
    ```
2. Navigate to the newly created directory and build the Docker container
    ```
    $ cd sambasvr/sambasvr/UbuntuServerX86-64
    ```
3. Build and run the Docker container
    ```
    $ docker build -t tsambasvr .
    $ docker run -d --name sambasvr --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --network host tsambasvr:latest
    ```
# Accessing the Share Drive
1. Inside Kali, install the CIFS utility
    ```
    $ sudo apt-get install cifs-utils
    ```
2. Mount the drive
    ```
    $ sudo mkdir /mnt/public
    $ sudo mount -t cifs //<target-ip>/Public /mnt/public
    ```
