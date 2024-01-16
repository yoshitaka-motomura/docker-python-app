import json
from src.app import app as flask_app
client = flask_app.test_client()


def test_get_request():
    response = client.get("/")
    res = json.loads(response.data.decode("utf-8"))
    assert res["message"] == "Hello, World!"
    assert response.status_code == 200
