FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask

ENV FLASK_APP=city.py

CMD ["flask", "run", "--host=0.0.0.0"]