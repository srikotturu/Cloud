FROM python:3.8-alpine

WORKDIR /app

COPY weather.py .

RUN pip install --no-cache-dir flask

ENV FLASK_APP=weather.py

EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0","--port=5001"]