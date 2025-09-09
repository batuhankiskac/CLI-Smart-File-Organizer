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
        print(f"Error: Directory '{target_folder}' could not be found")
        return

    for filename in entries:
        file_path = os.path.join(target_folder, filename)
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()

        moved = False
        for category, extensions in FILE_CATEGORIES.items():

            if file_extension in extensions:
                category_path = os.path.join(target_folder, category)
                os.makedirs(category_path, exist_ok=True)

                destination_path = os.path.join(category_path, filename)
                try:
                    shutil.move(file_path, destination_path)
                    print(f"Moved: {filename} -> {category}")
                    moved = True
                    break
                except Exception as e:
                    print(f"Error: Could not move '{filename}': {e}")
                    moved = True
                    break

        if not moved:
            print(f"Skipped (Uncategorized): {filename}")
    print("\nOrganization complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A smart tool to organize files in a directory into categorized subfolders."
    )

    parser.add_argument(
        "target_folder",
        type=str,
        help="The path to the folder you want to organize."
    )

    args = parser.parse_args()
    organize_folder(args.target_folder)