FROM alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache python3 py3-pip build-base python3-dev
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

CMD ["python", "app.py"]