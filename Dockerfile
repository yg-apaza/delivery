FROM python:3.8.5-slim as base-backend
# Install PostgreSQL libraries
RUN apt-get update && apt-get install wget gnupg2 -y --no-install-recommends
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install postgresql-server-dev-12 gcc python3-dev -y --no-install-recommends
# Copying backend and frontend
ENV STATIC_DIR=/opt/app/delivery_frontend
RUN mkdir -p /opt/app/delivery_backend && mkdir -p $STATIC_DIR
COPY delivery_frontend/ /opt/app/delivery_frontend/
WORKDIR /opt/app/delivery_backend
COPY delivery_backend/ ./
#Installing requirements for backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Production stages

FROM base-backend as production
## Heroku workaround to connect via ssh
RUN apt-get install openssh-server openssh-client curl iproute2 -y --no-install-recommends
ADD ./.profile.d /app/.profile.d
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
## Install and config nginx
RUN apt-get install nginx -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
# Run gunicorn
COPY start-server.sh /opt/app/
## Start server
ENV PORT=80
EXPOSE $PORT
STOPSIGNAL SIGTERM
CMD /opt/app/start-server.sh
