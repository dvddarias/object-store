FROM python:3.8.2-buster

RUN mkdir -p /eve

WORKDIR /eve

RUN pip install --no-cache-dir eve greenlet gevent gunicorn uwsgi

EXPOSE 5000
CMD ["python", "server.py"]
