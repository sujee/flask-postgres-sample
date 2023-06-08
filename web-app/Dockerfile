#FROM python:3-slim
# FROM python:3
FROM python:3.11.1

WORKDIR /app


RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# CMD ["python" , "app.py"]

# CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "app:app"]
