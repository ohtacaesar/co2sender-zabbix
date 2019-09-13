FROM python:3.7

WORKDIR /app

ADD setup.py  /app/
ADD co2sender /app/co2sender

RUN pip install . && rm -rf *

CMD ["co2sender"]

