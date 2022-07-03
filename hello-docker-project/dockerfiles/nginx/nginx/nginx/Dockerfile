# Pull official base image
FROM nginx:1.21.6

# Remove existing/default nginx config file
RUN rm -f /etc/nginx/conf.d/default.conf

# Copy custom nginx config file to nginx config dir
#COPY ./nginx-compose.conf /etc/nginx/conf.d/nginx.conf
#ADD ./nginx-compose.conf /etc/nginx/nginx.conf
# Replace with our own nginx.conf
ADD ./nginx3.conf /etc/nginx/conf.d/
