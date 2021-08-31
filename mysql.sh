sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepik;"
mysql -uroot -e "create user 'cogito'@'localhost' identified by 'pass123';"
mysql -uroot -e "grant all privileges on stepik.* to 'cogito'@'localhost' with grant option;"
mysql -uroot -e "grant all privileges on stepik.* to 'box'@'localhost' with grant option;"
#python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate