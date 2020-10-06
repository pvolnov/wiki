
## installing 
```
 sudo apt update
 sudo apt install mysql-server mysql-client
 sudo mysql_secure_installation
 sudo mysql 

mysql> CREATE DATABASE testDB;
mysql> CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL PRIVILEGES ON testDB.* TO 'my_user'@'localhost'




```

## Import SQL file
```
mysql> use DATABASE_NAME;
mysql> source path/to/file.sql;
```