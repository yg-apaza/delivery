# Building the React app
FROM node:10 as base-frontend
WORKDIR /app
COPY delivery-frontend /app/
RUN npm install
RUN npm run build

# Django
FROM python:3.8.5-slim as base-backend
ENV STATIC_DIR=/opt/app/delivery_frontend
RUN mkdir -p /opt/app/delivery_backend && mkdir -p $STATIC_DIR
WORKDIR ${STATIC_DIR}
COPY --from=base-frontend /app/build ./
WORKDIR /opt/app/delivery_backend
COPY delivery_backend ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Production stages

FROM base-backend as production
## Install and config nginx
RUN apt-get update && apt-get install nginx -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
# Run gunicorn
RUN pip install gunicorn
COPY start-server.sh /opt/app/
RUN chown -R www-data:www-data ${STATIC_DIR}
# Start server
ENV PORT=80
EXPOSE $PORT
STOPSIGNAL SIGTERM
CMD /opt/app/start-server.sh
