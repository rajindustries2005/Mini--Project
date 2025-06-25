import os
import zipfile
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def zip_file_or_folder(path, output_zip):
    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isdir(path):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, os.path.dirname(path))
                        zipf.write(file_path, arcname)
            elif os.path.isfile(path):
                zipf.write(path, os.path.basename(path))
            else:
                return False, "Error: Path is neither a file nor a directory."
        return True, f"Successfully created zip file at: {output_zip}"
    except Exception as e:
        return False, f"Error zipping: {e}"

def unzip_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return True, f"Successfully extracted to: {extract_to}"
    except Exception as e:
        return False, f"Error unzipping: {e}"

def select_file_or_folder():
    path = filedialog.askopenfilename(title="Select file or folder")
    if not path:
        path = filedialog.askdirectory(title="Select folder")
    return path

def gui_zip():
    path = select_file_or_folder()
    if not path:
        return
    default_output = os.path.join(os.path.dirname(path), os.path.basename(path) + '.zip')
    output_zip = filedialog.asksaveasfilename(defaultextension=".zip", initialfile=os.path.basename(default_output), filetypes=[("Zip files", "*.zip")])
    if not output_zip:
        return
    success, msg = zip_file_or_folder(path, output_zip)
    messagebox.showinfo("Zip Result", msg)

def gui_unzip():
    zip_path = filedialog.askopenfilename(title="Select zip file", filetypes=[("Zip files", "*.zip")])
    if not zip_path:
        return
    default_extract = os.path.join(os.path.dirname(zip_path), os.path.splitext(os.path.basename(zip_path))[0])
    extract_to = filedialog.askdirectory(title="Select directory to extract to", initialdir=default_extract)
    if not extract_to:
        return
    success, msg = unzip_file(zip_path, extract_to)
    messagebox.showinfo("Unzip Result", msg)

def main():
    root = tk.Tk()
    root.title("Zip/Unzip Utility")
    root.geometry("300x150")
    tk.Label(root, text="Zip/Unzip Utility", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Zip a file or folder", width=25, command=gui_zip).pack(pady=5)
    tk.Button(root, text="Unzip a file", width=25, command=gui_unzip).pack(pady=5)
    tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    main()