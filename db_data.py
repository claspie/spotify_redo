from json import loads, dumps;
from keys.db import host, user, password, db, port;
import mysql.connector as mysql;

mycon = mysql.connect(
    host=host,
    user=user,
    passwd=password,
    port=port,
    database=db
)

mycon.close();