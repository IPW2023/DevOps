from random import randint
import redis
import os

print("Redis: "+os.environ["REDIS_HOST"])
r = redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)
nr = randint(1,100)
print ("Reset to {}".format(nr))
r.set("nr", nr)
