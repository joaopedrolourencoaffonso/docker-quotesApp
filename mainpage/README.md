# Main Page - API que serve a página principal 

Este aplicativo Flask simples serve como uma página principal e inclui rotas do lado do cliente para recuperar cotações e buscar imagens de fundo de APIs externas. O aplicativo foi projetado para ser executado em um contêiner Docker.

## Dependências

- Flask
- requests

## Características

1. **Página principal:**
    - Acesse a página principal navegando até o endpoint raiz (`/`). Ele renderiza um modelo HTML (index.html).

2. **Rota do lado do cliente - Citações:**
    - Acesse as citações navegando até `/quotes`. O aplicativo faz uma solicitação para a [API de citações](https://github.com/joaopedrolourencoaffonso/docker-quotesApp/tree/main/quotes-api) (http://quotes-api:8080/quotes) e retorna a resposta JSON.

3. **Rota do lado do cliente - imagem de fundo:**
    - Acesse as imagens de fundo navegando até `/imagemDeFundo`. O app faz uma solicitação a a [API de imagem](https://github.com/joaopedrolourencoaffonso/docker-quotesApp/tree/main/images-api) (http://images-api:8080/imagemDeFundo) e retorna a imagem diretamente ao cliente.

## Configurar

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/joaopedrolourencoaffonso/docker-quotesApp.git
    ```

2. **Construa a imagem do Docker:**
    ```bash
    docker build -t suaContaDockerHub/mainpage-api
    ```

3. **Execute o contêiner Docker:**
    ```bash
    docker run -p 80:8080 mainpage-app
    ```

    Acesse o aplicativo em [http://localhost](http://localhost:80).

## Dockerfile

```Dockerfile
FROM python:3-alpine3.15

WORKDIR /mainpage
COPY . /mainpage

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python ./app.py
```
