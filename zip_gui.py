import os
import zipfile
import tkinter as tk
from tkinter import ttk, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD


def zip_folder(folder_path):
    zip_path = folder_path + ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, os.path.dirname(folder_path))
                zipf.write(abs_path, rel_path)

def compress_all():
    if not folder_list:
        messagebox.showwarning("Warning", "No folders have been added.")
        return

    for folder in folder_list:
        try:
            zip_folder(folder)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while compressing {folder}: {e}")
            return
    messagebox.showinfo("Done", "All folders have been successfully compressed.")


def drop(event):
    dropped = root.tk.splitlist(event.data)
    for item in dropped:
        item = item.strip()
        if os.path.isdir(item) and item not in folder_list:
            folder_list.append(item)
            listbox.insert(tk.END, item)


# GUI Setup
root = TkinterDnD.Tk()
root.title("Folder-to-ZIP Converter")
root.geometry("500x400")
root.config(bg="#f0f0f0")

folder_list = []

# Style
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TListbox", font=("Segoe UI", 10))

# Label
label = ttk.Label(root, text="Drag and drop folders here", background="#f0f0f0")
label.pack(pady=10)

# Listbox
listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(padx=10, pady=10)
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', drop)

# Button
btn = ttk.Button(root, text="Compress All", command=compress_all)
btn.pack(pady=10)

root.mainloop()
