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

def test_add_weather():
    with app.test_client() as client:
        response = client.post('/weather', json={'city': 'Chicago', 'temperature': 18, 'weather': 'Cloudy'})
        data = json.loads(response.data)

        assert response.status_code == 200
        assert 'message' in data
        assert data['message'] == 'Weather data added for Chicago'

        # Additional verification
        response = client.get('/weather/Chicago')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data['temperature'] == 18
        assert data['weather'] == 'Cloudy'

def test_update_weather():
    with app.test_client() as client:
        # Add initial weather data for New York
        client.post('/weather', json={'city': 'New York', 'temperature': 20, 'weather': 'Sunny'})

        # Update the temperature for New York
        response = client.put('/weather/New York', json={'temperature': 22})
        data = json.loads(response.data)

        assert response.status_code == 200
        assert 'message' in data
        assert data['message'] == 'Weather data updated for New York'

        # Verify the updated temperature
        response = client.get('/weather/New York')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data['temperature'] == 22
        assert data['weather'] == 'Sunny'  # Ensure weather remains unchanged

def test_delete_weather():
    with app.test_client() as client:
        # Add initial weather data for Seattle
        client.post('/weather', json={'city': 'Seattle', 'temperature': 10, 'weather': 'Rainy'})

        # Delete the weather data for Seattle
        response = client.delete('/weather/Seattle')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert 'message' in data
        assert data['message'] == 'Weather data deleted for Seattle'

        # Verify that Seattle is not found
        response = client.get('/weather/Seattle')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert 'error' in data
        assert data['error'] == 'City not found'
