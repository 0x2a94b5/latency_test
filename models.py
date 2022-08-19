"""
Model
"""

import os
import sqlite3

from logs import logger

cur_dir = os.path.dirname(os.path.abspath(__file__))
db_name = 'latency.db'
db = os.path.join(cur_dir, db_name)

def create_model():
    try:
        conn = sqlite3.connect(db)
        with conn:
            cur = conn.cursor()
            cur.executescript("""
            CREATE TABLE IF NOT EXISTS latency -- latency record
                (id INTEGER PRIMARY KEY,
                local TEXT, -- location
                host TEXT, -- target host/server
                latency INTEGER, -- network latency 
                create_time INTEGER DEFAULT (strftime('%s', 'now')) -- record create time
            );
            """)
    except:
        logger.exception('Data Model Creation Failed')
