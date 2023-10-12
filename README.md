# install requirements
- pip install -r requirements/dev.txt

# Run unit tests
- pytest -svv

# Run all tests(including integration)
- pytest -svv --integration

# Coverage
- pytest -svv --cov=. --cov-report=term-missing

# To run app
- FLASK_CONFIG="development" flask run
