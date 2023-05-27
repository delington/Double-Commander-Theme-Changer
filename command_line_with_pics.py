import os
import platform
import read_manager

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

        theme_input = int(input("Select a theme option (1-4): "))
        if theme_input == 0:
            print("Exiting...")
            break

        for i in range(len(theme_list)):
            if theme_input - 1 == i:
                theme_option = theme_list[i]
                print(theme_list[i]["name"], " selected.")
                break

            print("Invalid theme option.")
            continue

        show_picture_option = input("Show picture? (y/n): ")
        if show_picture_option.lower() == "y":
            show_picture(theme_option["picture_path"])

main()
