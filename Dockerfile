FROM python:3.9

WORKDIR /app

COPY practice/ .

CMD ["python", "app.py"]