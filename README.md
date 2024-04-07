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
