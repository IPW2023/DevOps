from flask import Flask

app = Flask(__name__)

@app.route("/echo/<text>")
def setter(text):
    return text
    
@app.route("/reverse/<text>")
def getter(text):
    return text[::-1]
