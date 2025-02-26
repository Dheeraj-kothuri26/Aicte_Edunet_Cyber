import cv2
import numpy as np
import hashlib

# Convert text to binary format
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'  # End marker

# Hide message in image
def hide_message(image_path, message, output_path, password):
    img = cv2.imread(image_path)

    if img is None:
        print("❌ Error: Could not open image.")
        return

    # Hash password to avoid corruption
    hashed_password = hashlib.sha256(password.encode()).hexdigest()[:10]  # Use only first 10 chars for storage
    secret_data = hashed_password + ":" + message  # Store hashed password + message

    binary_message = text_to_binary(secret_data)  # Convert message to binary
    binary_index = 0
    height, width, channels = img.shape

    for row in range(height):
        for col in range(width):
            for i in range(3):  # Modify only RGB channels
                if binary_index < len(binary_message):
                    bit_value = int(binary_message[binary_index])
                    new_pixel_value = (int(img[row, col, i]) & ~1) | bit_value  # Ensure valid pixel value

                    # Clip to 0-255 range
                    img[row, col, i] = np.clip(new_pixel_value, 0, 255).astype(np.uint8)

                    binary_index += 1

                if binary_index >= len(binary_message):
                    break
            if binary_index >= len(binary_message):
                break
        if binary_index >= len(binary_message):
            break

    cv2.imwrite(output_path, img)
    print("✅ Message hidden successfully in 'stego_image.png'!")
