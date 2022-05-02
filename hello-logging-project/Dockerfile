FROM python:3.9-alpine

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /crontab/crontab /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab

RUN touch /tmp/out.log

CMD ["crond", "-f", "/tmp/out.log"]