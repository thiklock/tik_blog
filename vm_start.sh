!/bin/bash

docker pull tiikit/docker-django-v0.0:latest

docker run --env-file .env -p 8080:8080 tikkit/docker-django-v0.0