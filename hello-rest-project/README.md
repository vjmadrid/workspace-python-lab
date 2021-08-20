# hello-rest-project

docker build -t acme/hello-rest-project .

docker run -d -p 5000:5000 acme/hello-rest-project

http://localhost:5000/

curl http://localhost:5000