sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
gunicorn -b 0.0.0.0:8080 hello &
cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi &
sudo /etc/init.d/mysql start
sudo chmod +x manage.py
