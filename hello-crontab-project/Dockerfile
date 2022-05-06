FROM python:3.6.12-alpine3.12

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install --upgrade pip

RUN cd /app && \
    pip install --no-cache-dir .

RUN chown -R "1000:1000" /app
#RUN crontab crontab

#CMD ["crond", "-f"]
CMD tail -f /dev/null