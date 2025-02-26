import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from encode import hide_message
from decode import extract_message
from image_utils import convert_jpg_to_png

# Create GUI Window
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("500x450")

selected_image = tk.StringVar()
secret_message = tk.StringVar()

# Select Image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp;*.jpg")])
    if file_path:
        converted_path = convert_jpg_to_png(file_path)  # Convert JPG to PNG if needed
        selected_image.set(converted_path)

# Encode Message
def encode():
    if not selected_image.get():
        messagebox.showerror("Error", "Please select an image.")
        return
    
    message = secret_message.get()
    if not message:
        messagebox.showerror("Error", "Please enter a secret message.")
        return

    password = simpledialog.askstring("Password", "Set a decryption password:", show="*")
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    output_image = "stego_image.png"
    hide_message(selected_image.get(), message, output_image, password)
    messagebox.showinfo("Success", "Message hidden successfully in 'stego_image.png'!")

# Decode Message
def decode():
    if not selected_image.get():
        messagebox.showerror("Error", "Please select an image.")
        return

    password = simpledialog.askstring("Password", "Enter decryption password:", show="*")
    if not password:
        messagebox.showerror("Error", "Password required!")
        return

    hidden_text = extract_message(selected_image.get(), password)
    if hidden_text:
        messagebox.showinfo("Extracted Message", f"Hidden Message: {hidden_text}")
    else:
        messagebox.showerror("Error", "Incorrect password!")

# GUI Elements
tk.Label(root, text="Steganography Tool", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Select Image", command=select_image).pack()
tk.Label(root, textvariable=selected_image, wraplength=400).pack()
tk.Label(root, text="Enter Secret Message:").pack()
tk.Entry(root, textvariable=secret_message, width=40).pack()
tk.Button(root, text="Encode Message", command=encode, bg="lightblue").pack(pady=5)
tk.Button(root, text="Decode Message", command=decode, bg="lightgreen").pack(pady=5)

root.mainloop()