import os
import hashlib
import tkinter as tk
from tkinter import messagebox
from tkinter import*


root = tk.Tk(screenName='Image_Finder', baseName='Image_Finder', className='Image_Finder',useTk=True)
root.title("Ayush Aditya")
root.geometry("700x500")
l = Label(root, text='Does the image exist in the file ?')
l.pack()
Label(root, text="Which file you want to search for ?").pack()
e1 = Entry(root)
e1.pack()
Label(root, text="Where do you want to search it for ?").pack()
e2 = Entry(root)
e2.pack()


def file_hash(filepath):
    """Return SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def image_exists_by_content():
    """Check if an image with same content exists in search_dir."""
    target_path = e1.get()
    search_dir = e2.get()
    result = False
    if not os.path.exists(target_path):
        result = False

    target_hash = file_hash(target_path)

    for root, _, files in os.walk(search_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                try:
                    if file_hash(file_path) == target_hash:
                        result = True
                except Exception:
                    pass  # Skip unreadable files

    if result:
        messagebox.showinfo(message="Yes the image exists")
    else:
        messagebox.showinfo(message="No the image is not there")


b = Button(root, text='Find out!', bg="blue", width=25, command = image_exists_by_content)
b.pack()

# Example usage"C:\\Users\\AYUSH ADITYA\\Pictures\\Screenshots"
# "C:\\Users\\AYUSH ADITYA\\PycharmProjects\\pythonProject\\static\\images\\Screenshot (194).png"


root.mainloop()