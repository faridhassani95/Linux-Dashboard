#!/usr/bin/env python3
import os, json, glob
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="/app/templates")
OUTPUT_DIR = "/app/output"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    files = sorted(glob.glob("/app/output/report-*.json"), key=os.path.getmtime, reverse=True)
    if not files:
        return jsonify({"hostname": "unknown", "uptime": "unknown", "load_average": "0.0 0.0 0.0", "data": {"cpu": 0, "mem": 0, "failed_ssh": 0, "cpu_temp": "N/A", "open_ports": 0}})
    with open(files[0]) as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
