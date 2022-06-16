
# General Configuration

VIRTUAL_LOCAL_ENV_NAME := venv
EXECUTION_DIRECTORY_BY_ENVIRONMENT := bin
EXECUTION_PATH := $(VIRTUAL_LOCAL_ENV_NAME)/$(EXECUTION_DIRECTORY_BY_ENVIRONMENT)

PYTHON := $(EXECUTION_PATH)/python3
PIP := $(EXECUTION_PATH)/pip

# Docker Configuration

IMAGE_NAME := acme/hello-world-flask-python
CONTAINER_NAME := hello-world-flask-python



init-venv:
	@make create-venv
	$(PIP) install -r requirements.txt

upgrade-venv:
	$(PIP) install --upgrade pip setuptools wheel

create-venv:
	python3 -m venv $(VIRTUAL_LOCAL_ENV_NAME)
	@make upgrade-venv

venv-upgrade:
	$(PIP) install --upgrade pip

run: venv
	$(PYTHON) app.py



docker-build:
	docker build --no-cache	-t $(IMAGE_NAME) .

docker-build-gunicorn:
	docker build --no-cache	-t $(IMAGE_NAME) -f Dockerfile.gunicorn_entrypoint .

docker-run:
	docker run --name $(CONTAINER_NAME) -p 5000:5000 -d $(IMAGE_NAME)

docker-stop: ##Execute docker stop
	ID=$$(docker ps -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker stop $$ID

docker-logs: ##Execute docker logs
	ID=$$(docker ps -a -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker logs $$ID

docker-ssh: ##Execute docker image with ssh
	ID=$$(docker ps -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker exec -it $$ID bash
