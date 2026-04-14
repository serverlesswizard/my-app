#!/bin/bash
set -e   # stop on any error

APP_DIR="/opt/myapp"        # change to your app folder
SERVICE_NAME="myapp"        # change to your systemd service name

echo "=== Deploying ==="

# Go to app folder and pull latest code
cd $APP_DIR
git pull origin main

# Install/update dependencies
pip install -r requirements.txt

# --- Choose ONE of these depending on how you run your app ---

# OPTION A: Direct Python (using systemd)
sudo systemctl restart $SERVICE_NAME
echo "Service restarted"

# OPTION B: Docker
# docker compose down
# docker compose up -d --build
# echo "Docker restarted"

echo "=== Deploy done ==="
