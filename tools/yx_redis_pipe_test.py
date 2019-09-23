# -*- coding:utf-8 -*-

import redis
import time
from concurrent.futures import ProcessPoolExecutor

r = redis.Redis(host='127.0.0.1', port=37379, password='')
count = 100
for i in range(count):
	r.zadd("ttt", {str(i): i})

def try_pipeline():
    start = time.time()
    with r.pipeline(transaction=False) as p:
        # p.sadd('seta', 1).sadd('seta', 2).srem('seta', 2).lpush('lista', 1).lrange('lista', 0, -1)
        for i in range(count):
    		p.zscore("ttt", str(i))
        p.execute()
    print("try_pipeline : ")
    print time.time() - start


def without_pipeline():
    start = time.time()
    for i in range(count):
    	r.zscore("ttt", str(i))
    # r.sadd('seta', 1)
    # r.sadd('seta', 2)
    # r.srem('seta', 2)
    # r.lpush('lista', 1)
    # r.lrange('lista', 0, -1)
    print("without_pipeline : ")
    print time.time() - start


without_pipeline()
try_pipeline()

# def worker():
#     while True:
#     	without_pipeline()
#         try_pipeline()

# with ProcessPoolExecutor(max_workers=1) as pool:
#     for _ in range(10):
#         pool.submit(worker)