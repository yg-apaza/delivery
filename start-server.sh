#!/usr/bin/env bash

sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/sites-available/default \
    && sed -i -e 's@$STATIC_DIR@'"$STATIC_DIR"'@g' /etc/nginx/sites-available/default \
    && gunicorn --chdir ./delivery_backend delivery_backend.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3 \
    & nginx -g "daemon off;"
