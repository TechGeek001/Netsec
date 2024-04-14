# Docker Containers
1. MySQL 5.7.20
2. Samba

# Flag Walkthrough
The goal of this CTF is to get the Death Star plans from the database server.
1. Get Kendal Ozzel's creds
  * nmap for samba (445)
  * mount the share
  * in galen.erso's directory, run steghide on the image
  * nmap for mysql (3306)
  * use creds to access eadu database
  * kendal ozzel's creds are in plaintext in the users table
2. Get Orson Krennic's creds
  * in kendal.ozzel's directory, unlock the .zip
  * orson krennic's creds are in plaintext in a file in the archive
  * in orson.krennic's directory, find the location of the flag on the database server
3. Get the Death Star plans
  * exploit a UDF vulnerability on the database server
  * as root (on the database server) navigate to the flag directory
  * download the flag file
