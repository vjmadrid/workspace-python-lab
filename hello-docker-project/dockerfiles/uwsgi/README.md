
uwsgi --wsgi-file app.py --http :9090

uwsgi --socket 0.0.0.0:9090 --protocol=http -w wsgi:app

uwsgi --ini uwsgi.ini
