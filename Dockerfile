FROM python:3.8-slim

WORKDIR /app

COPY main.py .

RUN pip install fastapi uvicorn

EXPOSE 9000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--workers", "4"]