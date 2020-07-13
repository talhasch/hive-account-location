import os
import sqlite3

this_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(this_dir, "cache.db")

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

def create_db():
    cursor.execute('CREATE TABLE IF NOT EXISTS cache (k text PRIMARY KEY, v text NOT NULL);')
    cursor.execute('CREATE TABLE IF NOT EXISTS skip_list (k text PRIMARY KEY);')
    conn.commit()

create_db()

def cache_set(k, v):
    cursor.execute("INSERT INTO cache (k,v) VALUES (?, ?)", [k,v])
    conn.commit()
    return cursor.lastrowid

def cache_get(k):
    cursor.execute("SELECT v FROM cache WHERE k = ?", [k])
    row = cursor.fetchone()
        
    if row is None:
        return None

    return row[0]

def cache_size():
    cursor.execute("SELECT count(k) FROM cache")
    row = cursor.fetchone()
    return row[0]


def skip_list_add(k):
    if skip_list_get(k) is None:
        cursor.execute("INSERT INTO skip_list (k) VALUES (?)", [k])
        conn.commit()
        return cursor.lastrowid


def skip_list_get(k):
    cursor.execute("SELECT k FROM skip_list WHERE k = ?", [k])
    row = cursor.fetchone()
        
    if row is None:
        return None

    return row[0]