# Web image optimizer
Simple Python script for converting JPG or PNG images to WEBP and making them smaller with lossy compression.

## About
This simple script looks for every JPG, PNG, or JPEG in every directory or subdirectory, makes a backup in one zip archive, and by default converts it to WEBP, scales it to Full HD (1920x1080), and makes the quality 60. This behavior can be changed by specifiing size, format, and quality in command line arguments.

## Usage
`web-image-optimizer.py format width height quality`

This script is available under GNU GPL v3 license. See LICENSE.md for details.
Copyright (c) 2021 Pavel40
