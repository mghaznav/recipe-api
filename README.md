# Recipe API

## Introduction
This is an API that supports an app where users can create, and save different recipes. This API handles user authentication, ingredient management and recipe management.

## Prerequisites
- Docker

## Running 

To build the docker image, cd in to the recipe-api directory and run:

```bash
docker compose build
```

Now it should be ready to run.

To run the image, simply use the Docker command:

```bash
docker compose up
```

This will launch the django server and map it to port 8000 on your machine. The local server can be accessed at [http://localhost:8000](http://localhost:8000).

## Stopping

Press Ctrl + c to stop (yes, its Ctrl + c even on Mac)

## Testing

Unit tests can be run on the application with the following command:

```bash
docker compose run --rm app sh -c "python manage.py test"
```

## Linting

Linting can be run on the application with the following command:

```bash
docker compose run --rm app sh -c "flake8"
```