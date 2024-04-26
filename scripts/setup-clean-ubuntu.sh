#! /usr/bin/env bash

mkdir /var/www/projects

git clone git@github.com:anabelenr8/store.git /var/www/projects/store

sudo ln -s /etc/nginx/sites-available/store /etc/nginx/sites-enabled/

Certificate is saved at: /etc/letsencrypt/live/anabelenromero.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/anabelenromero.com/privkey.pem

python manage.py collectstatic --noinput



sudo nginx -t
sudo systemctl restart nginx