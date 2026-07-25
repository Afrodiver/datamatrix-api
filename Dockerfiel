FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y libdmtx0b && \
    pip install flask pylibdmtx pillow && \
    apt-get clean

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
