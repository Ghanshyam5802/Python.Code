from PIL import Image
import numpy as np
from math import sin, pi, floor
import sys

def maketilable(src_path, dst_path):
    src = Image.open(src_path).convert('RGB')
    src_w, src_h = src.size
    
    dst = Image.new('RGB', (src_w, src_h))
    get = src.load()
    put = dst.load()
    
    def warp(p, l, dl):
        i = (p / l) * 2 * pi
        return abs((sin(i + pi) / 2 + 0.5) * dl)
    
    warpx = [warp(x, src_w - 1, src_w - 1) for x in range(src_w)]
    warpy = [warp(y, src_h - 1, src_h - 1) for y in range(src_h)]
    
    def getpixel(x, y):
        x0, y0 = int(x) % src_w, int(y) % src_h
        x1, y1 = (x0 + 1) % src_w, (y0 + 1) % src_h
        
        frac_x, frac_y = x - floor(x), y - floor(y)
        
        a = np.array(get[x0, y0]) * (1 - frac_x) * (1 - frac_y)
        b = np.array(get[x1, y0]) * frac_x * (1 - frac_y)
        c = np.array(get[x0, y1]) * (1 - frac_x) * frac_y
        d = np.array(get[x1, y1]) * frac_x * frac_y
        
        return tuple((a + b + c + d).astype(int))
    
    for y in range(src_h):
        print(f'{(y / src_h) * 100:.2f}% complete', end='\r')
        for x in range(src_w):
            put[x, y] = getpixel(warpx[x], warpy[y])
    
    dst.save(dst_path)
    print("Processing complete! Saved to", dst_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_image_path> <destination_image_path>")
    else:
        maketilable(sys.argv[1], sys.argv[2])