FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    iproute2 jq curl procps iputils-ping net-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN chmod +x collector.sh entrypoint.sh
RUN pip install --no-cache-dir flask

VOLUME ["/app/output"]
ENTRYPOINT ["./entrypoint.sh"]