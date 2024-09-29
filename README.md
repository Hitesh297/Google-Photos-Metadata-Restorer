
# Google Photos Metadata Restorer

**Google Photos Metadata Restorer** is a Python-based application that restores missing metadata (EXIF data) for your photos and videos from Google Takeout backups. The tool automatically reads metadata from accompanying JSON files (from Google Takeout) and updates your image/video files with the correct metadata, including creation dates, GPS data, and more. The tool also cleans up unnecessary backup files after the process.

## Features

- **Supports multiple formats**: Works with `.jpg`, `.jpeg`, `.png`, `.heic`, `.mov`, and `.mp4` files.
- **Automatic metadata restoration**: Restores EXIF data such as Date Taken, GPS Data, and file creation/modification times.
- **Deletes redundant files**: Cleans up `_original` and `.json` files after processing.
- **User-friendly GUI**: Provides an easy-to-use graphical interface with a "Browse Folder" button to select the folder.
- **Multithreaded processing**: Ensures the UI remains responsive while processing files in the background.
  
## Requirements

- Python 3.x
- `exiftool` (Included in the package)
  
## Important

⚠️ **Important: Make sure to back up your files before running this tool!**  
This tool performs **delete operations** on files after processing. Ensure you have backups to avoid accidental data loss.

## Installation

1. **Download the Repository**: 
   Clone or download the repository from GitHub:
   ```bash
   git clone https://github.com/your-username/google-photos-metadata-restorer.git
   ```
   
2. **Install Dependencies**:
   Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install ExifTool**:
   - ExifTool is included in this package, so there's no need for a separate installation.
   - Ensure the `exiftool.exe` and its required files are in the same directory as the script.

## Usage

1. **Place Files**: Place your Google Photos backup files (images/videos) and their corresponding `.json` metadata files inside a parent folder.
2. **Run the Script**:
   - Open the Python script `add_metadata.py` and run it:
   ```bash
   python add_metadata.py
   ```

3. **Using the GUI**:
   - A graphical interface will pop up.
   - Click on the "Browse Folder" button to select the folder that contains your Google Takeout backup files.
   - The script will start processing, and a progress symbol will display while files are being processed.
   - Once processing is complete, a notification will appear with the total number of files processed.

### Example Directory Structure

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

When the script is run, it will process the `photo1.jpg`, `video1.mp4`, and `photo2.heic` files, applying metadata from their respective JSON files. After processing, it will delete the unnecessary `_original` and `.json` files.

## Supported Metadata

The script restores the following metadata:

- **Date Taken** (`DateTimeOriginal`, `CreateDate`, `ModifyDate`)
- **GPS Data** (Latitude, Longitude, Altitude)
- **File Creation and Modification Time**

## Troubleshooting

- **ExifTool not working?** Ensure `exiftool.exe` is included in the folder and accessible.
- **Script not running?** Ensure Python 3.x is installed, and all dependencies are properly set up.
- **No metadata applied?** Ensure the `.json` files are named correctly (e.g., `image.jpg` should have `image.jpg.json`).

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

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
