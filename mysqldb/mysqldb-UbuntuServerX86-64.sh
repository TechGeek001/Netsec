# Script to clone specific files for creating a vulnerable netsec-db server environment within a Docker container
# running a minimal Ubuntu server image

mkdir mysqldb && cd mysqldb

# Start a Git repository
git init

# Squelch annoying message
git config pull.rebase false  # merge (the default strategy)

# Track repository, do not enter subdirectory
git remote add -f origin https://github.com/TechGeek001/Netsec.git

# Enable the tree check feature
git config core.sparseCheckout true

# Create a file in the path: .git/info/sparse-checkout
# That is inside the hidden .git directory that was created
# by running the command: git init
# And inside it enter the name of the specific files (or subdirectory) you only want to clone
echo 'mysqldb/UbuntuServerX86-64/.project' >> .git/info/sparse-checkout
echo 'mysqldb/UbuntuServerX86-64/Dockerfile' >> .git/info/sparse-checkout
echo 'mysqldb/UbuntuServerX86-64/lib_systemd_system_mysql.service' >> .git/info/sparse-checkout
echo 'mysqldb/UbuntuServerX86-64/etc_mysql_mysqlconfd_mysqld.cnf' >> .git/info/sparse-checkout
echo 'mysqldb/UbuntuServerX86-64/create_users.sql' >> .git/info/sparse-checkout
echo 'mysqldb/UbuntuServerX86-64/eadu.sql' >> .git/info/sparse-checkout
echo 'mysqldb/UbuntuServerX86-64/scarif.sql' >> .git/info/sparse-checkout
echo 'mysqldb/UbuntuServerX86-64/setup.sh' >> .git/info/sparse-checkout
echo 'mysqldb/UbuntuServerX86-64/Death-Star-Plans.sh' >> .git/info/sparse-checkout

## Download with pull, not clone
git pull origin main

echo 'cd into mysqldb/mysqldb/UbuntuServerX86-64 and view details in Dockerfile for building, running, and attaching to the container'

# References:
#   https://terminalroot.com/how-to-clone-only-a-subdirectory-with-git-or-svn
