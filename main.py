import os
import platform
import read_manager
import xml_manager

INPUT_THEME_JSON = "themes.json"

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

def main():
    theme_list = read_manager.read_themes_as_list(INPUT_THEME_JSON)

    while True:
        print("Theme Options:")
        print("0. Exit")

        for i, theme in enumerate(theme_list, start=1):
            print(f"{i}. {theme['name']}")

        theme_size = len(theme_list)
        print(f"Select a theme option (1-{theme_size}): ")
        theme_input = int(input())

        if theme_input == 0:
            print("Exiting...")
            break

        for i in range(theme_size):
            if theme_input - 1 == i:
                theme_option = theme_list[i]
                print(theme_list[i]["name"], "selected.")
                break

            print("Invalid theme option.")
            continue
        
        while True:
            print("0. Back to main menu")
            print("1. Apply theme")
            print("2. Show picture")
            apply_input = int(input())

            if (apply_input == 0):
                print("Back to main menu.")
                break

            if (apply_input == 1):
                xml_manager.apply_changes(theme_option["file_path"])
                print("Theme applied.")
                continue

            if (apply_input == 2):
                print("Showing picture...")
                show_picture(theme_option["picture_path"])
                continue

main()
