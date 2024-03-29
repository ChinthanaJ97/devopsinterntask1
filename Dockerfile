FROM python:3.9-alpine

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["python", "server.py"]