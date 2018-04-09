setup2:
	mkvirtualenv -a $(pwd) --python=$(which python2) $(NAME)

setup3:
	mkvirtualenv -a $(pwd) --python=$(which python3) $(NAME)

init:
	pipenv install --dev
	pipenv run pip install -e .

rs:
	./demo/manage.py runserver

mm:
	cd demo && python manage.py makemigrations hooked

mmd:
	rm -rf hooked/migrations
	
mdb:
	cd demo && python manage.py migrate hooked

rdb:
	cd demo && python manage.py migrate hooked zero

clean:
	find . -name '*.pyc' -delete

test:
	pipenv run py.test --ds=tests.settings --capture=no --cov-report term-missing --cov-report html --cov=hooked tests
	pipenv run flake8 . --exclude demo,tests,migrations --ignore W293,W291

