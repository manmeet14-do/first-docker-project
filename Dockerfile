FROM python:3.11-slim

WORKDIR /app

pip install -r requirements.txt

COPY app.py .

CMD [ "python","app.py" ]
