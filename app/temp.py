# ###################################
# # get Docker container IP address #
# ###################################
# # client = docker.DockerClient()
# # db_container = client.containers.get("kafka_stream_mariadb_1")
# # db_container.attrs['NetworkSettings']['Networks']['kafka_stream_default']['IPAddress'],
# # try:
# #     client = MongoClient('localhost:27017')
# #     print("dd")
# # except exceptions as e:
# #     print(f"Error connecting to MariaDB Platform: {e}")
# #
# #
# # def db_connection():
# #     try:
# #         print(f"Connecting to INFLUXDB Platform")
# #         return InfluxDBClient(
# #             host='localhost', port=8086, username='admin', password='admin'
# #         )
# #
# #     except exceptions as e:
# #         print(f"Error connecting to MariaDB Platform: {e}")
# #         sys.exit(1)
# #
# #
# # def close_connection(conn):
# #     conn.close()
# #     print("Maria connection is closed")
#
#
#
#
# # json_body = {
# #         "measurement": "brushEvents",
# #         "tags": {
# #             "user": "Carol",
# #             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
# #         },
# #         "fields": {
# #             "duration": 127
# #         }
# #     }
# # client = db_connection()
# # # client.create_database("example")
# # print(client.get_list_database())
# # client.write_points(json_body, "logs_db", protocol='json')
# # print(client.query('SELECT "duration" FROM "example"."autogen"."brushEvents" WHERE time > now() - 4d GROUP BY "user"'))
# # # consume_data()
#
#
#
#
#
#
#
#
# #  mariadb:
# #    image: "mariadb:10.2"
# #    environment:
# #      - MYSQL_ROOT_PASSWORD=admin
# #      - MYSQL_DATABASE=logs_db
# #      - MYSQL_USER=admin
# #      - MYSQL_PASSWORD=admin
# #    hostname: localhost
#
# #  adminer:
# #    image: adminer
# #    restart: always
# #    ports:
# #      - 8080:8080
#
# #  influxdb:
# #    image: influxdb:latest
# #    ports:
# #      - '8086:8086'
# #    environment:
# #      - INFLUXDB_DB=logs_db
# #      - INFLUXDB_ADMIN_USER=admin
# #      - INFLUXDB_ADMIN_PASSWORD=admin
# #  chronograf:
# #    image: chronograf:latest
# #    ports:
# #      - '127.0.0.1:8888:8888'
# #    depends_on:
# #      - influxdb
# #    environment:
# #      - INFLUXDB_URL=http://influxdb:8086
# #      - INFLUXDB_USERNAME=admin
# #      - INFLUXDB_PASSWORD=admin
#
#
#
# # from influxdb import InfluxDBClient, exceptions
# # # import pymysql
# # from pymongo import MongoClient
#
#
# # SELECT hour, COUNT(DISTINCT date_ip)
# # FROM logs
# # GROUP BY hour
# #   HAVING COUNT(DISTINCT date_ip) > 0
#
#
# SELECT hour, COUNT(DISTINCT date_ip) as unique_ip_count
# FROM logs
# GROUP BY hour
#
SELECT UNIX_TIMESTAMP(YEAR(date_time)) as time_sec, count(ip) as value, cast(hour as char(10)) as metric
FROM logs
group by 1,3
#
# # select YEAR(date_time), MONTH(date_time), count(distinct date_ip)
# # from logs
# # group by 1, 2
#
#
select now() as time, hour, count(distinct date_ip)
from logs

group by 2

# # SELECT UNIX_TIMESTAMP(DATE_FORMAT(time,'%H:%i:%s')) AS time_sec, MONTH(time), count(distinct date_ip)
# # FROM logs
# # group by 1, 2
# # having YEAR(time) == 2015
#
#
#
# SELECT DATE_FORMAT(time,'%H:%i:%s') AS time_sec, MONTH(time), count(distinct date_ip)
# FROM logs
# where YEAR(time) = 2019
# group by 1, 2
# limit 20
#
#
#
# select YEAR(date_time), MONTHNAME(date_time), DAY(date_time), count(distinct ip)
# from logs
# group by 1, 2, 3
#
#
# SELECT YEAR(time), MONTH(time), count(distinct date_ip)
# FROM logs
# group by 1,2
# #
# # from datetime import datetime
# #
# #
# # nb = {'time': '2019-05-14 12:14:08', 'ip': '10.0.207.93', 'status_code': 586}
# #
# # date = (nb.get('time').split(' ')[0])
# # times = (nb.get('time').split(' ')[1])
# # hour = ((nb.get('time').split(' ')[1]).split(':')[0])
# #
# # date_ip = (nb.get('time').split(' ')[0] + "_" + nb.get('ip'))
# #
# #
# #
# # print(date, times, hour, date_ip)
# #
# #
# # print(datetime.strptime(nb.get('time'), "%Y-%m-%d %H:%M:%S"))
# import time
#
# animation = "|/-\\"
# idx = 0
# while True:
#     print(animation[idx % len(animation)], end="\r")
#     idx += 1
#     time.sleep(2)


from kafka import KafkaProducer
from json import dumps
import subprocess
import ast
import sys
from resources.utils import (
    SCRIPTS_DIR,
    topics,
    log_set
)

proc = subprocess.Popen(
    [
        r"C:\Program Files\Git\bin\bash.exe",
        SCRIPTS_DIR / 'logs.sh'
    ],
    stdout=subprocess.PIPE
)
while True:
    line = proc.stdout.readline()
    if not line:
        break
    # the code does filtering here
    print(ast.literal_eval(line.decode("utf8").rstrip()))