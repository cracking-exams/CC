FROM python:3.9-slim
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 8999

CMD ["python", "app.py"]
