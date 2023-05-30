import os
import platform
import service.read_manager as read_manager
import service.xml_manager as xml_manager
import service.folder_selector_manager as folder_selector_manager
from tkinter import Tk

INPUT_THEME_JSON = "themes.json"
SEPARATOR_LINE = "----------------------------------------------"

def show_picture(picture_path):
    
    if picture_path is not None:
        system = platform.system()
        if system == "Darwin":  # macOS
            os.system(f"open {picture_path}")
        elif system == "Windows":
            os.system(f"start {picture_path}")
        elif system == "Linux":
            os.system(f"xdg-open {picture_path}")
        else:
            print(f"Unsupported operating system: {system}")
    else:
        print("No picture found for the selected theme.")

def get_input_folder_location():
    input_folder_location = folder_selector_manager.find_db_commander_property_file()

    while True:
        if os.path.isfile(input_folder_location):
            print("✔️  Folder location is valid.")
            return input_folder_location
        else:
            print("Invalid input folder location.")

def create_root_tinkter():
    root = Tk()
    root.withdraw()  # Hide the root window

def main():
    last_applied_theme = ""
    create_root_tinkter()
    theme_list = read_manager.read_themes_as_list(INPUT_THEME_JSON)

    print(SEPARATOR_LINE)
    print("⚠️  If you've never opened Double Commander before, please do so, and close it.\n(It creates doublecmd.xml which is essential!)")
    print(SEPARATOR_LINE)
    print("Please select Double Commander installation location.")
    print("0. Exit")
    print("1. OK")

    if (input() == "0"):
        print("Exiting...")
        return

    db_folder_location = get_input_folder_location()

    while True:
        print(SEPARATOR_LINE)
        print("Theme Options:")
        print("0. Exit")

        for i, theme in enumerate(theme_list, start=1):
            list_item_name = f"{i}. {theme['name']}"
            
            if theme["name"] == last_applied_theme:
                list_item_name += "⭐*"
            print(list_item_name)

        theme_size = len(theme_list)
        print(SEPARATOR_LINE)
        print(f"Select a theme option (1-{theme_size}): ")
        theme_input = int(input())

        if theme_input == 0:
            print("Exiting...")
            break

        for i in range(theme_size):
            if theme_input - 1 == i:
                theme_option = theme_list[i]
                print("✔️ *", theme_list[i]["name"], "selected.")
                break
        
        while True:
            print(SEPARATOR_LINE)
            print("0. Back to main menu")
            print("1. Apply theme")
            print("2. Show picture")
            apply_input = int(input())

            if (apply_input == 0):
                print("Back to main menu.")
                break

            if (apply_input == 1):
                xml_manager.apply_changes(db_folder_location, theme_option["file_path"])
                print(SEPARATOR_LINE)
                print(f"*** {theme_option['name']} applied. ***")
                last_applied_theme = theme_option["name"]
                break

            if (apply_input == 2):
                print("Showing picture...")
                show_picture(theme_option["picture_path"])
                continue

main()
