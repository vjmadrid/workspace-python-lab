# Makefile
#
# Author: vjmadrid
# Last Change: March 1, 2020
# URL: 

# **********************************
# 			Makefile Setup
# **********************************

# Shell Setup
SHELL := /bin/bash

# Text Format Constants
BOLD=`tput bold`
UNDERLINE_ON=`tput smul`
UNDERLINE_OFF=`tput rmul`

TEXT_BLUE=`tput setaf 4`
TEXT_BLACK=`tput setaf 0`
TEXT_RED=`tput setaf 1`
TEXT_GREEN=`tput setaf 2`
TEXT_YELLOW=`tput setaf 3`
TEXT_BLUE=`tput setaf 4`
TEXT_MAGENTA=`tput setaf 5`
TEXT_CYAN=`tput setaf 6`
TEXT_WHITE=`tput setaf 7`

RESET_FORMATTING=`tput sgr0`



# **********************************
# 			Python Setup
# **********************************

# Python
PYTHON_VERSION :=  $(shell python --version)
PYTHON_PATH := $(shell which python)


# Pyenv Setup
VIRTUAL_ENV_NAME_DEFAULT = venv

PYENV_PATH := $(PYENV_ROOT)
PYENV_VIRTUAL_ENV_PATH := $(PYENV_VIRTUAL_ENV)
PYENV_VERSION := $(shell pyenv version)


# Tools Setup
MAKE_TOOL := make --no-print-directory

PYTHON_TOOL = python
PYENV_TOOL = pyenv
VIRTUALENV_TOOL = virtualenv
PACKAGE_TOOL = pip
TEST_TOOL = pytest
DOCKER_TOOL = docker

# Commands

PYENV_CMD = ${PYENV_TOOL}
VIRTUALENV_CMD = ${VIRTUALENV_TOOL}
PACKAGE_CMD = $(PYTHON_TOOL) -m $(PACKAGE_TOOL)
TEST_CMD = $(PYTHON_TOOL) -m $(TEST_TOOL)

DOCKER_CMD = ${DOCKER_TOOL}


# **********************************
# 			Project Setup
# **********************************

PROJECT_CURRENT_PATH := $(shell pwd)
PROJECT_NAME := $(shell basename $(PROJECT_CURRENT_PATH))
#VERSION := $(shell python -c "import sys; import $(MODULE); sys.stdout.write($(MODULE).__version__)")
#SOURCES := $(shell find $(MODULE) -name '*.py') #$(shell find $(MODULE) -name '*.py')

MODULE := helloworld

DOCKER_REGISTRY :=docker.acme
DOCKER_IMAGE := $(DOCKER_REGISTRY)/$(MODULE)

TAG :=v1.0

# Virtualenv local Setup

VIRTUAL_ENV_LOCAL_NAME = $(VIRTUAL_ENV_NAME_DEFAULT)
VIRTUAL_ENV_LOCAL_PATH = $(PROJECT_CURRENT_PATH)/$(VIRTUAL_ENV_LOCAL_NAME)

VIRTUAL_ENV_PATH := $(PYENV_VIRTUAL_ENV_PATH)

TEST=KK


# **********************************
# 			Commands Setup
# **********************************



# **********************************
# 			Actions
# **********************************

# "    make install    install the package in a virtual environment"
	#  "    make reset      recreate the virtual environment"
	#  "    make check      check coding style (PEP-8, PEP-257)"
	#  "    make test       run the test suite, report coverage"
	#  "    make tox        run the tests on all Python versions"
	# "    make readme     update usage in readme"
	#  "    make docs       update documentation using Sphinx"
	#  "    make publish    publish changes to GitHub/PyPI"


# *****************************************
#  	  ____                           _ 
# 	 / ___| ___ _ __   ___ _ __ __ _| |
#	| |  _ / _ \ '_ \ / _ \ '__/ _` | |
#	| |_| |  __/ | | |  __/ | | (_| | |
#	 \____|\___|_| |_|\___|_|  \__,_|_|
#
# *****************************************



# *** help : show help info ***
help:
	@echo""
	@echo "Usage: make [<goal>]"
	@echo ""
	@echo "Goals:"
	@echo -e "\t${TEXT_GREEN}help${RESET_FORMATTING}\t\t show help info"
	@echo -e "\t${TEXT_GREEN}info${RESET_FORMATTING}\t\t show project info"
	@echo -e "\t${TEXT_GREEN}clean${RESET_FORMATTING}\t\t cleanup all temporary files"
	@echo -e "\t${TEXT_GREEN}freeze ${RESET_FORMATTING}\t\t write the requirements to file"
	@echo ""
	@echo "Virtual Enviroment Goals:"
	@echo -e "\t${TEXT_GREEN}clean-venv-local${RESET_FORMATTING}\t clean/delete the virtual environment local"
	@echo -e "\t${TEXT_GREEN}install-venv-local${RESET_FORMATTING}\t clean/delete the virtual environment local"
	@echo ""
	@echo "Docker Goals:"
	@echo -e "\t${TEXT_GREEN}clean-docker${RESET_FORMATTING}\t\t xxx"
	@echo -e "\t${TEXT_GREEN}build-docker-dev${RESET_FORMATTING}\t xxx"
	@echo



# *** default-init : initial template ***
default-init:
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] Scanning for projects..."
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] ---< ${TEXT_CYAN}${PROJECT_NAME}${RESET_FORMATTING} >---"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] \t- Project Current Path : ${TEXT_GREEN}$(PROJECT_CURRENT_PATH)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] \t- Project Name : ${TEXT_GREEN}$(PROJECT_NAME)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] ------------------------------------------------------------------------"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]"



# *** default-end : end template ***
default-end:
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] ------------------------------------------------------------------------"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] ${TEXT_GREEN}BUILD SUCCESS${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] ------------------------------------------------------------------------"



# *****************************************
# 			 ___        __       
#			|_ _|_ __  / _| ___  
# 		 	 | || '_ \| |_ / _ \ 
# 		 	 | || | | |  _| (_) |
#			|___|_| |_|_|  \___/ 
#
# *****************************************


# *** info ***
info: default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:info${RESET_FORMATTING} ${BOLD}(default-info)${RESET_FORMATTING} ---"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] Python Setup"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] \t- Python Version : ${TEXT_GREEN}$(PYTHON_VERSION)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] \t- Python Path : ${TEXT_GREEN}$(PYTHON_PATH)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] Pyenv Setup"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] \t- Pyenv Path : ${TEXT_GREEN}$(PYENV_PATH)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] \t- Pyenv Virtual Env Path : ${TEXT_GREEN}$(PYENV_VIRTUAL_ENV_PATH)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] \t- Pyenv Virtual Env Name : ${TEXT_GREEN}$(PYENV_VERSION)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] Virtual Env"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] \t- Virtual Env Path : ${TEXT_GREEN}$(VIRTUAL_ENV_PATH)${RESET_FORMATTING}"



# *****************************************
# 		 __     __              
# 		 \ \   / /__ _ ____   __
#  		  \ \ / / _ \ '_ \ \ / /
#   	   \ V /  __/ | | \ V / 
#    		\_/ \___|_| |_|\_/  
#
# *****************************************

test-condition:
	@echo $(TEST)

	@if [ "$(TEST)" = "ON" ]; then echo "PASO1 PASSED"; else echo "PASO1 FAILED"; fi
	
	@if [ "$(TEST)" = "ON" ]; then \
		echo "PASO2 PASSED"; \
	else \
		echo "PASO2 FAILED"; \
	fi

ifeq ($(TEST),ON)
	@echo "EXTERNO PASSED"
else
	@echo "EXTERNO FAILED"
endif

	#test -d $(VIRTUAL_ENV_LOCAL_PATH)


# *** clean-venv-local : clean/delete the local virtual environment***
clean-venv-local:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:clean-venv-local${RESET_FORMATTING} ${BOLD}(default-clean-venv-local)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]   - VIRTUAL_ENV_LOCAL_NAME : ${TEXT_GREEN}$(VIRTUAL_ENV_LOCAL_NAME)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]   - VIRTUAL_ENV_LOCAL_PATH : ${TEXT_GREEN}$(VIRTUAL_ENV_LOCAL_PATH)${RESET_FORMATTING}"

	# Delete "venv" directory (if exist)
	@if [ -d "$(VIRTUAL_ENV_LOCAL_PATH)" ]; then \
		echo "Directory $(VIRTUAL_ENV_LOCAL_PATH) exists"; \
		rm -Rf "$(VIRTUAL_ENV_LOCAL_PATH)"; \
	fi

	@$(MAKE_TOOL) default-end

# *** clean-venv-pyenv : xxx***
clean-venv-pyenv:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:clean-venv-pyenv${RESET_FORMATTING} ${BOLD}(default-clean-venv-pyenv)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]   - PYENV_VIRTUAL_ENV_PATH : ${TEXT_GREEN}$(PYENV_VIRTUAL_ENV_PATH)${RESET_FORMATTING}"
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]   - PYENV_VERSION : ${TEXT_GREEN}$(PYENV_VERSION)${RESET_FORMATTING}"

	@$(MAKE_TOOL) default-end



# *** install-venv-local : create the local virtual environment local***
install-venv-local:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:install-venv-local${RESET_FORMATTING} ${BOLD}(default-install-venv-local)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"

	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]   - Install $(VIRTUALENV_TOOL)"
	@$(PACKAGE_TOOL) install $(VIRTUALENV_TOOL)

	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]   - Create Local Virtual Env -> $(VIRTUALENV_CMD) $(VIRTUAL_ENV_LOCAL_PATH)"
	@$(VIRTUALENV_CMD) $(VIRTUAL_ENV_LOCAL_PATH)
	@test -d $(VIRTUAL_ENV_LOCAL_PATH)

	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]   - Activate Local Virtual Env -> source ./$(VIRTUAL_ENV_LOCAL_NAME)/bin/activate"
	@source ./$(VIRTUAL_ENV_LOCAL_NAME)/bin/activate

	@$(MAKE_TOOL) default-end


install-venv-pyenv:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:install-venv-pyenv${RESET_FORMATTING} ${BOLD}(default-install-venv-pyenv)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"

	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}]   - Create Pyenv Virtual Env -> $(PYENV_CMD) ${VIRTUALENV_TOOL} 3.9.0 $(VIRTUAL_ENV_LOCAL_NAME)"
	$(PYENV_CMD) ${VIRTUALENV_TOOL} 3.9.0 $(VIRTUAL_ENV_LOCAL_NAME)

	@$(MAKE_TOOL) default-end




# *****************************************
#   		 ____             _     
#  			/ ___| ___   __ _| |___ 
# 		   | |  _ / _ \ / _` | / __|
# 		   | |_| | (_) | (_| | \__ \
#  			\____|\___/ \__,_|_|___/
#                          
# *****************************************


# *** clean : cleanup all temporary files ***
clean:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:clean${RESET_FORMATTING} ${BOLD}(default-clean)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	
	@rm -rf .pytest_cache __pycache__ .coverage coverage.xml build dist
	@$(MAKE_TOOL) default-end



# *** freeze : write the requirements to file ***
freeze:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:freeze${RESET_FORMATTING} ${BOLD}(default-freeze)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	
	@$(PACKAGE_TOOL) freeze > requirements.txt
	@$(MAKE_TOOL) default-end


# *** install ***
install:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:install${RESET_FORMATTING} ${BOLD}(default-install)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	
	@${PACKAGE_CMD} install -r requirements.txt
	# @${PACKAGE_CMD} install -e .
	@$(MAKE_TOOL) default-end



# *** run ***
run: clean
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:run${RESET_FORMATTING} ${BOLD}(default-run)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	@python -m flask run
	@$(MAKE_TOOL) default-end



# **********************************		
#     ____ _               _    
#  	 / ___| |__   ___  ___| | __
# 	| |   | '_ \ / _ \/ __| |/ /
# 	| |___| | | |  __/ (__|   < 
#	 \____|_| |_|\___|\___|_|\_\
#
# **********************************


# *** lint ***
lint:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:lint${RESET_FORMATTING} ${BOLD}(default-lint)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- Executing ${TEXT_GREEN}makefile:lint:flake8${RESET_FORMATTING} ${BOLD}(default-flake8)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	@flake8

	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- Executing ${TEXT_GREEN}makefile:lint:pylint${RESET_FORMATTING} ${BOLD}(default-pylint)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	@pylint --rcfile=setup.cfg *.py
	@$(MAKE_TOOL) default-end



# **********************************		
# 	 ____             _             
#	|  _ \  ___   ___| | _____ _ __ 
#	| | | |/ _ \ / __| |/ / _ \ '__|
#	| |_| | (_) | (__|   <  __/ |   
#	|____/ \___/ \___|_|\_\___|_|   
#
# **********************************

clean-docker:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:clean-docker${RESET_FORMATTING} ${BOLD}(default-clean-docker)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	
	@$(DOCKER_CMD) system prune -f --filter "label=name=$(MODULE)"
	@$(MAKE_TOOL) default-end

# make build-dev NAME=victor VERSION=1.0.0
build-docker-dev:
	@$(MAKE_TOOL) default-init
	@echo "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}makefile:build-docker-dev${RESET_FORMATTING} ${BOLD}(default-build-docker-dev)${RESET_FORMATTING} @ ${TEXT_CYAN}${MODULE}${RESET_FORMATTING} ---"
	@echo " - Name: ${TEXT_GREEN}$(NAME)${RESET_FORMATTING}"
	@echo " - Module: ${TEXT_GREEN}$(MODULE)${RESET_FORMATTING}"
	@echo " - Version: ${TEXT_GREEN}$(VERSION)${RESET_FORMATTING}"
	@echo " - Tag: ${TEXT_GREEN}$(TAG)${RESET_FORMATTING}"
	@echo " - DOCKER_IMAGE: ${TEXT_GREEN}$(DOCKER_IMAGE)${RESET_FORMATTING}\n"
	@sed                                 \
		-e 's|{NAME}|$(MODULE)|g'        \
		-e 's|{VERSION}|$(TAG)|g'        \
		dev.Dockerfile | $(DOCKER_CMD) build -t $(DOCKER_IMAGE):$(TAG) -f- .
	@$(MAKE_TOOL) default-end

