#!/usr/bin/env bash

VENV_PATH="/var/www/.local/share/virtualenvs/store-new-version-Y-PARjJd"

CURRENT_PROJECT_PATH="/var/www/projects/store"

APP_PATH="${CURRENT_PROJECT_PATH}"

APP="store"

cd ${APP_PATH}

exec ${VENV_PATH}/bin/gunicorn --workers 3 --bind unix:${APP_PATH}/${APP}.sock ${APP}.wsgi:application --chdir=${APP_PATH}