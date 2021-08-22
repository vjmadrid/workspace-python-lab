clean:
	rm -rf ./acme_common.egg-info
	rm -rf ./build
	rm -rf ./dist

init:
	pip3 install -r requirements.txt

test:
	pytest

install-develop:
	python3 setup.py develop --uninstall
	python3 setup.py develop

uninstall-develop:
	python3 setup.py develop --uninstall

install:
	python3 setup.py install

local-distribute:
	python3 setup.py sdist

show-content:
	cp ./dist/acme-common-0.0.1.tar.gz ../

.PHONY: init test