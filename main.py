import string
from tkinter import *
import tkinter as tk
from os.path import exists

# Creates the username.txt file if it doesn't already exist in the project directory
if not exists('usernames.txt'):
    with open('usernames.txt', 'w') as f:
        print("\nError: Missing files.\nThe required files has been created, please restart.")
        quit()


class Usernames:
    """Creating and storing usernames if they are available"""
    def __init__(self, root):
        root.geometry("500x225")
        root.title("Username Creator")
        root.resizable(False, False)
        self.font = "Open Sans"
        self.font_size = 18
        self.is_available = True

        """Buttons and Labels"""
        # Canvas
        canvas = tk.Canvas(root, width=500, height=300)
        canvas.pack()

        # Username Text
        username_text = tk.Label(canvas, text="Username:")
        username_text.config(font=(self.font, self.font_size, 'bold'))
        canvas.create_window(105, 50, window=username_text)

        # Username Input
        self.user_input = tk.Entry(canvas)
        self.user_input.config(font=(self.font, self.font_size), relief=GROOVE)
        canvas.create_window(315, 50, window=self.user_input)

        # Create Button
        self.create_button = tk.Button(canvas, text="Create", padx=32, pady=2, borderwidth=2)
        self.create_button.config(font=(self.font, 13), relief=GROOVE, command=self.create_username)
        canvas.create_window(245, 95, window=self.create_button)

        # Clear Button
        self.clear_button = tk.Button(canvas, text="Clear", padx=38.5, pady=2, borderwidth=2)
        self.clear_button.config(font=(self.font, 13), relief=GROOVE, command=self.clear_entry)
        canvas.create_window(383, 95, window=self.clear_button)

        # Status Text
        status_text = tk.Label(canvas, text="Status:")
        status_text.config(font=(self.font, self.font_size, "bold"))
        canvas.create_window(126, 160, window=status_text)

        # Status
        self.status = StringVar()
        self.status_value = tk.Label(canvas, textvariable=self.status)
        self.status_value.config(font=(self.font, 15))
        canvas.create_window(315, 160, window=self.status_value)

    def create_username(self, keybind=None):
        """
        Checks if the username is available
        If it is available then add it else return username taken
        """

        # List of symbols not allowed
        not_allowed = string.punctuation + string.whitespace

        # Getting the user's input and formatting it for processing
        user_input = self.user_input.get().lower()
        username = f"{user_input}\n"

        for i in not_allowed:
            if i in user_input:
                self.is_available = False
                break
            else:
                self.is_available = True

        if self.is_available and user_input != "":
            with open("usernames.txt", "r") as r:
                current_usernames = r.readlines()

                for current_username in current_usernames:
                    if username != current_username:
                        self.is_available = True
                    else:
                        self.is_available = False
                        break

                if self.is_available:
                    with open("usernames.txt", "a") as a:
                        a.write(username)
                        self.status.set("Username Successfully Added")
                        self.status_value.after(1200, lambda: self.status.set(""))
                else:
                    self.status.set("Username is Taken")
                    self.status_value.after(1200, lambda: self.status.set(""))
        elif self.is_available and user_input == "":
            self.status.set("Please provide a username.")
            self.status_value.after(1200, lambda: self.status.set(""))
        else:
            self.status.set("No spaces or special\ncharacters allowed.")
            self.status_value.after(1200, lambda: self.status.set(""))

    def clear_entry(self, keybind=None):
        """Clear the entry window"""
        self.user_input.delete(0, END)
        self.status.set("Input has been cleared")
        self.status_value.after(1200, lambda: self.status.set(""))


main_root = Tk()
usernames = Usernames(main_root)
main_root.bind("<Return>", usernames.create_username)
main_root.bind("<Escape>", usernames.clear_entry)
main_root.mainloop()
