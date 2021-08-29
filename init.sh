sudo apt update
sudo python3 -m pip install django==2.0
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c /home/box/web/etc/gunicorn.conf.py hello:app &
gunicorn -c /home/box/web/etc/gunicorn-django.conf.py ask.wsgi:application &


# Test #
# sudo ln -sf /home/cogito/nginx_server/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
# sudo rm -rf /etc/nginx/sites-enabled/default
# sudo /etc/init.d/nginx restart
# gunicorn -c /home/cogito/nginx_server/etc/gunicorn.conf.py hello:app &
# gunicorn -c /home/cogito/nginx_server/etc/gunicorn-django.conf.py ask.wsgi:application &