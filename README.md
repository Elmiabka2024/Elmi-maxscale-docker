# MariaDB MaxScale Sharded Database with Docker

## Introduction

This project sets up a basic MariaDB sharded environment using MaxScale and Docker. It includes:

Two MariaDB containers (shard1 and shard2), each hosting:

zipcodes_one (on shard1)

zipcodes_two (on shard2)
One MaxScale container to route client queries based on the schema.


## Getting Start
```bash
git clone git@github.com:Elmiabka2024/elmi-maxscale-docker.git
cd elmi-maxscale-docker
```

---

## Building

```
build the image to start up
```
sudo docker compose up build
 sudo docker compose up -d
```

## Running
Make sure you are in the root project directory where your configuration files and SQL data files are located
 ```
docker-compose.yml
maxscale.cnf.d/example.cnf
```

check running containers
```
sudo docker ps
```
stop and clean up the environment
```
sudo compose down
```

remove volumes

```
sudo docker compose down v
```

## Configuration

MaxScale Setup
MaxScale is configured via a mounted config file located at:


```./maxscale/maxscale.cnf.d/example.cnf
```

Key configuration components:

Shard1 and Shard2: Two MariaDB instances (masters) for sharding

Router: schemarouter — routes queries based on database name

Monitor: mariadbmon for basic health checking (auto-failover disabled)

Listener: Listens on port 4006
### Databases
shard1.sql 
 contains the zipcodes_one database

shard2.sql

contains the zipcodes_two database

### Authentication
MaxScale and the shards use the following credentials (defined in user.sql and used in MaxScale config):

Username:
``` maxuser```

Password:
```maxpwd```

These credentials are used by:

MaxScale to connect to the shards

The Python client to connect to MaxScale

### ports
shard1: host port 4001 and container port 3306
shard2: host port 4002 and container port 3306
maxscale: exposes listener on port 4006

## Connecting to containers


connect to shard1 
```
sudo docker exec -it shard1 mysql -u root
```
connect to shard2

```
sudo docker exec -it shard2 mysql -u root

```
### Connect to MaxScale

MaxScale is configured to route queries using the schemarouter module.
This means:

It routes queries based on the schema (database) name

You query via a single port (4006), and MaxScale decides which backend (shard)

 
from your local terminal run:
```
mysql -h 127.0.0.1 -P 4006 -u maxuser -p
```
Enter```maxpwd```
 when prompted for password 

Once connected, run queries like:
```
USE zipcodes_one;
SELECT * FROM zipcodes_one WHERE State = 'KY';
```

## To check for servers status:

To inspect the health and status of the backend shards:

```
sudo docker compose exec maxscale maxctrl list servers```

┌────────┬─────────┬──────┬─────────────┬─────────────────┬──────┐
│ Server │ Address │ Port │ Connections │ State           │ GTID │
├────────┼─────────┼──────┼─────────────┼─────────────────┼──────┤
│ shard1 │ shard1  │ 3306 │ 0           │ Master, Running │      │
├────────┼─────────┼──────┼─────────────┼─────────────────┼──────┤
│ shard2 │ shard2  │ 3306 │ 0           │ Running         │      │
└────────┴─────────┴──────┴─────────────┴─────────────────┴──────┘

