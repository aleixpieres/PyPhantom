#!/bin/bash

# Update and upgrade the system
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Python3 and pip3 if not already installed
sudo apt-get install -y python3 python3-pip

# Install discord.py
python3 -m pip install -U discord.py

# Install ollama Python package
python3 -m pip install -U ollama

# Install Ollama server
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama server
ollama serve &

# Run Ollama with llama3
ollama run llama3

# Notify user of completion
echo "All dependencies have been installed and Ollama server is running."
