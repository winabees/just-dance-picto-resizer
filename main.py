import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()

root.geometry("700x300")
root.title("Just Dance Picto Resizer")
root.iconbitmap("icon.ico")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

def choose_folder():
    path_selected = filedialog.askdirectory()
    folderEntry.delete(0, tk.END)
    folderEntry.insert(0, path_selected)

def export_pictoes():

    input_folder = folderEntry.get()
    size_text = resize_entry.get()

    if not input_folder or not size_text:
        print("Error: Please select a folder and enter a pixel size.")
        return
    
    try:
        width_str, height_str = size_text.split('x')
        width = int(width_str.strip())
        height = int(height_str.strip())
    except ValueError:
        print("Error: Please make sure to enter the size as WIDTHxHEIGHT (e.g., 256x256)")
        return # Stop if they entered something weird like letters or forgot the 'x'
    
    print("Looping throught folder...")

    for root, dirs, files in os.walk(input_folder):
        for n in files:
                if n.lower().endswith('.png'):
                 fp = os.path.join(root, n)

                with Image.open(fp) as img:
                    print("Resizing")

                    resized_img = img.resize((width, height), Image.Resampling.LANCZOS)

                    out_fp = os.path.join('output', n)
                    resized_img.save(out_fp) 
                    print(f"Resized {n} successfully!")
    

    

label = tk.Label(root, text="JUST DANCE PICTO RESIZER!", font=('Verdana', 25))
label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=20)

folderEntry = tk.Entry(root, width=80)
folderEntry.grid(row=1, column=0, padx=10, pady=10)

buttonFldr = tk.Button(root, text="SELECT FOLDER", font=('Arial', 18), command=choose_folder)
buttonFldr.grid(row=1, column=1, padx=10, pady=10)

resize_entry = tk.Entry(root, width=80)
resize_entry.grid(row=2, column=0, padx=10, pady=10)

btnExport = tk.Button(root, text="EXPORT", font=('Arial', 18), command=export_pictoes)
btnExport.grid(row=2, column=1, padx=10, pady=20)

root.mainloop()