sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c /home/box/web/etc/gunicorn.conf.py hello:app &
gunicorn -c /home/box/web/etc/gunicorn-django.conf.py ask.wsgi:application &