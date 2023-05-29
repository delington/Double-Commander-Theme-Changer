import os
from tkinter.filedialog import askdirectory

DB_COMMANDER_PROPERTY_PATH = "doublecmd.xml"

def find_db_commander_property_file():

    # Ask the user to select a directory
    selected_directory = askdirectory(title="Select Directory")

    if selected_directory:
        # Iterate over all files in the selected directory
        for root_dir, dirs, files in os.walk(selected_directory):
            # Check if "doublecmd.xml" exists in the files list
            if DB_COMMANDER_PROPERTY_PATH in files:
                file_path = os.path.join(root_dir, DB_COMMANDER_PROPERTY_PATH)
                print(f"✔️  Found {DB_COMMANDER_PROPERTY_PATH} at:", file_path)
                return file_path  # Stop searching after finding the first occurrence
        else:
            print(f"{DB_COMMANDER_PROPERTY_PATH} not found in the selected directory.")
    else:
        print("No directory selected.")
