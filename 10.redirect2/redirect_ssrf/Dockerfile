FROM python:3.11-slim

WORKDIR /app

COPY app.py ./
COPY file.txt ./

COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]