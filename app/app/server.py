from flask import Flask
import redis
import os

app = Flask(__name__)

print("Redis: "+os.environ["REDIS_HOST"])

r = redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)

@app.route("/set/<key>/<value>")
def setter(key, value):
    r.set(key, value)
    return "key set"
    
@app.route("/get/<key>")
def getter(key):
    return r.get(key)

