mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

gen_key:
	openssl rand -base64 32

install:
	pip install -r requirements.txt

req:
	pip freeze > requirements.txt

admin:
	./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(email='admin@gmail.com', full_name='Admin adminov', is_active=True, password='1', status='admin')"

export_req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

celery:
	celery -A root worker -l info &
	celery -A root flower --port=5555 --address=0.0.0.0