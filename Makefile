setup2:
	mkvirtualenv -a $(pwd) --python=$(python) $(NAME)

setup3:
	mkvirtualenv -a $(pwd) --python=$(python3) $(NAME)

init:
	pipenv install --dev
	pipenv run pip install -e .

mm:
	cd demo && python manage.py makemigrations hooked

test:
	pipenv run py.test --ds=tests.settings --capture=no --cov-report term-missing --cov-report html --cov=hooked tests
	pipenv run flake8 . --exclude demo,tests --ignore W293,W291

