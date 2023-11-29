FROM python:3-alpine3.15
WORKDIR /imagesapp
COPY . /imagesapp
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./app.py
