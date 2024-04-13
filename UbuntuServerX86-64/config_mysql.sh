mysql
echo "CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypass';"
echo "CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';"
echo "GRANT ALL ON *.* TO 'myuser'@'localhost';"
echo "GRANT ALL ON *.* TO 'myuser'@'%';"
echo "FLUSH PRIVILEGES;"
echo "exit"
