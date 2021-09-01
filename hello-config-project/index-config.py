# !/usr/bin/env python11
"""Top-level script to invoke helloworld implementation"""

# *** MODULES ***

# Option 1 : Import module
# from src.hello import hello
from src.hello import hello

from os import environ, path
from dotenv import load_dotenv

import configparser
import toml


# Read local file `.env`
# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))
# config_toml = toml.load('config/.env')
load_dotenv("config/.env")

# Read local file `config.ini`
config_ini = configparser.ConfigParser()
config_ini.read("config/config.ini")

# Read local file `config.toml`
config_toml = toml.load("config/config.toml")


if __name__ == '__main__':
    hello.hello()

    print("Example with .ini  :: "+ str(config_ini['LOGGING']['LOG_CONFIG_FILE']))
    print("Example with .toml  :: "+ str(config_toml['logging']['log_config_file']))
    print("Example with .env  :: "+ str(environ.get("LOG_CONFIG_FILE")))

