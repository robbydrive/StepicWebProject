mysql -uroot -e "create database dbweb;
		 use dbweb;
		 create user 'box'@'localhost' identified by 'pass';
		 grant all privileges on dbweb to 'box'@'localhost' with grant option;
		 flush privileges;"
