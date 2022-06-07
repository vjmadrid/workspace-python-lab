FROM python:3.9-alpine as build-stage

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]


FROM nginx:1.15

COPY --from=build-stage /app/ /usr/share/nginx/html

# Copy the default nginx.conf provided by tiangolo/node-frontend
COPY --from=build-stage /configs/nginx.conf /etc/nginx/conf.d/default.conf