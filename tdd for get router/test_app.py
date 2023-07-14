from app import app
import json

def test_get_weather_for_existing_city():
    with app.test_client() as client:
        response = client.get('/weather/San Francisco')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data['temperature'] == 14
        assert data['weather'] == 'Cloudy'

def test_get_weather_for_non_existing_city():
    with app.test_client() as client:
        response = client.get('/weather/Chicago')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert 'error' in data
        assert data['error'] == 'City not found'
