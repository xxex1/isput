FROM alpine

WORKDIR /app

COPY . .
RUN apt install python3
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]