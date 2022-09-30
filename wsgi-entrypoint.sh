python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
