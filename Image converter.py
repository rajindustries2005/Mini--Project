from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def image_converter_gui():
    def select_file():
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.tiff")]
        )
        if file_path:
            input_entry.delete(0, tk.END)
            input_entry.insert(0, file_path)

    def convert_image():
        input_path = input_entry.get().strip('"').strip("'")
        output_format = format_var.get().upper()
        supported_formats = ['JPG', 'JPEG', 'PNG', 'BMP', 'GIF', 'TIFF']

        if not os.path.isfile(input_path):
            messagebox.showerror("Error", "File not found!")
            return

        if output_format not in supported_formats:
            messagebox.showerror("Error", f"Unsupported format. Please choose from: {', '.join(supported_formats)}")
            return

        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}_converted.{output_format.lower()}"

        try:
            with Image.open(input_path) as img:
                if output_format in ['JPG', 'JPEG'] and img.mode in ['RGBA', 'LA']:
                    img = img.convert('RGB')
                img.save(output_path, format=output_format)

            input_size = os.path.getsize(input_path)
            output_size = os.path.getsize(output_path)
            result_text.set(
                f"Image converted successfully!\n"
                f"Saved as: {output_path}\n"
                f"Original size: {input_size} bytes\n"
                f"Converted size: {output_size} bytes"
            )
        except Exception as e:
            if os.path.exists(output_path):
                os.remove(output_path)
            messagebox.showerror("Error", f"An error occurred during conversion: {str(e)}")
            result_text.set("")

    root = tk.Tk()
    root.title("Image Format Converter")
    root.geometry("450x300")
    root.resizable(False, False)

    tk.Label(root, text="Image Format Converter", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(root, text="Supported formats: JPG, PNG, BMP, GIF, TIFF").pack()

    frame = tk.Frame(root)
    frame.pack(pady=10)

    input_entry = tk.Entry(frame, width=35)
    input_entry.grid(row=0, column=0, padx=5)
    tk.Button(frame, text="Browse...", command=select_file).grid(row=0, column=1, padx=5)

    tk.Label(root, text="Select output format:").pack()
    format_var = tk.StringVar(value="PNG")
    format_combo = ttk.Combobox(root, textvariable=format_var, values=["JPG", "PNG", "BMP", "GIF", "TIFF"], state="readonly")
    format_combo.pack(pady=5)

    tk.Button(root, text="Convert", command=convert_image, width=15).pack(pady=10)

    result_text = tk.StringVar()
    tk.Label(root, textvariable=result_text, justify="left", wraplength=400, fg="green").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    image_converter_gui()