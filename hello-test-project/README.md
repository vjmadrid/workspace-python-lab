

[tox]
isolated_build = True
envlist = py37,py38,py39

[testenv]
deps =
    black
    coverage
    flake8
    mccabe
    mypy
    pylint
    pytest
commands =
    black acme-project
    flake8 acme-project
    pylint acme-project
    mypy acme-project
    coverage erase
    coverage run --include=acme-project/* -m pytest -ra
    coverage report -m


$ tox -e py39