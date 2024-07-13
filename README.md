# python-sonarqube
PythonAppWithSonarQube is a sample Python application that demonstrates how to integrate SonarQube for continuous code quality inspection. SonarQube is an open-source platform used to analyze and measure code quality and provide continuous code inspection.


## Project Structure

```
python-sonarqube/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_utils.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── sonar-project.properties
├── run_tests.sh
├── README.md
```

### Prerequisites

- Docker
- Python 3.x
- `pylint`, `pytest`, `pytest-cov`, and `requests` libraries

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python-sonarqube.git
   cd python-sonarqube
   ```

2. **Set up the Docker container:**
   ```bash
   docker-compose up -d
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the application:**
   ```bash
   docker build -t python-app .
   docker run -it --rm python-app
   ```

2. **Run tests and generate coverage report:**
   ```bash
   ./run_tests.sh
   ```

3. **Analyze code with SonarQube:**
   - Open a browser and go to `http://localhost:9000`
   - Log in with the default credentials (`admin` / `admin`)
   - Create a new project and obtain the project key and token
   - Add the project key to `sonar-project.properties`
   - Run the following command to analyze the project:
     ```bash
     sonar-scanner -Dsonar.projectKey=PythonAppWithSonarQube -Dsonar.sources=./app -Dsonar.host.url=http://localhost:9000 -Dsonar.login=<your_token>
     ```

### License

This project is licensed under the MIT License.

### Contributing

Contributions are welcome! Please feel free to submit a pull request.

### Contact

For any questions or suggestions, please open an issue or contact the project maintainer.
