web: gunicorn personal_portfolio.wsgi --log-file - --log-level debug
python3 manage.py collectstatic --noinput
manage.py migrate
