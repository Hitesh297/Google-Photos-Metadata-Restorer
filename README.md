
# Google Photos Metadata Restorer

A Python script to restore metadata (EXIF, GPS, Date Taken) for Google Photos images and videos downloaded via Google Takeout. This script supports **JPG**, **PNG**, **HEIC**, **MOV**, and **MP4** file formats, restoring important metadata such as **Date Taken**, **Creation Time**, and **GPS** information from the corresponding `.json` files generated by Google Takeout.

## Important Note
> **⚠️ Important:** Please ensure you have backed up your original files before running this script, as it performs delete operations on the `_original` files and `.json` files after processing.

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
   git clone https://github.com/Hitesh297/google-photos-metadata-restorer.git
   cd google-photos-metadata-restorer
   ```

2. **Install exiftool**:

   Download and install `exiftool` from the [official website](https://exiftool.org/install.html). For Windows, ensure `exiftool` is added to your system's PATH for global usage.

## Usage

1. Place the **Python script** (`add_metadata.py`) inside the **parent folder** that contains your Google Photos backups (images/videos) along with their corresponding `.json` files.

2. Run the script:

   ```bash
   python add_metadata.py
   ```

3. The script will:
   - Traverse the **parent directory** and its subdirectories for supported file formats (`.jpg`, `.png`, `.heic`, `.mov`, `.mp4`).
   - Match each file with its corresponding JSON metadata file (e.g., `image.jpg` -> `image.jpg.json`).
   - Apply the metadata from the JSON file to the image or video using `exiftool`.
   - Delete the `_original` backup file and the `.json` file after successful processing.

### Example Directory Structure

If your folder looks like this:

```
/parent_folder/
    /subfolder1/
        photo1.jpg
        photo1.jpg.json
        video1.mp4
        video1.mp4.json
    /subfolder2/
        photo2.heic
        photo2.heic.json
```

Running the script will process `photo1.jpg`, `video1.mp4`, and `photo2.heic`, apply metadata from their respective JSON files, and then delete the `_original` files and `.json` files after processing.

## Supported Metadata

The script restores the following metadata:

- **Date Taken** (`DateTimeOriginal`, `CreateDate`, `ModifyDate`)
- **GPS Data** (Latitude, Longitude, Altitude)
- **File Creation and Modification Time**

## Troubleshooting

If you encounter issues while running the script, make sure:

1. **ExifTool** is correctly installed and accessible via the command line.
2. You are running the script in the correct directory (the parent folder of your Google Takeout files).
3. The `.json` files are named correctly (e.g., `image.jpg` should have `image.jpg.json`).

## Keywords

- Restore Google Photos metadata
- Recover EXIF data from Google Takeout
- Bulk update EXIF metadata
- Add metadata to JPG, PNG, HEIC, MOV, MP4
- Google Photos JSON to EXIF script
- GPS metadata restoration
- Python script for Google Photos backup
- Restore original photo date Google Photos
- Google Takeout metadata repair

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
