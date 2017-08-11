FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /aggregator
WORKDIR /aggregator
ADD requirements.txt /aggregator/
RUN pip install -r requirements.txt
ADD . /aggregator/
RUN python manage.py loaddata city