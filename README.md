## FastAPI + mysql Compose application v1 

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/fastapi)

### Python/FastAPI application
-- Project structure:
```
├── db
│   └── password.txt
├── app
│   ├── main.py
│   ├── create_tables.py
│   ├── ...
│   └── Dockerfile
├── compose.yaml
├── requirements.txt
└── README.md

```

[_compose.yaml_](compose.yaml)
```
services:
  db:
  phpmyadmin:
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

## Expected result

After the application starts, navigate to `http://localhost:8000` in your web browser and you should see the following json response:
```
{
"message": "OK"
}
```



## Project relevant. How to play

1. Enter the container `docker-compose exec -it api /bin/bash`
2. Create the tables by executing `python create_tables.py`
3. Verify the creation by executing `docker exec -it fastapi-db-1 mysql -u root -p`,key in root when asked password,  `USE example`, `show tables;`, `SELECT * FROM ohlc_history;` || log in phpmyadmin http://localhost:8001/, username:root, password :root

4. Populate the table `python intg_test.py` to  -- By right, it should insert to test DB, but here we insert into PROD DB for convenience 
5. Execute `pytest` to run ALL the tests
Troubleshoot tips: if there are erros, run each test alone
`python connect_test.py` test DB connection
`python utils_test.py` test POST /data endpoint
`python connect_test.py` test DB manager

6. Test service by trying GET /, expected result is {"message": "OK"}

7. Before testing any endpoints...please authenticate yourself...POST /token, for now key in usrname and password as you like.

8. If you have run pytest in step 4, when you test POST/data endpoint, please make sure the data you are uploading here has no overlap of the data in the ohlv.csv. Otherwise it would be inserting the date twice, violating primary key.

9. verify the result by querying GET /data

10. Test GET with filer, pagination endpoints or sort: run tests on postman OR browser



## API docs
http://localhost:8000/docs
1. step authenticate client key in usename and password. For now it is not enforced, as long as you key in something, it will work
2. Try out the endpoints you like


Stop and remove the containers
```
$ docker compose down
```


## function extension
sort: order by
aggregation : group by