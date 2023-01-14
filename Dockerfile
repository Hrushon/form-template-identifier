FROM python:3.8.9-slim

WORKDIR /app

COPY . .

RUN pip3 install -r ./requirements.txt --no-cache-dir

CMD ["python3", "main.py"]