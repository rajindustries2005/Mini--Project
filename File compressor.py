import tkinter as tk
from tkinter import filedialog, messagebox
import gzip
import os
import shutil
import zipfile
from threading import Thread

class FileCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compressor")
        self.root.geometry("500x300")
        
        # Variables
        self.file_path = tk.StringVar()
        self.compression_type = tk.StringVar(value="gzip")
        self.status = tk.StringVar(value="Ready")
        
        # GUI Elements
        self.create_widgets()
    
    def create_widgets(self):
        # File Selection Frame
        file_frame = tk.LabelFrame(self.root, text="Select File", padx=10, pady=10)
        file_frame.pack(pady=10, padx=10, fill="x")
        
        tk.Entry(file_frame, textvariable=self.file_path, width=40).pack(side="left", padx=5)
        tk.Button(file_frame, text="Browse", command=self.browse_file).pack(side="left")
        
        # Compression Options Frame
        options_frame = tk.LabelFrame(self.root, text="Compression Options", padx=10, pady=10)
        options_frame.pack(pady=10, padx=10, fill="x")
        
        tk.Radiobutton(options_frame, text="GZIP (Fast)", variable=self.compression_type, value="gzip").pack(anchor="w")
        tk.Radiobutton(options_frame, text="ZIP (Standard)", variable=self.compression_type, value="zip").pack(anchor="w")
        
        # Action Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Compress File", command=self.start_compression, width=15).pack(side="left", padx=5)
        tk.Button(button_frame, text="Exit", command=self.root.quit, width=15).pack(side="left", padx=5)
        
        # Status Bar
        status_frame = tk.Frame(self.root, bd=1, relief="sunken")
        status_frame.pack(side="bottom", fill="x", padx=5, pady=5)
        tk.Label(status_frame, textvariable=self.status).pack(side="left")
    
    def browse_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.file_path.set(filename)
            self.status.set(f"Selected: {os.path.basename(filename)}")
    
    def start_compression(self):
        if not self.file_path.get():
            messagebox.showerror("Error", "Please select a file first!")
            return
        
        # Disable buttons during compression
        self.status.set("Compressing... Please wait")
        self.root.config(cursor="watch")
        
        # Start compression in a separate thread to keep GUI responsive
        Thread(target=self.compress_file, daemon=True).start()
    
    def compress_file(self):
        try:
            input_file = self.file_path.get()
            compression_type = self.compression_type.get()
            
            if compression_type == "gzip":
                output_file = input_file + ".gz"
                self.compress_with_gzip(input_file, output_file)
            elif compression_type == "zip":
                output_file = os.path.splitext(input_file)[0] + ".zip"
                self.compress_with_zip(input_file, output_file)
            
            # Show success message
            original_size = os.path.getsize(input_file)
            compressed_size = os.path.getsize(output_file)
            ratio = (1 - compressed_size / original_size) * 100
            
            message = (
                f"Compression complete!\n\n"
                f"Original size: {original_size:,} bytes\n"
                f"Compressed size: {compressed_size:,} bytes\n"
                f"Compression ratio: {ratio:.2f}%\n"
                f"Saved as: {os.path.basename(output_file)}"
            )
            
            self.status.set("Compression complete!")
            messagebox.showinfo("Success", message)
            
        except Exception as e:
            self.status.set("Error occurred")
            messagebox.showerror("Error", f"Compression failed: {str(e)}")
        finally:
            self.root.config(cursor="")
    
    def compress_with_gzip(self, input_file, output_file):
        with open(input_file, 'rb') as f_in:
            with gzip.open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    
    def compress_with_zip(self, input_file, output_file):
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(input_file, os.path.basename(input_file))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileCompressorApp(root)
    root.mainloop()