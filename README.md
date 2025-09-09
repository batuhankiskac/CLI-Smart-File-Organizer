# Command-Line Smart File Organizer

## 1. Project Overview

The **Smart File Organizer** is a command-line utility designed to bring order to chaotic directories, such as a user's Downloads folder. The script automatically scans a specified directory, identifies files based on their extensions, and moves them into categorized subdirectories.

This project serves as a practical exercise for learning and applying core Python concepts, particularly in file system manipulation and command-line interface (CLI) creation. The final product will be a simple yet powerful tool that can be used in daily digital life.

---

## 2. Core Features & Requirements

### FR-1: Target Directory Specification
- The user must be able to specify the directory to organize via a command-line argument.
- If the specified directory does not exist, the program should display an informative error message and exit gracefully.

### FR-2: File Scanning and Identification
- The script must read all entries within the root of the specified target directory.
- It must differentiate between files and subdirectories.
- **Scope:** Only files directly inside the target directory will be processed. Existing subdirectories and their files are ignored.

### FR-3: File Categorization Logic
- Files are categorized based on a predefined mapping of file extensions to categories.
- This mapping is initially defined within the script using a Python dictionary.

#### Initial Categories:
| Category    | Extensions                                                            |
|-------------|----------------------------------------------------------------------|
| Images      | .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp                          |
| Documents   | .pdf, .docx, .doc, .xlsx, .xls, .pptx, .ppt, .txt, .rtf, .csv        |
| Videos      | .mp4, .mov, .avi, .mkv, .wmv, .flv                                   |
| Audio       | .mp3, .wav, .aac, .flac, .ogg                                        |
| Archives    | .zip, .rar, .7z, .tar, .gz                                           |
| Scripts     | .py, .js, .html, .css, .sh, .bat                                     |
| Executables | .exe, .msi, .dmg                                                     |

- Files with extensions not found in the mapping should be left in their original location.

### FR-4: Automated Directory Creation
- For each category that contains at least one file, the script must create a corresponding subdirectory within the target folder (e.g., `.../Downloads/Images`).
- The script must check if a category directory already exists before attempting to create it. If it exists, it should proceed without error.

### FR-5: File Movement
- Once the appropriate category folder exists, the script will move each file from the target directory into its new destination.
- The script should handle potential errors during the move operation (e.g., permission issues) and report them to the user.

### FR-6: Console Feedback
- The script must provide clear, real-time feedback to the user in the console.
- Output should indicate:
  - Which directory is being scanned
  - Which files are being moved and to where
  - Which files are being skipped (uncategorized)
- A final message should be displayed upon completion.

---

## 3. Technical Requirements

- **Language:** Python 3.x
- **Execution Environment:** A standard terminal or command prompt.
- **Standard Libraries Only:**  
  - `os`: For essential OS interactions (`os.listdir()`, `os.path.join()`, `os.path.isdir()`, etc.)
  - `shutil`: For high-level file operations (`shutil.move()`)
  - `argparse`: For creating a professional and user-friendly CLI to accept the target folder path
- **Development Practice:**  
  - It is highly recommended to use a virtual environment (`venv`) to isolate the project.

---

## 4. Future Enhancements (Stretch Goals)

Once the core functionality is complete, consider extending the project with the following features:

- **Configuration from File:** Move the `FILE_CATEGORIES` dictionary to an external configuration file (e.g., `config.json`) that the script reads on startup.
- **Recursive Mode:** Add an optional flag (e.g., `--recursive`) to organize files in all subdirectories of the target folder.
- **Dry Run Mode:** Implement a `--dry-run` flag that prints what actions would be taken without actually moving any files.
- **Logging:** Log all operations to a file (e.g., `organizer.log`) for later review, including timestamps, files moved, and any errors encountered.

---
