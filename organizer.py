import os
import shutil
import argparse
import json

def load_categories(config_path='config.json'):
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"ERROR: Configuration file '{config_path}' is not a valid JSON file.")
        return None

def organize_folder(target_folder, categories, dry_run = False):
    if dry_run:
        print("--- DRY RUN MODE: No files will be moved. ---\n")

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
        for category, extensions in categories.items():

            if file_extension in extensions:
                if dry_run:
                    print(f"[DRY RUN] Would move '{filename}' to '{category}/'")
                else:
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

    file_categories = load_categories()
    if not file_categories:
        exit()

    parser = argparse.ArgumentParser(
        description="A smart tool to organize files in a directory into categorized subfolders."
    )

    parser.add_argument(
        "target_folder",
        type=str,
        help="The path to the folder you want to organize."
    )

    parser.add_argument(
        "--dry-run",
        action='store_true',
        help="Simulate the organization process without moving any files."
    )

    args = parser.parse_args()
    organize_folder(args.target_folder, file_categories, args.dry_run)