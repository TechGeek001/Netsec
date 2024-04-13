# Script to clone specific files for creating a vulnerable netsec-db server environment within a Docker container
# running a minimal Ubuntu server image

# Create a directory, so Git doesn't get messy, and enter it
mkdir netsecdb && cd netsecdb

# Start a Git repository
git init

# Squelch annoying message
git config pull.rebase false  # merge (the default strategy)

# Track repository, do not enter subdirectory
git remote add -f origin https://github.com/TechGeek001/netsec-db.git

# Enable the tree check feature
git config core.sparseCheckout true

# Create a file in the path: .git/info/sparse-checkout
# That is inside the hidden .git directory that was created
# by running the command: git init
# And inside it enter the name of the specific files (or subdirectory) you only want to clone
echo 'UbuntuServerX86-64/.project' >> .git/info/sparse-checkout
echo 'UbuntuServerX86-64/Dockerfile' >> .git/info/sparse-checkout
echo 'UbuntuServerX86-64/etc_mysql_mysqlconfd_mysql.conf' >> .git/info/sparse-checkout
echo 'populate_db.py' >> .git/info/sparse-checkout
echo 'first_names.txt' >> .git/info/sparse-checkout
echo 'last_names.txt' >> .git/info/sparse-checkout
echo 'domains.txt' >> .git/info/sparse-checkout

## Download with pull, not clone
git pull origin main

echo 'cd into UbuntuServerX86-64 and view details in Dockerfile for building, running, and attaching to the container'
echo 'docker build -t tnetsecdb .'
echo 'docker run -d --name netsecdb --dns 192.168.25.10 --dns-search netsec-docker.isi.jhu.edu --privileged --network host tnetsecdb:latest'

# References:
#   https://terminalroot.com/how-to-clone-only-a-subdirectory-with-git-or-svn
