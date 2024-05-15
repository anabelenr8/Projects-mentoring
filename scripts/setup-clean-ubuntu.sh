#! /usr/bin/env bash

#how to connect with server:
ssh root@167.172.53.113

mkdir /var/www/projects


# - Generate a new SSH key for Ubuntu server
# - Must be done just once - the first time server is setup
# ssh-keygen -t rsa -b 4096 -C "api@yourprojectname.com"
# Path for SSH key /root/.ssh/id_rsa.pub

# Adjust "/var/www/projects/newproject" to fit your project
git clone git@github.com:anabelenr8/store.git /var/www/projects/store


# Install deps
sudo apt-get update
sudo apt-get install libpq-dev build-essential python3.11-dev postgresql postgresql-contrib supervisor -y

# Postgres DB setup
sudo -i -u postgres psql

# Postgres DB setup
# Change "projectname_*" prefix to fit your project
# !!! Don't keep your passwords in this file
# !!! only in secure notes / 1Password App
CREATE ROLE projectname_api WITH LOGIN PASSWORD;

ALTER ROLE projectname_api CREATEDB;

CREATE DATABASE projectname_api_db;

GRANT ALL PRIVILEGES ON DATABASE projectname_api_db TO projectname_api;

# Pipenv setup
apt install python3-pip -y
pip3 install pipenv


# Give permissions to www-data user for a folder and subfolders
sudo chown -R www-data:www-data /var/www

# Switch www-data user on Ubuntu
sudo -u www-data /bin/bash

# Replace "newproject" with your project folder name
cd /var/www/projects/newproject/
python3 -V # .. If returns 3.10, use 3.10 in the next command

# Setup pipenv virtual env with the Python version from "python3 -V" command
pipenv shell --python 3.10


# Path to virtualenv:
# /var/www/.local/share/virtualenvs/newproject-E9saqUxb


# Gunicorn config:
# See config/gunicorn.conf for file content
vim /etc/supervisor/conf.d/gunicorn.conf


####################################
# Setup nginx config
####################################

# Install
sudo apt update
sudo apt install nginx -y

# Change "newproject" to your project name
sudo vim /etc/nginx/sites-available/newproject

# - nginx config details
# - nginx config path: /config/nginx
# - Change "146.190.56.0" in "server_name 146.190.56.0;" to server IP or domain

sudo ln -s /etc/nginx/sites-available/newproject /etc/nginx/sites-enabled/

sudo nginx -t
sudo systemctl restart nginx


# Install SSL for HTTPS
sudo apt update
sudo apt install certbot python3-certbot-nginx -y

# Certbot will automatically configure Nginx to use the SSL certificates for the specified domains.
# It will also ask if you want to redirect all HTTP traffic to HTTPS.
# It's recommended to choose this option for better security.
sudo certbot --nginx -d anabelenromero.com

# After obtaining the certificates, they will be stored in:
# Full path to certificate: /etc/letsencrypt/live/your_domain_name/fullchain.pem
# Full path to private key: /etc/letsencrypt/live/your_domain_name/privkey.pem

# Let's Encrypt certificates are valid for 90 days.
# However, you can set up an automatic renewal:
sudo certbot renew --dry-run


# Collect static files
python manage.py collectstatic --noinput


