# install requirements
- pip install -r requirements/dev.txt

# Run tests
- ./manage.py test -- --integration

# Coverage
- pytest -svv --cov=. --cov-report=term-missing

# To run app
- FLASK_CONFIG="development" flask run
