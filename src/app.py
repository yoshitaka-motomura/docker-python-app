from flask import Flask
import json
app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({"message": "Hello, World!"})