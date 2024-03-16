FROM python:3.8-slim

WORKDIR /app

COPY main.py .

RUN pip install fastapi uvicorn

CMD ["python", "main.py"]