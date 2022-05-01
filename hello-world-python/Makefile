venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

venv-upgrade:
	venv/bin/pip install --upgrade pip

run: venv
	venv/bin/python main.py

docker/build:
	docker build --no-cache	-t hello-world-python .

docker/build/raspberrypi:
	docker build --no-cache	-t hello-world-python -f Dockerfile.arm32v7 .

docker/run:
	docker run -p 5000:5000 -d hello-world-python

docker/run/debug:
	docker run -p 5000:5000 -it hello-world-python

docker/push/skynetpi:
	docker tag hello-world-python skynetpi.local:1000/hello-world-python
	docker push skynetpi.local:1000/hello-world-python