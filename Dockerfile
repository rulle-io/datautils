FROM python:3.8.7-slim-buster
# LABEL 
WORKDIR /
# RUN pip install -r requirements.txt
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

COPY datautils.py .
ENTRYPOINT ["/run.sh"]
