FROM python:3.8-slim

WORKDIR /app

COPY main.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--workers", "4"]]