#!/bin/bash

# Project Indian

# List connected USB devices
echo "List of connected USB devices:"
lsusb
echo

# Install picamera
pip install picamera

# Create camera.py script
cat <<EOL > camera.py
import time
import picamera

def take_picture(output_file):
    with picamera.PiCamera() as camera:
        time.sleep(2)
        camera.capture(output_file)

output_file = "image.jpg"

take_picture(output_file)

print(f"Picture taken and saved as {output_file}")
EOL

echo "camera.py created successfully."

# Run camera.py
echo "Running camera.py..."
python camera.py
echo

# Check if fswebcam is installed
if ! command -v fswebcam &> /dev/null; then
    echo "Installing fswebcam..."
    sudo apt-get install -y fswebcam
    echo "fswebcam installed successfully."
fi

# Create fs.py script
cat <<EOL > fs.py
import subprocess

def take_picture(output_file):
    subprocess.run(["fswebcam", "--no-banner", "-r", "1080x720", "--jpeg", "85", "-D", "1", output_file])

output_file = "image.jpg"

take_picture(output_file)

print(f"Picture taken and saved as {output_file}")
EOL

echo "fs.py created successfully."

# Run fs.py
echo "Running fs.py..."
python fs.py

