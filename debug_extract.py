import cv2

def debug_extract(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("❌ Error: Could not open image.")
        return

    binary_message = ""
    height, width, channels = img.shape

    for row in range(height):
        for col in range(width):
            for i in range(3):  # Extract only RGB channels
                binary_message += str(img[row, col, i] & 1)

                # Print first 100 bits to debug
                if len(binary_message) >= 100:
                    break
            if len(binary_message) >= 100:
                break
        if len(binary_message) >= 100:
            break

    print("📝 First 100 Bits Extracted:", binary_message[:100])

debug_extract("stego_image.png")  # Run on your encoded image
