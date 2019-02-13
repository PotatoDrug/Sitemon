#!/usr/bin/env python3
import sqlite3

db_file = 'main/database.db'


def create_connection(fname):
    """ create a database connection to the SQLite database
        specified by the fname
    :param fname: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(fname)
        return conn
    except Exception as e:
        print(e)

    return None


def get_urls_by_user(username):
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute('SELECT url FROM watchlist WHERE username=?', (username,))
    urls = cur.fetchall()
    conn.close()
    return urls


tmp = get_urls_by_user('default')
print(type(tmp))
for index, url in enumerate(tmp):
    print('{}. {}'.format(index+1, url[0]))
