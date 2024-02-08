#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/current/index.html
sudo tee /data/web_static/current/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo cp /data/web_static/current/index.html  /data/web_static/releases/test/index.html
echo "server {
   listen 80 default_server;
   listen [::]:80 default_server;
   root /var/www/html;
   index index.html;
   add_header X-Served-By $HOSTNAME;
   location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
   }
   location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
   error_page 404 /404.html;
   location = /404.html{
                 internal;
         }
}"  | sudo tee /etc/nginx/sites-available/default
sudo nginx -t
sudo service nginx restart
