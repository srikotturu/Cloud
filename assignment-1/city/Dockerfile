FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install --no-cache-dir flask

ENV FLASK_APP=city.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0","--port=5000"]