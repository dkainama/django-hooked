init:
	pipenv install --dev
	pipenv run pip install -e .

test:
	pipenv run py.test --ds=tests.settings --capture=no --cov-report term-missing --cov-report html --cov=hooked tests
	pipenv run flake8 . --exclude demo

