FROM python:3.9.0-slim-buster AS builder

RUN apt-get update && apt-get install -y --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip


FROM builder AS builder-venv

COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install -r /requirements.txt


FROM builder-venv AS runner

COPY . /app
WORKDIR /app

ENTRYPOINT ["/venv/bin/python3", "-m", "flask run"]