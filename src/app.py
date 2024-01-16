from flask import Flask
import json
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({"message": "Hello, World!"})


@app.route('/health')
def health():
    return json.dumps({"message": "Healthy!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
