## FastAPI + mysql Compose application v1 

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/fastapi)

### Python/FastAPI application

<!-- Project structure:
```
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── app
    ├── main.py
    ├── __init__.py

``` -->

```
├── db
│   └── password.txt
├── app
│   ├── src...
│   └── Dockerfile
├── compose.yaml
├── requirements.txt
└── README.md

```

[_compose.yaml_](compose.yaml)
```
services:
  api:
    build: .
    container_name: fastapi-application
    environment:
      PORT: 8000
    ports:
      - '8000:8000'
    restart: "no"

```

## Deploy with docker compose

```shell
docker-compose up -d --build
```

```shell
docker-compose ps
```

```shell
docker-compose logs -f;
``` 

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED              STATUS              PORTS                                               NAMES
7087a6e79610   5c1778a60cf8   "/start.sh"   About a minute ago   Up About a minute   80/tcp, 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   fastapi-application
```
## docs
http://127.0.0.1:8000/docs


## project relevant use
1. enter the container `docker-compose exec -it api /bin/bash`
2. create the tables by executing `create_table.py`
3. verify the creation by executing `docker exec -it fastapi-db-1 mysql -u root -p`, `USE example`, `show tables;`, `SELECT * FROM ohlc_history;` || log in phpmyadmin http://localhost:8001/

4. run unit tests and intg tests
`python intg_test.py`
`python test_file_processing.py`

OR

5. run tests on postman

## Expected result

After the application starts, navigate to `http://localhost:8000` in your web browser and you should see the following json response:
```
{
"message": "OK"
}
```

Stop and remove the containers
```
$ docker compose down
```
