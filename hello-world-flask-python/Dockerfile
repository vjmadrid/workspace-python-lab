# Pull official base image
FROM python:3.9.13-slim-buster


# Set environment variables
ARG ENV=local

ENV ENV=${ENV} \
    # python
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # app
    APP_HOME=/app \
    PYTHONPATH="src" \
    SERVER_HOST="0.0.0.0"

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends netcat

# Set work directory
WORKDIR $APP_HOME

# Install dependencies to the local user directory (eg. /root/.local)
RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt $APP_HOME/
RUN pip install -r requirements.txt

# Copy project
COPY app.py $APP_HOME/

# Run python3
CMD ["python", "app.py"]