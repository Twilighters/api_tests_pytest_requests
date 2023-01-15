[![tests](https://github.com/Twilighters/api_tests_pytest_requests/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Twilighters/api_tests_pytest_requests/actions/workflows/tests.yml)
# Python api tests
This is a tutorial project that shows how to implement api tests in Python

The project uses:
1. Python
2. Requests
3. Allure for reports
4. CI (GitHub actions)


Testing application (write with Flask):

git: https://github.com/berpress/flask-restful-api

url: https://stores-tests-api.herokuapp.com

swagger: https://app.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0



### How to start
Use Docker and test this app local
```
docker run -d -p 56733:80 litovsky/flask-api-test
```

Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

or install poetry https://python-poetry.org/, then

```
poetry install
```

and add pre-commit
```
pre-commit install
```

### Run all tests

```
pytest
```

Some requests require an authorization token. Use header like
```angular2html
"Authorization": "JWT {token}"
```
