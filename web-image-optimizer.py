#!/usr/bin/python3
import os
import sys
import PIL
from PIL import Image
import zipfile
import time
import datetime

if not sys.argv[1:]:
    # Default values
    size = (1920, 1080)
    img_format = 'webp'
    img_quality = 60
else:
    try:
        # Values from comand-line arguments
        img_format = sys.argv[1]
        size = (int(sys.argv[2]), int(sys.argv[3]))
        img_quality = int(sys.argv[4])
    except Exception:
        print('Usage: web-optimizer.py format width height quality')
        sys.exit(0)

images = []  # Array for storing image paths

# Get paths to all files in the current directory and all subdirectories
for path, subdirs, files in os.walk(os.getcwd()):
    for name in files:
        # Check if the file is an image
        if name.endswith(('JPG', 'PNG', 'JPEG', 'jpg', 'png', 'jpeg')):
            images.append(os.path.join(path, name))

# Create a zip archive backup
zip = zipfile.ZipFile('backup.zip', 'w', zipfile.ZIP_DEFLATED)
for img in images:
    print('Backuping: {}'.format(img))
    try:
        zip.write(os.path.relpath(img))
    except ValueError:  # If file has timestamp before 1980, change it to 1980
        date = datetime.datetime(1980, 1, 1, 1, 1, 1)
        date = time.mktime(date.timetuple())
        os.utime(img, (date, date))
        zip.write(os.path.relpath(img))
zip.close()

# Optimize the images
for img in images:
    image = Image.open(img)
    image.thumbnail(size)

    new_path = img.split('.')
    new_path[-1] = img_format
    new_path = '.'.join(new_path)

    print('Optimizing: {}'.format(new_path))
    image.save(new_path, optimize=True, format=img_format, quality=img_quality)
    os.remove(img)