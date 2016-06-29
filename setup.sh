#!/usr/bin/env bash

# ----- Aptitude Installs ----- #

# Update package list.
echo '-----> Updating package list...'
sudo apt-get update

# Install Python 3.
echo '-----> Installing Python 3...'
sudo apt-get install -y python3 python3-pip python3-venv


# ----- Working Directory ----- #

WORKING_DIR=$(pwd)


# ----- Configure Virtual Environment ----- #

echo '-----> Creating Python virtual environment...'

# Create virtual environment.
pyvenv around-the-house-env

echo '-----> Installing Python dependencies...'

# Install dependencies.
$WORKING_DIR/around-the-house-env/bin/pip install -r requirements.txt


# ---- Configure Systemd ----- #

echo '-----> Configuring Systemd...'

# Replace paths to working directory.
WORKING_DIR_ESC="${WORKING_DIR//\//\\/}"
sed "s/\/home\/pi\/around-the-house/$WORKING_DIR_ESC/g" around-the-house.service > /etc/systemd/system/around-the-house.service

# Enable and start the service.
sudo systemctl enable /etc/systemd/system/around-the-house.service
sudo systemctl start around-the-house.service
