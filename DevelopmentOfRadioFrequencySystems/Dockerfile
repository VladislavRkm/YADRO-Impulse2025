FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip
RUN pip install requests

WORKDIR /app

COPY http_requests_processing.py /app/http_requests_processing.py

CMD ["python3", "/app/http_requests_processing.py"]

