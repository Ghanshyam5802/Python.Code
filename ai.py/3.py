from PIL import Image
import numpy as np
import sys

def maketilable(src_path, dst_path):
    src = Image.open(src_path).convert('RGB')
    src_w, src_h = src.size
    
    dst = Image.new('RGB', (src_w, src_h))
    get = src.load()
    put = dst.load()

    # Warp function ensuring seamless tiling
    def warp(p, l):
        return (p + (l // 2)) % l  # Ensures correct wrapping

    # Precompute warp mappings
    warpx = [warp(x, src_w) for x in range(src_w)]
    warpy = [warp(y, src_h) for y in range(src_h)]

    def getpixel(x, y):
        x0, y0 = int(x) % src_w, int(y) % src_h
        return get[x0, y0]

    # Process image with correct wrapping
    for y in range(src_h):
        print(f'{(y / src_h) * 100:.2f}% complete', end='\r')
        for x in range(src_w):
            put[x, y] = getpixel(warpx[x], warpy[y])

    dst.save(dst_path)
    print("\nProcessing complete! Saved to", dst_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_image_path> <destination_image_path>")
    else:
        maketilable(sys.argv[1], sys.argv[2])
