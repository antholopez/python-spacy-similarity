FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download es_core_news_md

COPY . /app

CMD [ "python3", "./app.py" ]