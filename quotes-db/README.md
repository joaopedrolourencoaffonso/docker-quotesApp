# Imagem do Banco de Dados

O banco de dados propriamente dito foi criado conforme os passos abaixo:

```SQL
mysql> create user 'quotesApp'@'%' IDENTIFIED BY 'senha';
Query OK, 0 rows affected (0,06 sec)

mysql> grant all privileges on * . * to 'quotesApp'@'%';
Query OK, 0 rows affected (0,05 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0,02 sec)

exit;

mysql -u quotesApp -p

mysql> create database quotesApp;
Query OK, 1 row affected (0,09 sec)

mysql> use quotesApp;
Database changed
mysql> CREATE TABLE quotes (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     author VARCHAR(255) NOT NULL,
    ->     quote TEXT NOT NULL
    -> );
```
Foi usado então o script [inserir.py]() para inserir as frases contidas no arquivo [citacoes.json](https://github.com/joaopedrolourencoaffonso/quotes_bot/blob/main/citacoes.json).

O dump foi criado usando o comando abaixo:
```bash
mysqldump -u quotesApp -p senha quotesApp > dump.sql
```
Por fim, a imagem foi criada usando o [Dockerfile]() com o comando abaixo:
```bash
docker build -t clusterminator/quotes-db:1.0 .
```
