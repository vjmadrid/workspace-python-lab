FROM python:3.9-alpine

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "./main.py"]