import os
from PIL import Image

INPUT_DIR = "assets"
OUTPUT_DIR = "outputs"

COLOR_MAP = {
    "413f54": "0a090e",
    "f2f2f2": "8e8e8e",
    "cbccd4": "42434b",
    "adb0c4": "2d2f3c",
    "9a9fb4": "242631",
    "696d88": "14151d",
    "878fa5": "1d2029",
    "e8e8ea": "6d6d72",
    "4d4d67": "0d0d13"
}

COLOR_MAP_RGB = {
    tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)):
    tuple(int(new_color[i:i+2], 16) for i in (0, 2, 4))
    for hex_color, new_color in COLOR_MAP.items()
}

def process_image(file_path, output_path):
    img = Image.open(file_path).convert("RGBA")
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if (r, g, b) in COLOR_MAP_RGB:
                nr, ng, nb = COLOR_MAP_RGB[(r, g, b)]
                pixels[x, y] = (nr, ng, nb, a)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")


def main():
    for root, _, files in os.walk(INPUT_DIR):
        for filename in files:
            if filename.lower().endswith(".png"):
                input_path = os.path.join(root, filename)

                rel_path = os.path.relpath(input_path, INPUT_DIR)
                output_path = os.path.join(OUTPUT_DIR, rel_path)

                process_image(input_path, output_path)
                print(f"Processed {rel_path}")


if __name__ == "__main__":
    main()
