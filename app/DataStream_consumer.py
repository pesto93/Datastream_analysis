# _author_ = Johnleonard C.O
# _Date_ = 6/6/2020

from kafka import KafkaConsumer
from json import loads
from datetime import datetime
from resources.utils import (
    topics,
    close_connection,
    connections,
    log_set,
    cursor,
)


def insert_log_db(cur: cursor, msg: dict):
    """
    Function inserts consumed data into our database to load into grafana for almost real time analysis.
    :param cur: mysql cursor instance
    :param msg: data to insert
    :return:
    """
    sql = "INSERT INTO logs (date_time, ip, status_code, date_ip, hour, time) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (
        datetime.strptime(msg.get("time"), "%Y-%m-%d %H:%M:%S"),
        msg.get("ip"),
        msg.get("status_code"),
        msg.get("time").split(" ")[0] + "_" + msg.get("ip"),
        (msg.get("time").split(" ")[1]).split(":")[0],
        datetime.strptime(msg.get("time"), "%Y-%m-%d %H:%M:%S").time(),
    )
    # log_set.info(f"INSERT INTO logs {val}")
    cur.execute(sql, val)


def consume_data(cur: cursor):
    """
    The function handles the kafka consumer instance.
    The messages published into topics are then utilized by Consumers apps.
    A consumer gets subscribed to the topic of its choice and consumes data.
    which in this case we subscribed only to the error status code (which we need to log) even though we are streaming all
    logs. The group_id makes it possible for consumer to only consume new los, meaning it keeps track of already consumed logs.
    :param cur: mysql cursor instance
    :return:
    """
    consumer = KafkaConsumer(
        bootstrap_servers="localhost:9094",
        auto_offset_reset="earliest",
        group_id="log_group",
        enable_auto_commit=True,
        consumer_timeout_ms=100000,
        value_deserializer=lambda x: loads(x.decode("utf-8")),
    )
    # consumer subscription happens here.
    consumer.subscribe(topics.get("500"))
    for message in consumer:
        messages = message.value
        insert_log_db(cur, messages)
    # close consumer connection when no message is received after timeout
    consumer.close()
    log_set.info("Closed Consumer after idling")


def create_log_table(cur: cursor):
    """
    Function creates a new table if table do not already exist in MySQL database
    :param cur: mysql cursor instance
    :return:
    """
    cur.execute(
        f"""
                        CREATE TABLE IF NOT EXISTS logs (
                            date_time DATETIME,
                            ip VARCHAR (225),
                            status_code INT,
                            date_ip VARCHAR (225),
                            hour int,
                            time TIME
                        )
        """
    )


if __name__ == "__main__":
    conn, cursor = connections()
    create_log_table(cursor)
    consume_data(cursor)
    close_connection(conn=conn, cur=cursor)
