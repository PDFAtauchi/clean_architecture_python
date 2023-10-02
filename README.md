# install requirements
- pip install -r requirements/dev.txt

# Run tests
- pytest -svv

# Coverage
- pytest -svv --cov=. --cov-report=term-missing
