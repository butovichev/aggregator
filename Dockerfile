FROM python:3
ENV PYTHONUNBUFFERED 1
RUN git clone https://github.com/butovichev/aggregator
WORKDIR /aggregator
RUN pip install -r requirements.txt
