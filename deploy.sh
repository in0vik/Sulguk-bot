#!/bin/bash

# Exit on error
set -e

# Load environment variables
source .env

# Install dependencies
pip install -r requirements.txt

# Create a systemd service file for the bot
sudo tee /etc/systemd/system/telegram-bot.service << EOF
[Unit]
Description=Telegram HTML Bot
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)
Environment=PATH=$(pwd)/venv/bin:$PATH
ExecStart=$(pwd)/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd
sudo systemctl daemon-reload

# Stop any existing bot instance
sudo systemctl stop telegram-bot || true

# Start the bot service
sudo systemctl start telegram-bot

# Enable the service to start on boot
sudo systemctl enable telegram-bot

# Show the status
sudo systemctl status telegram-bot 