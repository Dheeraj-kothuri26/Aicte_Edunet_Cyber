# Secure Data Hiding in Image Using Steganography

## 📌 Project Overview

This project implements **Least Significant Bit (LSB) Steganography** to hide and extract secret messages within images. It includes **password-based decryption** for added security.

## 🚀 Features

✅ **Password-Based Decryption** – Only authorized users can extract messages.\
✅ **JPG to PNG Auto-Conversion** – Ensures lossless image format.\
✅ **Graphical User Interface (GUI)** – Easy-to-use Tkinter-based interface.\
✅ **LSB Steganography** – Invisible data hiding inside images.\
✅ **Secure Encryption (SHA-256)** – Adds an extra security layer.

## 📂 Project Structure

```
Secure_Data_Hiding/
│── app.py             # Main Tkinter GUI
│── encode.py          # Hides text using LSB steganography
│── decode.py          # Extracts hidden text with password verification
│── image_utils.py     # Converts JPG to PNG if needed
│── sample_image.png   # Test image (Use PNG format)
│── stego_image.png    # Output image after encoding
│── requirements.txt   # Dependencies list
│── README.md          # Documentation
```

## 🔧 Installation

1. Clone the repository:
   ```sh
   git clone [your-repo-link]
   cd Secure_Data_Hiding
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## ▶ Usage

### **1️⃣ Run the GUI**

```sh
python app.py
```

### **2️⃣ Encoding Process**

1. Click **"Select Image"** and choose a PNG/JPG image.
2. Enter the **secret message** and **set a password**.
3. Click **"Encode Message"** → The new `stego_image.png` is generated.

### **3️⃣ Decoding Process**

1. Click **"Select Image"** and choose `stego_image.png`.
2. Enter the **correct password**.
3. Click **"Decode Message"** → The extracted message appears.

## 📝 Example Output

**Hiding Message:**

```
✅ Message hidden successfully in 'stego_image.png'!
```

**Extracting Message:**

```
🔑 Enter Password: [User Inputs Password]
📝 Extracted Message: "Hello, this is a secret!"
```

## 🔮 Future Enhancements

🔹 **AES Encryption** – Adding a stronger encryption layer before embedding.\
🔹 **Audio & Video Steganography** – Expanding beyond images.\
🔹 **AI-Based Steganalysis Resistance** – Preventing detection by advanced tools.

## 📜 License

This project is licensed under [MIT License].

## 🤝 Contributing

Feel free to **fork** this repository and submit **pull requests** for improvements!

## 📩 Contact

For any queries, contact [Dheeraj-Kothuri] at kothuridheeraj\@gmail.com.

