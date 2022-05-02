#
# Makefile for Project Management
#  

SHELL = /bin/bash
.DEFAULT_GOAL := help
VIRTUAL_LOCAL_ENV_NAME := venv
START_FILE := ./app.py
CONTAINER_NAME := hello-flask-redis-project




# *** CLEAN ***

clean-build: #Remove elements for build
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '.pytest_cache' -type d | xargs rm -fr
	@find . -name '*.pytest_cache' -type d | xargs rm -fr
	@find . -name '*.pyc' -type d | xargs rm -fr

clean-test: #Remove test and coverage artifacts
	@rm -fr .tox/
	@rm -fr .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache

clean-pyc: #Remove Python file artifacts
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-distribute: #Remove *.egg-info files and *.egg, build and dist directories
	@rm -vrf build/ 
	@rm -vrf dist/ 
	@rm -vrf ./*.tgz 
	@rm -vrf .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean : clean-build clean-pyc clean-test clean-distribute  ## Remove all build, test, coverage and distribute Python artifacts



# *** GENERAL ***

upgrade: ##Upgrade Python modules : pip and setuptools
	pip install -U pip setuptools wheel



# *** LOCAL VIRTUAL ENVIRONMENT  ***

local-venv-init: ##Prepare Local Virtual Environment
	@make local-venv-create
	@make local-venv-upgrade
	@make deps-install-dev-local-venv

local-venv-create: #Create Virtual Environment
	python3 -m venv $(VIRTUAL_LOCAL_ENV_NAME)

local-venv-upgrade: ##Upgrade Virtual Environment Pip
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pip install --upgrade pip wheel

local-venv-remove: ##Remove Local Virtual Environment
	@rm -rf ./$(VIRTUAL_LOCAL_ENV_NAME)



# *** DEPENDENCIES LOCAL VIRTUAL ENVIRONMENT ***

deps-install-dev-local-venv: ##Install dependencies 'dev-requirements.txt' file (No versions) in the Local Virtual Environment
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pip install -r dev-requirements.txt
	@make deps-generate-requirements-local-venv

deps-generate-requirements-local-venv: ##Generate 'requirements.txt' file (With versions) in the Local Virtual Environment
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pip freeze | grep -v -- '^-e' > requirements.txt

deps-install-local-venv: ## Install dependencies 'requirements.txt' file (With versions) in the Local Virtual Environment
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pip install -Ur requirements.txt

deps-reset-local-venv: ## Reset all requirements in the Local Virtual Environment in the Local Virtual Environment
	$(VIRTUAL_LOCAL_ENV_NAME)/bin/pip freeze | xargs pip uninstall -y



# *** DEPENDENCIES ***

deps-install-dev: ##Install dependencies 'dev-requirements.txt' file (No versions)
	pip install -r dev-requirements.txt

deps-generate-requirements: ##Generate 'requirements.txt' file (With versions)
	pip freeze | grep -v -- '^-e' > requirements.txt

deps-install: ## Install dependencies 'requirements.txt' file (With versions)
	pip install -Ur requirements.txt

deps-reset: ## Reset all requirements in the Local Virtual Environment
	pip freeze | xargs pip uninstall -y



# *** RUN ***

run-local-venv: ## Run Application in the Local Virtual Environment
	PYTHONPATH=src $(VIRTUAL_LOCAL_ENV_NAME)/bin/python $(START_FILE)

run: ## Run Application
	PYTHONPATH=src python3 $(START_FILE)



# *** DOCKER ***

docker-build: ##Build docker image for default architecture 
	docker build --no-cache	-t $(CONTAINER_NAME) .

docker-run: ##Execute docker image for default architecture 
	docker run -p 5000:5000 -d $(CONTAINER_NAME)

docker-run-debug: ##Execute docker image for default architecture
	docker run -p 5000:5000 -it $(CONTAINER_NAME)




# *** HELP ***

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [target]"; \
	printf "%-40s %s\n" "target" "help" ; \
	printf "%-40s %s\n" "----------------------------------" "----------------------------------" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-40s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
	@echo "Check the Makefile to know exactly what each target is doing"


.PHONY: init test