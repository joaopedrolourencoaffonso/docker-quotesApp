FROM mysql:latest
WORKDIR /docker-entrypoint-initdb.d
COPY dump.sql /docker-entrypoint-initdb.d
ENV MYSQL_ROOT_PASSWORD=senha
ENV MYSQL_DATABASE=quotesApp
ENV MYSQL_USER=quotesApp
ENV MYSQL_PASSWORD=senha
EXPOSE 3306
