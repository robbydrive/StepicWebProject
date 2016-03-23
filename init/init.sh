sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
gunicorn -b 0.0.0.0:8080 -p ~/web/pids/1.pid hello &
cd ~/web/ask
gunicorn -b 0.0.0.0:8000 -p ~/web/pids/2.pid ask.wsgi &
sudo /etc/init.d/mysql start
sudo chmod +x manage.py
./manage.py syncdb
