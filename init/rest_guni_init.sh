kill -TERM $(cat ~/web/pids/1.pid)
kill -TERM $(cat ~/web/pids/2.pid)
gunicorn -b 0.0.0.0:8080 -p ~/web/pids/1.pid hello &
cd ask
gunicorn -b 0.0.0.0:8000 -p ~/web/pids/2.pid ask.wsgi &
mysql -uroot -e "use dbweb; delete from auth_user where username = 'blabla';"
