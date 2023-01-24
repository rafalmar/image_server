# Image Server API

A simple REST API for uploading and serving images. Done as a Python recruitment ask.
Each image is rescaled to a given width and height just before save to storing directory.

Created by using Django Rest Framework, Docker and Postgres

## Before run
Create `.env` file in the main directory of the project. Three variables must be set there. Exemple:
> POSTGRES_DB=postgres  
POSTGRES_USER=user  
POSTGRES_PASSWORD=password

Use values of your choice.

## Run
### Requirements
docker, docker-compose

### Build images and run containers
`$ make build`

It will run django server at localhost:8001 and postgres server at localhost:8002
Both containers share a volume - an image storage.

### Stop
`$ make down`

## Run tests
Tests are only available locally - when containers run.

### Requirements
python 3.10, pip

1. create python virtual environment
2. cd to cloned directory
2. `pip install -r requirements.txt`
3. `$ pytest`

## Endpoints
- `POST /images/`
  - see test/test_endpoint.py for exemplary usage or go to http://localhost:8001/images/ to upload some image
- `GET /images/`
  - Run get against http://localhost:8001/images/ to obtain paginated list of all image objects
  - Each object is returned with following set of attributes: `id`, `url`, `title`, `width` `height`
  - Endpoint allows for filtering based on piece of title string. `title` parameter can be passed either by url parameter or in a body of the request.
  - e.g. http://localhost:8001/images/?title=test
- `GET /images/:id`
  - Endpoint returns an object of given id
  - e.g. http://localhost:8001/images/1
- `GET /docs/openapi-schema.yml`
  - Returns OpenAPI document
- `GET /swagger/`
  - Renders OpenAPI 3 documentation, generated automatically and adjusted.
  - note: swagger UI doesn't support body in GET requests
