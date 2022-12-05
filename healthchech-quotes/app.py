import os
import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "WORKING"

@app.route("/quotes")
def quotes():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.txt)
    quote = '"{}" - {}'.format(json_data[0]['q'], json_data[0]['a'])
    return(quote)

@app.route("//healthcheck", methods=["GET"])
def healthcheck():
    return "WORKING"

app.run(port=int(os.environ.get("PORT", "5000")), host="0.0.0.0")