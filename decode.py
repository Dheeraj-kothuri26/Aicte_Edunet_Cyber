import cv2
import numpy as np
import hashlib

# Convert binary to text format
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    text = ''.join(chr(int(char, 2)) for char in chars if int(char, 2) < 128)  # Only use ASCII values
    return text

# Extract message from image
def extract_message(image_path, password):
    img = cv2.imread(image_path)

    if img is None:
        print("❌ Error: Could not open image.")
        return None

    binary_message = ""
    height, width, channels = img.shape

    print("🔄 Extracting message, please wait...")

    for row in range(height):
        for col in range(width):
            for i in range(3):  # Extract only RGB channels
                binary_message += str(img[row, col, i] & 1)

                # Stop reading once the end marker is found
                if binary_message.endswith('1111111111111110'):
                    break
            if binary_message.endswith('1111111111111110'):
                break
        if binary_message.endswith('1111111111111110'):
            break

    # Ensure enough bits were extracted
    if len(binary_message) < 16:
        print("⚠️ No valid hidden message found!")
        return None

    # Remove end marker
    binary_message = binary_message.replace('1111111111111110', '')

    # Convert binary to text
    full_text = binary_to_text(binary_message)

    # Debug extracted text
    print("🔍 Extracted Full Text:", full_text)

    # Extract password and message
    if ":" in full_text:
        stored_password, hidden_message = full_text.split(":", 1)

        # Hash the user-entered password and compare it to the stored password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()[:10]  # Use first 10 chars
        print("🔑 Extracted Password (Stored):", stored_password)
        print("🔑 Hashed Input Password:", hashed_password)

        if stored_password.strip() == hashed_password.strip():
            return hidden_message
        else:
            print("❌ Incorrect password!")
            return None
    print("⚠️ No valid message found in image.")
    return None

