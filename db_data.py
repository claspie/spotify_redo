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


def fetch_songs(year, category):
    cursor = mycon.cursor();
    query = f"SELECT title, artist FROM {year}_{category};"

    cursor.execute(query);
    result = cursor.fetchall();
    table = [];
    for row in result:
        results = {
            "name": row[0].replace("\n", ""),
            "artist": row[1].replace("\n", "").rsplit(" ")[0],
            "real_artist": row[1].replace("\n", "")
        }
        table.append(results)
    cursor.close();
    mycon.close()
    return table;
