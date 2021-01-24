# _author_ = Johnleonard C.O
# _Date_ = 6/7/2020

import sys
import logging
from pathlib import Path
from mysql.connector import connect, connection, cursor, Error


def _configure_logger() -> logging.Logger:
    """
    This function handles the logging setup which will replace print.
    Logging can be used for debugging purposes or just info printing
    :return: An instance of logging as logger
    """
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - Data Stream - %(message)s "
    )
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def connections() -> tuple:
    """
    Functions handles mysql database connections
    :return: Mysql connection and cursor instance
    """
    try:
        conn = connect(
            host="localhost",
            user="user",
            password="userpass",
            db="log_stream",
            auth_plugin="mysql_native_password",
        )
        conn.autocommit = True
        log_set.info("Acquired Connection to Mysql DB")
        return conn, conn.cursor()
    except Error as e:
        log_set.info(f"Error connecting to MYSQL Platform: {e}")


def close_connection(conn: connection, cur: cursor) -> None:
    """
    Function handle closing mysql connection
    :param conn: Mysql connection instance
    :param cur: Mysqlc cursor instance
    :return:
    """
    conn.close()
    cur.close()
    log_set.info("MYSQL connection is closed")


################
# GLOBAL SCOPE #
###############
log_set = _configure_logger()

##########
# TOPICS #
##########
topics = {
    "500": "error",
    "300": "moved",
    "400": "server_issue",
    "200": "ok",
    "others": "all_others",
}

#########
# PATHS #
#########
BASE_DIRECTORY = Path(__file__).resolve().parent.parent
SCRIPTS_DIR: Path = BASE_DIRECTORY / "scripts"
