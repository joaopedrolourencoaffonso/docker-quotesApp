FROM python:3-alpine3.15
WORKDIR /addQuotes
COPY . /addQuotes
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./app.py
