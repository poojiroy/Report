import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_weather_with_city(client):
    response = client.get('/weather?city=Hyderabad')
    assert response.status_code == 200
    data = response.get_json()
    assert data['city'] == 'Hyderabad'

def test_weather_without_city(client):
    response = client.get('/weather')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
