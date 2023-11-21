# Project Indian

`lsusb`

`pip install picamera`


`nano camera.py`

Write this into it
```python
import time
import picamera

def take_picture(output_file):
    with picamera.PiCamera() as camera:
        time.sleep(2)
        
        camera.capture(output_file)

output_file = "image.jpg"

take_picture(output_file)

print(f"Picture taken and saved as {output_file}")
```

`python take_picture.py`

Eller
`sudo apt-get install fswebcam`

`nano fs.py`

```python
import subprocess

def take_picture(output_file):
    subprocess.run(["fswebcam", "--no-banner", "-r", "1080x720", "--jpeg", "85", "-D", "1", output_file])

output_file = "image.jpg"

take_picture(output_file)

print(f"Picture taken and saved as {output_file}")
```

`python fs.py`


