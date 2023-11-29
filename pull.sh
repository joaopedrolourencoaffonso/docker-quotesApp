#!/bin/sh

docker pull clusterminator/quotes-db:1.0
sleep 30;
docker pull clusterminator/images-api:latest
sleep 30;
docker pull clusterminator/mainpage-api:1.0
sleep 30;
docker pull clusterminator/quotes-api:1.0
sleep 30;
echo "Pronto!"
