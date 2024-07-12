#!/usr/bin/env bash
# setting up web static
mkdir -p /data/web_static/shared
mkdir -p "/data/web_static/releases/test"
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
HOSTNAME=$(hostname)
echo "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;
    
    location /hbnb_static { 
    	add_header X-Served-By $HOSTNAME;
	alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default
service nginx restart

