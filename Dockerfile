FROM python:3.8-slim

WORKDIR /app

COPY main.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

CMD ["python", "main.py"]