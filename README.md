# docker-quotesApp

Um pequeno projeto construído em Flask e postgres para exemplificar a criação e utilização do Docker. Para um passo a passo ainda mais simples, veja [esse projeto](https://github.com/joaopedrolourencoaffonso/simple-time-api).

Para ver como executar essa aplicação usando kubernetes, veja o repositório [kubernetes-quotesApp](https://github.com/joaopedrolourencoaffonso/kubernetes-quotesApp/tree/main). Para as imagens em si, acesse: https://hub.docker.com/u/clusterminator.

Para iniciar a aplicação, primeiro, é necessário fazer o download das imagens:

```bash
sh pull.sh
```
Depois, inicalizar os containers:
```bash
sh start.sh
```
Quando estiver satisfeito, basta parar:
```bash
sh stop.sh
```

Para adicionar uma citação, basta fazer:

```bash
$ curl -X POST   -H "Content-Type: application/json"   -d '{"author": "Joao Pedro", "quote": "Olá Lua!"}'   http://127.0.0.1:8080/addQuote
{
  "id": 1129,
  "message": "Nova cita\u00e7\u00e3o adicionada!"
}
```

Para recuperar uma citação com base no número, basta fazer:

```bash
$ curl localhost:8080/getQuote/1129
{
  "author": "Joao Pedro",
  "quote": "Ol\u00e1 Lua!"
}
```