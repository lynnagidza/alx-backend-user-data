#!/usr/bin/env python3
""" Tasks 0 to 4"""
import logging
import re
from typing import List
import os
import datetime
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


# Task 0. Regex-ing
def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
# end of Task 0


# Task 1. Log formatter
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            msg, self.SEPARATOR)
# end of Task 1


# Task 2. Create logger
def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        f'{datetime.datetime.now()} - %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
# end of Task 2


# Task 3. Connect to secure database
def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    connector = mysql.connector.connect(
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME'))
    return connector
# end of Task 3


# Task 4. Read and filter data
def main():
    """reads and filters data"""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        string = ''
        for key in row:
            string += f'{key}={row[key]}; '
        logger.info(string)
    cursor.close()
    db.close()
# end of Task 4


if __name__ == '__main__':
    main()
