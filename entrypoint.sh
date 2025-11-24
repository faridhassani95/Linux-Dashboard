#!/bin/sh
set -e

echo "شروع collector هر 60 ثانیه..."
while true; do
    /app/collector.sh
    sleep "${COLLECTION_INTERVAL:-60}"
done &

echo "شروع داشبورد گرافیکی..."
exec python3 /app/dashboard.py