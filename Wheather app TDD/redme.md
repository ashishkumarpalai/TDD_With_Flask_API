Flask Weather Application
The Flask Weather Application is a RESTful API that provides weather information for cities. It allows users to perform CRUD (Create, Read, Update, Delete) operations on the weather data. The application is built using the Flask framework and follows the Test-Driven Development (TDD) approach.

# Features
Retrieve Weather Data: The application provides a GET API endpoint /weather/<string:city> that retrieves and returns the weather information for a given city. The response is a JSON object containing the temperature and weather conditions.

Add Weather Data: The application supports adding new weather data for cities using a POST API endpoint /weather. Users can provide the city name, temperature, and weather conditions as input in a JSON object in the request body. Upon successful addition, a success message is returned.

Update Weather Data: Users can update the weather data for a specific city using a PUT API endpoint /weather/<string:city>. They can provide the updated temperature and/or weather conditions in a JSON object in the request body. The application updates the specified fields for the city and returns a success message.

Delete Weather Data: The application allows users to delete the weather data for a given city using a DELETE API endpoint /weather/<string:city>. Upon successful deletion, a success message is returned.

$Data Storage
The weather data for cities is stored in memory using a Python dictionary. The initial weather data includes cities such as San Francisco, New York, Los Angeles, Seattle, and Austin, along with their respective temperature and weather conditions.

Test-Driven Development (TDD)
The application follows the Test-Driven Development (TDD) approach, where test cases are written before implementing the corresponding functionality. The tests cover the CRUD operations, ensuring the application functions correctly and meets the expected behavior. The tests are written using the pytest framework.

# Technology Stack
Python
Flask
JSON
pytest
Installation and Usage
To run the Flask Weather Application:

# Install Python on your machine.
Clone the project repository and navigate to the project directory.
Install the required dependencies using pip install -r requirements.txt.
Run the application using the command python app.py.
The application will start running on http://localhost:5000.
You can use tools like cURL or Postman to interact with the API endpoints and perform CRUD operations on the weather data.

# Conclusion
The Flask Weather Application provides a convenient and flexible way to retrieve, add, update, and delete weather data for cities. By following the Test-Driven Development approach, the application ensures reliability and accuracy in its functionality. The use of a Python dictionary for data storage simplifies the application's setup and allows for quick access to weather information.
