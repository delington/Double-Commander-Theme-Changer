import os
import platform
import service.read_manager as read_manager
import service.xml_manager as xml_manager
import service.folder_selector_manager as folder_selector_manager
from tkinter import Tk, Button, Label, Listbox, Scrollbar, messagebox

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

def apply_theme(theme_option, db_folder_location, listbox):
    xml_manager.apply_changes(db_folder_location, theme_option["file_path"])
    messagebox.showinfo("Theme Applied", f"{theme_option['name']} applied successfully.")

def main():
    def create_root_tkinter():
        root = Tk()
        root.withdraw()  # Hide the root window

    create_root_tkinter()
    last_applied_theme = ""
    theme_list = read_manager.read_themes_as_list(INPUT_THEME_JSON)

    root = Tk()
    root.title("Double Commander Theme Selector")

    def get_input_folder_location():
        input_folder_location = folder_selector_manager.find_db_commander_property_file()
        while True:
            if os.path.isfile(input_folder_location):
                return input_folder_location
            else:
                messagebox.showerror("Invalid Input Folder", "Invalid input folder location. Please select again.")

    def on_quit():
        root.quit()

    def on_theme_select():
        selected_index = themes_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("No Theme Selected", "Please select a theme from the list.")
            return

        selected_theme = theme_list[selected_index[0]]
        show_picture(selected_theme["picture_path"])

    def on_theme_apply():
        selected_index = themes_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("No Theme Selected", "Please select a theme from the list.")
            return

        selected_theme = theme_list[selected_index[0]]
        apply_theme(selected_theme, db_folder_location, themes_listbox)
        nonlocal last_applied_theme
        last_applied_theme = selected_theme["name"]

    def refresh_theme_list():
        themes_listbox.delete(0, "end")
        for theme in theme_list:
            themes_listbox.insert("end", theme["name"])

    messagebox.showinfo("Installation folder", "Please select Double Commander installation folder");
    db_folder_location = get_input_folder_location()

    # Theme List
    themes_listbox = Listbox(root, selectmode="SINGLE", height=10, width=50)
    themes_listbox.grid(row=0, column=0, padx=10, pady=10)
    refresh_theme_list()

    scrollbar = Scrollbar(root, orient="vertical")
    scrollbar.grid(row=0, column=1, sticky="ns")
    themes_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=themes_listbox.yview)

    # Buttons
    show_button = Button(root, text="Show Picture", command=on_theme_select)
    show_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    apply_button = Button(root, text="Apply Theme", command=on_theme_apply)
    apply_button.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    quit_button = Button(root, text="Quit", command=on_quit)
    quit_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    root.mainloop()

if __name__ == "__main__":
    main()
