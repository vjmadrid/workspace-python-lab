

docker build -t hello-crontab-project .

docker run -it --rm hello-crontab-project


*/5 * * * * docker exec docker_container scheduled-task.py

0 */1 * * *