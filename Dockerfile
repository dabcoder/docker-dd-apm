FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ddtrace-run python app.py
