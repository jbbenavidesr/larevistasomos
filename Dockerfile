# Pull base image
FROM python:3.8

WORKDIR /code

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install operating system dependencies
RUN apt-get update -y && \
    apt-get install -y apt-transport-https rsync gettext libgettextpo-dev && \
    curl -sL https://deb.nodesource.com/setup_lts.x | bash - &&\
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code/static_src/

# Install front-end dependencies
COPY ./static_src/package.json ./static_src/package-lock.json /code/static_src/
RUN npm install

# Install Python dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Compile static files
COPY ./static_src/ /code/static_src/
RUN npm run production

WORKDIR /code

# Copy project
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput --clear