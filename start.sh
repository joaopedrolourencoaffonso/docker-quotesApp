#!/bin/sh

echo "1 - Criando rede quotesApp";
docker network create quotesApp
echo "2 - Rede quotesApp criada!";
sleep 5;
echo "3 - Inicializando banco de dados";
docker run -d --name database --network quotesApp -p 4000:3306 clusterminator/quotes-db:1.0
sleep 25;
echo "4 - Banco de dados inicalizado com sucesso";
echo "5 - Inicializando APIs"
docker run -d --name images-api --network quotesApp -p 4002:8080 clusterminator/images-api:latest
sleep 5;
docker run -d --name mainpage --network quotesApp -p 80:8080 clusterminator/mainpage-api:1.0
sleep 5;
docker run -d --name quotes-api --network quotesApp -p 4001:8080 clusterminator/quotes-api:1.0
sleep 5;
docker run -d --name addget-api --network quotesApp -p 4003:8080 clusterminator/addget-api:1.0
sleep 5;
echo "Aplicação inicalizada! Acesse: http://localhost";
