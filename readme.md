## Data Stream with Kafka, MySQL and Grafana

Multi-container Docker app built from the following services:

* [kafka/Zookeeper](https://kafka.apache.org/) - distributed streaming platform
* [Adminer](https://www.adminer.org/) - admin UI for Databases
* [Grafana](https://grafana.com/) - visualization UI
* [MySQL](https://www.mysql.com/) - Database


![alt text](CVSHealth_Logo.gif)


## Quick Start
In order to run this project you need to have Python, docker plus docker-compose installed
on your local machine.

To start the app:

1. Install [docker/docker-compose](https://docs.docker.com/compose/install/).
1. Install [Python](https://www.python.org/downloads/).
1. Clone this repo.
1. Run the following command from the root of the cloned repo:
     <br /> . ```pip3 install -r requirements.txt (Python 3)``` to install python libs 
     for this project.
     <br />. ```docker-compose up ``` to build docker containers.
     <br />. ```docker-compose down ``` to stop docker containers.


## Ports
The services in the project run on the following ports 
(you can confirm if the services started properly) :

Host Port | Service
------------ | -------------
| http://localhost:3000/      | Grafana       |
|http://localhost:8080/       | Adminer       | 
|:9092       | Kafka         | 

## Users

The service creates two admin users - one for MySQL and one for Grafana. 

- `MYSQL_USER=user`
- `MYSQL_PASSWORD=userpass`
- `MYSQL_ROOT_PASSWORD=admin`
- `GF_SECURITY_ADMIN_USER=admin`
- `GF_SECURITY_ADMIN_PASSWORD=admin`

## MySQL Database
The service creates a default InfluxDB database called `log_stream`.

## Adminer login
[Adminer Page](http://localhost:8080/ ) and fill out the details
<br> 
<br> ![alt text](images/db_login.PNG)


## Grafana
Our grafana will be reading data from our mysql db in almost real time depending on the
refresh rate.

Check  [Grafana Page](http://localhost:3000/ ) and fill out the username and password.
<br> click login and skip password change.
<br>
<br>![alt text](images/grafana_login.PNG)
<br>
#### Grafana datasource setup
Setup and save
<br>
<br>![alt text](images/datasource.PNG)
<br>

#### Grafana Dashboard
By default, the app does not create any Grafana dashboards. But we will create
2 or 3 table dashboard to monitor unique ips per hour etc using sql queries.
To make additional dashboards, see the Grafana 
[documentation](https://grafana.com/docs/grafana/latest/features/datasources/mysql/#time-series-queries).
<br>
<br>![alt text](images/dashboard1.PNG)
<br>
<br>![alt text](images/dashboard2.PNG)



##Usage


* utils.py
```
Dependencies:
    logging
    sys
    pathlib
    pymysql
```
This module is responsible for little micro functions services mainly 
such as setting up logging, db connections, topic dict etc.

* DataStream_producer.py
```
Dependencies:
    subprocess
    ast
    KafkaProducer
    json
```
Kafka Producer reads stdout logs from logs.sh and pushes it to different topics.

* DataStream_consumer.py
```
Dependencies:
   KafkaConsumer
   json
   datetime
```
Kafka consumer which consumers and keeps track of data consumed from the producer.

* logs.sh
```
Produces the logs consumed by kafka.
```


* grafana.sql
```
Contains some sql script for grafana dashboard to view
tables in real time.
```





## Information
Run the script as a module 
- run : ` python -m CVShealth.controller `


P.S : Dont hesitate to reach out if there is an issues.