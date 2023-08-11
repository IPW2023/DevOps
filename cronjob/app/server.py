from flask import Flask
import redis
import os

app = Flask(__name__)

print("Redis: "+os.environ["REDIS_HOST"])

r = redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)

@app.route("/guess/<nr>")
def setter(nr):
    number = int(r.get("nr"))
    nr = int(nr)
    if nr < number:
        return "greater"
    elif nr > number:
        return "lower"
    else:
        return "got it"
