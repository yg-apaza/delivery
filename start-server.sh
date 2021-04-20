#!/usr/bin/env bash

 # Heroku workaround, replace PORT  and STATIC_DIR variables
sed -i -e 's/$PORT/'"$PORT"'/g' -e 's@$STATIC_DIR@'"$STATIC_DIR"'@g' /etc/nginx/sites-available/default \
&& gunicorn --chdir ./delivery_backend delivery_backend.wsgi --bind 0.0.0.0:8000 \
& nginx -g "daemon off;"
