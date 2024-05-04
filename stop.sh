#!/bin/sh

echo "Encerrando aplicação"

docker stop mainpage;
docker rm mainpage;

docker stop quotes-api;
docker rm quotes-api;

docker stop addget-api;
docker rm addget-api;

docker stop images-api;
docker rm images-api;

docker stop database;
docker rm database;

docker network rm quotesApp;

echo "Aplicação encerrada!"
