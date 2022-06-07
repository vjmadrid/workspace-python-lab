
# General Configuration

VIRTUAL_LOCAL_ENV_NAME := venv
EXECUTION_DIRECTORY_BY_ENVIRONMENT := bin
EXECUTION_PATH := $(VIRTUAL_LOCAL_ENV_NAME)/$(EXECUTION_DIRECTORY_BY_ENVIRONMENT)

# Docker Configuration

IMAGE_NAME := acme/hello-world-python
CONTAINER_NAME := hello-world-python

venv:
	python3 -m venv $(VIRTUAL_LOCAL_ENV_NAME)
	$(EXECUTION_PATH)/pip install -r requirements.txt

venv-upgrade:
	$(EXECUTION_PATH)/pip install --upgrade pip

run: venv
	$(EXECUTION_PATH)/python app.py

docker-build:
	docker build --no-cache	-t $(IMAGE_NAME) .

docker-build-raspberrypi:
	docker build --no-cache	-t $(IMAGE_NAME) -f Dockerfile.arm32v7 .

docker-run:
	docker run --name $(CONTAINER_NAME) -p 5000:5000 -d $(IMAGE_NAME)

docker-stop: ##Execute docker stop
	ID=$$(docker ps -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker stop $$ID

docker-logs: ##Execute docker logs
	ID=$$(docker ps -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker logs $$ID

docker-ssh: ##Execute docker image with ssh
	ID=$$(docker ps -f name=$(CONTAINER_NAME) |tail -1 |colrm 12) && docker exec -it $$ID bash

docker-push-skynetpi:
	docker tag hello-world-python skynetpi.local:1000/hello-world-python
	docker push skynetpi.local:1000/hello-world-python