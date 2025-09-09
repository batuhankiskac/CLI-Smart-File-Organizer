import os
import shutil
import argparse

FILE_CATEGORIES = {
    "Images" : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents" : [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".rtf", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat"],
    "Executables": [".exe", ".msi", ".dmg"]
}

def organize_folder(target_folder):
    print(f"Scanning directory: {target_folder}\n")

    try:
        entries = os.listdir(target_folder)
    except FileNotFoundError:
        print(f"Error: Path '{target_folder}' could not be found")
        return

    for filename in entries:
        file_path = os.path.join(target_folder, filename)
        if os.path.isdir(file_path):
            continue