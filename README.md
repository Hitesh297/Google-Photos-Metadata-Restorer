# Google Photos Metadata Restorer

A Python script to restore metadata (EXIF, GPS, Date Taken) for Google Photos images and videos downloaded via Google Takeout. This script supports **JPG**, **PNG**, **HEIC**, **MOV**, and **MP4** file formats, restoring important metadata such as **Date Taken**, **Creation Time**, and **GPS** information from the corresponding `.json` files generated by Google Takeout.

## Features

- Restores **EXIF Date/Time**, **GPS coordinates**, and other metadata from Google Takeout JSON files.
- Supports **JPG (.jpg, .jpeg)**, **PNG (.png)**, **HEIC (.heic)**, **MOV (.mov)**, and **MP4 (.mp4)** file formats.
- Recursively processes all files within the specified parent directory and subdirectories.
- Deletes `.json` files and `_original` backup files created by `exiftool` after successful metadata restoration.

## Requirements

- **Python 3.x** installed.
- **exiftool**: Required for metadata editing. You can download it from [ExifTool Website](https://exiftool.org/install.html).

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/google-photos-metadata-restorer.git
   cd google-photos-metadata-restorer
