"""
Latency Test
"""

import sys
import time
import sqlite3
from threading import Thread

from tcp_latency import measure_latency

from models import create_model, db
from configs import config, file
from logs import logger

def add_record(local, host, latency):
    try:
        conn = sqlite3.connect(db)
        with conn:
            cur = conn.cursor()
            cur.execute('''
                INSERT INTO latency (local, host, latency)
                VALUES (?, ?, ?)''', (local, host, latency)
            )
    except:
        logger.exception('Add Record Failed.')

def get_latency(local, host, port, timeout):
    try:
        res = measure_latency(host=host, port=port, timeout=timeout)
        if res:
            latency = round(res[0])
            add_record(local, host, latency)
    except:
        logger.exception('Get Latency Failed.')

if __name__ == '__main__':
    print('Latency Test Starting...')

    create_model()

    try:
        while True:
            config.read(file)
            local = config.get('default', 'local')
            hosts = config.get('default', 'hosts').split()
            port = config.getint('default', 'port')
            timeout = config.getint('default', 'timeout')

            t_list = []
            for host in hosts:
                t = Thread(target=get_latency, args=(local, host, port, timeout))
                t.start()
                t_list.append(t) 

            for t in t_list:
                t.join()

            time.sleep(60)

    except KeyboardInterrupt:
        logger.info('Latency Test Exit.')
        sys.exit(0)

    except Exception as e:
        logger.exception('Latency Test Error.')
        sys.exit(1)
