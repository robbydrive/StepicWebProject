kill -TERM $(cat 1.pid)
kill -TERM $(cat ask/2.pid)
gunicorn -b 0.0.0.0:8080 -p 1.pid hello &
cd ask
gunicorn -b 0.0.0.0:8000 -p 2.pid ask.wsgi &
