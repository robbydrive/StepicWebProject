mysql -uroot -e "create database dbweb"
mysql -uroot -e "create user 'box'@'localhost' identified by 'pass'"
mysql -uroot -e "grant all privileges on dbweb to 'box'@'localhost' with grant option"
