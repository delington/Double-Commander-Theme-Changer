import tkinter as tk
import process


class GUI:
    def __init__(self, master, *inputs):
        self.master = master
        master.title("My App")

        # Create labels and images for each option
        self.option_labels = []
        self.option_images = []
        self.option_buttons = []

        for i, input_path in enumerate(inputs):
            label = tk.Label(master, text=f"Option {i+1}")
            image = tk.PhotoImage(file=input_path).subsample(2)
            button = tk.Button(master, image=image, command=lambda index=i: self.select_option(index))

            self.option_labels.append(label)
            self.option_images.append(image)
            self.option_buttons.append(button)

        # Create apply and exit buttons
        self.apply_button = tk.Button(master, text="Apply", command=self.apply_options)
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)

        # Use grid layout to position widgets
        num_options = len(inputs)
        for i in range(num_options):
            self.option_labels[i].grid(row=0, column=i)
            self.option_buttons[i].grid(row=1, column=i)

        self.apply_button.grid(row=2, column=0)
        self.exit_button.grid(row=2, column=num_options-1)

    def select_option(self, index):
        print(f"Option {index+1} selected")

    def apply_options(self):
        print("Applying options")
        process.apply_changes()

root = tk.Tk()
app = GUI(root, "option1.png", "option2.png", "option3.png")
root.mainloop()
