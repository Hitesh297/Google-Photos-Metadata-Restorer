import os
import json
import subprocess
from datetime import datetime

# A dictionary to handle month abbreviations, including "Sept"
MONTHS_MAPPING = {
    "Jan": "Jan", "Feb": "Feb", "Mar": "Mar", "Apr": "Apr",
    "May": "May", "Jun": "Jun", "Jul": "Jul", "Aug": "Aug",
    "Sep": "Sep", "Sept": "Sep", "Oct": "Oct", "Nov": "Nov", "Dec": "Dec"
}

def reformat_date(date_str):
    """Convert a date string like '22 Sept 2019, 05:16:58 UTC' to '2019:09:22 05:16:58'."""
    try:
        # Split the date string to substitute the month abbreviation if needed
        parts = date_str.split()
        parts[1] = MONTHS_MAPPING.get(parts[1], parts[1])  # Map 'Sept' to 'Sep'
        standardized_date_str = ' '.join(parts)
        
        # Parse the date string and convert it to the desired format
        dt = datetime.strptime(standardized_date_str, '%d %b %Y, %H:%M:%S UTC')
        return dt.strftime('%Y:%m:%d %H:%M:%S')
    except ValueError as e:
        print(f"Date format error ({date_str}): {e}")
        return None

def add_metadata(file_path, json_path):
    # Load metadata from the JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # Extract the relevant metadata (photo taken time and geoData)
    photo_taken_time_str = metadata.get('photoTakenTime', {}).get('formatted')
    creation_time_str = metadata.get('creationTime', {}).get('formatted')
    geo_data = metadata.get('geoData', {})

    # Reformat the date string to a format that exiftool understands
    if photo_taken_time_str:
        photo_taken_time = reformat_date(photo_taken_time_str)
        if photo_taken_time:
            # Use exiftool to write the metadata back to the image/video (photo taken time)
            subprocess.run([
                'exiftool',
                f'-DateTimeOriginal={photo_taken_time}', 
                f'-CreateDate={photo_taken_time}', 
                f'-ModifyDate={photo_taken_time}',
                file_path
            ], shell=True)

            print(f"Metadata added to {file_path} - Photo Taken Time: {photo_taken_time}")
        else:
            print(f"Invalid photo taken time for {file_path}")

    # Optional: Add geoData to the image if it's available and not default (0.0 values)
    if geo_data and geo_data['latitude'] != 0.0 and geo_data['longitude'] != 0.0:
        subprocess.run([
            'exiftool',
            f'-GPSLatitude={geo_data["latitude"]}',
            f'-GPSLongitude={geo_data["longitude"]}',
            f'-GPSAltitude={geo_data["altitude"]}',
            file_path
        ], shell=True)
        print(f"GeoData added to {file_path} - Latitude: {geo_data['latitude']}, Longitude: {geo_data['longitude']}")

    # Delete the _original file created by exiftool (backup file)
    original_file_path = f"{file_path}_original"
    if os.path.exists(original_file_path):
        os.remove(original_file_path)
        print(f"Deleted backup file: {original_file_path}")

    # Delete the JSON file after processing
    if os.path.exists(json_path):
        os.remove(json_path)
        print(f"Deleted JSON file: {json_path}")

def process_images_in_directory(directory):
    """Process all image files in the directory and its subdirectories."""
    # Walk through the directory tree
    for root, _, files in os.walk(directory):
        for filename in files:
            # Handle .jpg, .png, .mov, .heic, and .mp4 files
            if filename.lower().endswith((".jpg", ".png", ".mov", ".heic", ".mp4")):
                file_path = os.path.join(root, filename)

                # Adjust the .json filename for .jpg, .png, .mov, .heic, or .mp4
                json_path = file_path + ".json"  # Looks for .JPG.json, .PNG.json, .MOV.json, .HEIC.json, or .MP4.json

                # Check if JSON metadata exists for the image/video
                if os.path.exists(json_path):
                    add_metadata(file_path, json_path)
                else:
                    print(f"No JSON metadata found for {filename}")

# Process all images in the current directory and its subdirectories
if __name__ == "__main__":
    parent_directory = os.getcwd()  # Get the current working directory
    process_images_in_directory(parent_directory)
