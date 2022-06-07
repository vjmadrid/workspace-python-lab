# Pull official base image
FROM python:3.9-alpine

# Set environment variables
ARG ENV=local

ENV ENV=${ENV} \
    # python
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # app
    APP_HOME=/app

# Set work directory
WORKDIR $APP_HOME

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt $APP_HOME
RUN pip install -r requirements.txt

# Copy project
COPY app.py $APP_HOME

# Run python3
CMD ["python", "app.py"]