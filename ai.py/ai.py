import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def create_seamless_pattern(image_path, tile_size=(500, 500)):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    
    img_array = np.array(img)
    h, w, _ = img_array.shape
    
    pattern_canvas = Image.new("RGBA", tile_size)
    for i in range(0, tile_size[0], w):
        for j in range(0, tile_size[1], h):
            pattern_canvas.paste(img, (i, j), img)
    
    return pattern_canvas

def choose_file():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    return file_path

def main():
    image_path = choose_file()  # User will select file from dialog
    if not image_path:
        print("❌ No file selected!")
        return
    
    seamless_pattern = create_seamless_pattern(image_path)
    
    plt.figure(figsize=(5,5))
    plt.imshow(seamless_pattern)
    plt.axis("off")
    plt.show()
    
    seamless_pattern.save("seamless_output.png")
    print("✅ Pattern saved as seamless_output.png!")

if __name__ == "__main__":
    main()
