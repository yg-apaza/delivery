#!/usr/bin/env bash

(cd delivery_backend; gunicorn delivery_backend.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3) & nginx -g "daemon off;"
