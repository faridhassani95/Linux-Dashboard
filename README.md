# Linux Security & Performance Dashboard

![Demo GIF](./demo.gif)

A lightweight, containerized solution for real-time monitoring of Linux system performance and security metrics. This project leverages low-level Bash scripting for efficient data collection, a Flask backend for API delivery, and a modern frontend stack utilizing HTMX and Tailwind CSS for a responsive user experience without the overhead of heavy JavaScript frameworks.

## Project Overview

This dashboard provides a unified view of critical system health indicators. It is designed to be minimally invasive, running as a Docker container that mounts necessary system directories in read-only mode to gather metrics directly from the kernel.

**Key Capabilities:**

- **Real-Time Monitoring:** Updates system metrics every 5 seconds via HTMX polling.
- **Resource Efficiency:** Data collection handled by lightweight Bash scripts, web server handles presentation.
- **Security Visibility:** Tracks open ports and monitors SSH connection attempts (simulated logic included for demonstration).
- **Visual Analytics:** Live CPU and memory usage trends rendered using Chart.js.

## Technical Architecture

1. **Data Collector (`collector.sh`)**: A background Bash process parsing `/proc/stat`, `/proc/loadavg`, and other Linux utilities to generate JSON reports every 60 seconds.
2. **API Backend (`dashboard.py`)**: Flask application serving frontend and `/data` endpoint reading latest JSON report.
3. **Frontend Orchestration**: HTMX requests `/data` endpoint periodically; DOM updates efficiently, Chart.js renders visualization.
4. **Entrypoint (`entrypoint.sh`)**: Runs collector loop and Flask server concurrently.

## Technology Stack

- **Containerization:** Docker, Docker Compose  
- **Backend:** Python 3.11 (Flask), Bash scripting  
- **Frontend:** HTML5, Tailwind CSS, HTMX, Chart.js  
- **System Tools:** `iproute2`, `procps`, `net-tools`

## Installation and Deployment

### Prerequisites

- Docker Engine  
- Docker Compose

### Setup Instructions

```bash
git clone https://github.com/faridhassani95/Linux-Dashboard.git
cd Linux-Dashboard
cp config.env.example config.env
docker-compose up -d
