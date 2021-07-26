# Stepik #
sudo ln -sf /home/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo rm -rf /etc/nginx/sites-enabled/default
# Test #
# sudo ln -sf /home/cogito/nginx_server/etc/nginx.conf  /etc/nginx/nginx.conf
# Restart #
sudo /etc/init.d/nginx restart