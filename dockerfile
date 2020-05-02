FROM python:3-alpine

RUN mkdir -p /eve

WORKDIR /eve

RUN pip install --no-cache-dir eve greenlet gunicorn uwsgi

EXPOSE 5000
CMD ["python", "server.py"]
