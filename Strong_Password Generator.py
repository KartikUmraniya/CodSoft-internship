import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length):
    """
    Generate a random password of the specified length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_clicked():
    """
    Generate a password when the "Generate Password" button is clicked.
    """
    password_length = int(password_length_entry.get())
    if password_length < 6:
        message_label.config(text="Password length should be at least 6 characters for security.")
    else:
        generated_password = generate_password(password_length)
        message_label.config(text=f"Generated password: {generated_password}")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, generated_password)

def copy_password():
    """
    Copy the generated password to the clipboard.
    """
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    message_label.config(text="Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

## Password Length Input
password_length_label = ttk.Label(root, text="Enter the length of the password you want to generate:")
password_length_label.pack()

password_length_entry = ttk.Entry(root)
password_length_entry.pack()

## Generate Password Button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_clicked)
generate_button.pack()

## Password Display
password_entry = ttk.Entry(root, state="readonly")
password_entry.pack()

## Copy Password Button
copy_button = ttk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack()

## Message Label
message_label = ttk.Label(root, text="")
message_label.pack()

root.mainloop()