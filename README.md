# MariaDB MaxScale Sharded Database with Docker

## Introduction

This project sets up a basic MariaDB sharded environment using MaxScale and Docker. It includes two MariaDB containers (`shard1` and `shard2`) each with their own database (`zipcodes_one` and `zipcodes_two`), and a MaxScale container for query routing.

This setup is ideal for assignment requirement  and  local testing use cases, as authentication has been disabled (passwordless root user).

---

## Running

To start the project: clone the repo

```bash
git clone git@github.com:Elmiabka2024/elmi-maxscale-docker.git
cd elmi-maxscale-docker
```

```
sudo docker compose up build
 sudo docker compose up -d
```
once the containers are running verify with
```
sudo docker ps
```
stop and clean upl the environment 
```
sudo compose down
```

remove volumes

```
sudo docker compose down v
```

## Configuration

### Databases
shard1.sql 
 contains the zipcodes_one database

shard2.sql

contains the zipcodes_two database

### Authentication
No password is used only root user

### Maxscale 
routes queries through the readwritesplit router

### ports
shard1: host port 4001 and container port 3306
shard2: host port 4002 and container port 3306
maxscale: exposes listener on port 4006

## MaxScale docker-compose.yml set up

```
version: '2'

services:
  shard1:
    image: mariadb:10.3
    container_name: shard1
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
    volumes:
      - ./init:/docker-entrypoint-initdb.d
    ports:
      - "4001:3306"

  shard2:
    image: mariadb:10.3
    container_name: shard2
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
    volumes:
      - ./init:/docker-entrypoint-initdb.d
    ports:
      - "4002:3306"

  maxscale:
    image: mariadb/maxscale:2.4.7
    container_name: maxscale
    depends_on:
      - shard1
      - shard2
    volumes:
      - ./maxscale.cnf:/etc/maxscale.cnf
    ports:
      - "4006:4006"
```

### connecting to databases

connect to shard1 
```
sudo docker exec -it shard1 mysql -u root
```
connect to shard2

```
sudo docker exec -it shard2 mysql -u root

```



