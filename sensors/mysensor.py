import random
import redis
import time

# Connect to redis.
r = redis.Redis(host='myapp-redis', port=6379, db=0)
# Sample a new value random times between 100 ms and 2s
while True:
    time.sleep(float(random.randint(100, 2000))/1000)
    r.set("mysensor", random.randint(1, 10))
