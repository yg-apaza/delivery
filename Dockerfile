FROM python:3.8.5-slim

# install and config nginx
RUN apt-get update && apt-get install nginx -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
    
# copy source and install dependencies
RUN mkdir -p /opt/app/delivery_backend
COPY start-server.sh /opt/app/
COPY delivery_backend /opt/app/delivery_backend/
WORKDIR /opt/app
RUN pip install --upgrade pip
RUN pip install -r delivery_backend/requirements.txt
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
