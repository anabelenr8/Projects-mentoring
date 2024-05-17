#! /usr/bin/env bash

###
## STEPS TO DEPLOY A NEW VERSION
###
# ssh root@167.172.53.113 "su -s /bin/bash www-data -c 'cd /var/www/projects/scripts/backend && ./build-new-release.sh'"

NEW_PROJECT_PATH="/var/www/projects/store-new-version"

CURRENT_PROJECT_PATH="/var/www/projects/store"

OLD_PROJECT_PATH="/var/www/projects/store-old-version"

ENV_FILE_PATH="/var/www/projects/env/store.env"

PIPENV_PATH="/usr/bin/pipenv"

VENV_PATH="/var/www/.local/share/virtualenvs/store-new-version-Y-PARjJd"


if [ -d "$NEW_PROJECT_PATH" ]; then rm -Rf ${NEW_PROJECT_PATH}; fi

# ssh-keygen -t rsa -b 4096 -C "www-data@store.com"
git clone git@github.com:anabelenr8/store.git ${NEW_PROJECT_PATH}

# Need .env file from somewhere
cp ${ENV_FILE_PATH} ${NEW_PROJECT_PATH}

# Install pipenv deps
cd ${NEW_PROJECT_PATH}

# Change venv path to this one in all scripts prepared so far:
#/var/www/.local/share/virtualenvs/store-new-version-Y-PARjJd
${PIPENV_PATH} install

PYTHON_PATH="${VENV_PATH}/bin/python"

# Migrate DB
${PYTHON_PATH} ${NEW_PROJECT_PATH}/manage.py migrate

# Static files
${PYTHON_PATH} ${NEW_PROJECT_PATH}/manage.py collectstatic --noinput

# Switch to new version
if [ -d "$OLD_PROJECT_PATH" ]; then rm -Rf ${OLD_PROJECT_PATH}; fi

# Switch: Current version -> Old version
if [ -d "$CURRENT_PROJECT_PATH" ]; then mv ${CURRENT_PROJECT_PATH} ${OLD_PROJECT_PATH}; fi

# Switch: New version -> Current version
mv ${NEW_PROJECT_PATH} ${CURRENT_PROJECT_PATH}

# Make gunicorn script executable
chmod +x ${CURRENT_PROJECT_PATH}/scripts/start_gunicorn.sh

# !!! In order for "www-data" user to be able to
# restart the following service, make sure "www-data" user is configured
# to not ask for the password.

# Switch to "root" user and execute the following commands:
# sudo visudo
# ( alternative command: )
# sudo EDITOR=vim visudo

# Add the following line at the end of the file to grant the www-data
# user permission to run supervisorctl without providing a password:
# www-data ALL=(ALL:ALL) NOPASSWD: /usr/bin/supervisorctl
# www-data ALL=(ALL) NOPASSWD: /bin/systemctl reload nginx
# www-data ALL=(ALL) NOPASSWD: /bin/systemctl restart nginx
#
# Actual path: /usr/bin/supervisorctl (found using "which supervisorctl" command)
#
# Replace /path/to/supervisorctl with the actual path,
# which can usually be found using the command which supervisorctl.

sudo supervisorctl reread
sudo supervisorctl update

sudo supervisorctl restart gunicorn

sudo systemctl reload nginx
sudo systemctl restart nginx

