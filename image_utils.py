from PIL import Image
import os

def convert_jpg_to_png(image_path):
    if image_path.lower().endswith(".jpg"):
        png_path = image_path.replace(".jpg", ".png")
        img = Image.open(image_path)
        img.save(png_path, "PNG")
        return png_path
    return image_path
