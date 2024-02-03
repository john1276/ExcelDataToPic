import tkinter as tk
from tkinter import filedialog
def FileOpen():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path
def FolderOpen():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path