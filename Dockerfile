FROM python:3.6.9-alpine3.10
RUN apk add --no-cache curl

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /app

ENTRYPOINT ["python", "server.py"]
