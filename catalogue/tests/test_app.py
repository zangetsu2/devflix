# catalogue/tests/test_app.py
import json
from app import app

def test_get_movies():
    client = app.test_client()
    response = client.get('/movies')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) >= 1
