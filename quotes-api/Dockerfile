FROM python:3-alpine3.15
WORKDIR /quotesapi
COPY . /quotesapi
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./app.py
