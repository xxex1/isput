FROM alpine

WORKDIR /app

COPY . .

RUN "apt install -r requirements.txt"

CMD ["python", "app.py"]