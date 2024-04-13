# Application overview
* Vulnerable database using outdated MySQL
# Runtime environment setup
1. Download files to build container
    ```
    $ wget https://raw.githubusercontent.com/TechGeek001/netsec-db/main/netsecdb-UbuntuServerX86-64.sh
    $ chmod +x netsec-db-UbuntuServerX86-64.sh
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
