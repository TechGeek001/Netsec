# Docker Containers
1. MySQL 5.7.20
2. Samba

# Modify Existing Infrastructure
This CTF is designed to work on top of the existing netsec-docker infrastructure. It requires the dnssvr and dhcpsvr containers.
1. In the dnssvr container, append the following lines to ```/etc/bind/zones/db.netsec-docker.isi.jhu.edu```:
   ```
   ; CTF Targets
   samba.netsec-docker.isi.jhu.edu  IN  A  192.168.25.150
   mysql.netsec-docker.isi.jhu.edu  IN  A  192.168.25.151
   ```
2. In the dnssvr container, append the following lines to ```/etc/bind/zones/db.25.168.192```:
   ```
   ; CTF Targets
   150.25.168.192.in-addr-arpa.  IN  PTR  samba.netsec-docker.isi.jhu.edu ; 192.168.25.150
   151.25.168.192.in-addr-arpa.  IN  PTR  mysql.netsec-docker.isi.jhu.edu ; 192.168.25.151
   ```
3. Restart the DNS server with ```# systemctl restart bind9 && systemctl status bind9```
4. In the dhcpsvr container, append the following lines to ```/etc/dhcp/dhcpd.conf```
   ```
   # CTF Ubuntu server, Samba
   host samba {
     hardware ethernet <interface mac>;
     fixed-address samba.netsec-docker.isi.jhu.edu;
   }
   # CTF Ubuntu server, MySQL
   host mysql {
     hardware ethernet <interface mac>;
     fixed-address mysql.netsec-docker.isi.jhu.edu;
   }
   ```
5. Restart the DHCP server with ```# systemctl restart isc-dhcp-server && systemctl status isc-dhcp-server```
# Generate the Login Network Traffic
This step gives the CTF participant traffic to intercept, revealing the creds needed to access the Samba share
1. On whatever server (not the one the Samba container is on) execute the following commands:
    ```
    $ wget https://raw.githubusercontent.com/TechGeek001/Netsec/main/sambasvr/Client/empty_room_client.py
    $ python3 empty_room_client.py &
    ```
   This will periodically send the Samba credentials over telnet on port 45, simulating a misconfiguration.
# Flag Walkthrough
The goal of this CTF is to get the Death Star plans from the database server.
1. Get access to the Samba share drive
  * nmap for samba (445)
  * use wireshark to capture traffic going to the IP address
  * capture network traffic (telnet to port 45) with the share drive creds
2. Get Kendal Ozzel's creds
  * mount the share
  * in galen.erso's directory, run steghide on the image
  * nmap for mysql (3306)
  * use creds to access eadu database
  * kendal ozzel's creds are in plaintext in the users table
3. Get Orson Krennic's creds
  * in kendal.ozzel's directory, unlock the .zip
  * orson krennic's creds are in plaintext in a file in the archive
  * in orson.krennic's directory, find the location of the flag on the database server
4. Get the Death Star plans
  * exploit a UDF vulnerability on the database server
  * as root (on the database server) navigate to the flag directory
  * download the flag file
