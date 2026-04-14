#!/bin/bash
set -e

echo "=== Deploying ==="

# You are already inside the latest repo code
pwd
ls -la

echo "Running script..."
python3 app.py   # change if your file name is different

echo "=== Done ==="