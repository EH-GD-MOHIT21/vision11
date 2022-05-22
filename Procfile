web: daphne vision11.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A taskSchedularApp.celery worker -l info -c 2 -P eventlet
celerybeat: celery -A taskSchedularApp beat -l info
celeryworker: celery -A taskSchedularApp.celery worker & celery -A taskSchedularApp beat -l info -P eventlet & wait -n