#! /usr/bin/env bash

NEW_PROJECT_PATH="/var/www/projects/store-new-version"

CURRENT_PROJECT_PATH="/var/www/projects/store"

OLD_PROJECT_PATH="/var/www/projects/store-old-version"

ENV_FILE_PATH="/var/www/projects/env/store.env"

PIPENV_PATH="/usr/bin/pipenv"

VENV_PATH="/var/www/.local/share/virtualenvs/store-LEsRl0nh "


if [ -d "$NEW_PROJECT_PATH" ]; then rm -Rf ${NEW_PROJECT_PATH}; fi

# ssh-keygen -t rsa -b 4096 -C "www-data@store.com"
git clone git@github.com:anabelenr8/store.git ${NEW_PROJECT_PATH}

# Need .env file from somewhere
cp ${ENV_FILE_PATH} ${NEW_PROJECT_PATH}

# Install pipenv deps
cd ${NEW_PROJECT_PATH}

# Change venv path to this one in all scripts prepared so far:
#Virtualenv location: /var/www/.local/share/virtualenvs/store-new-version-Y-PARjJd
${PIPENV_PATH} install