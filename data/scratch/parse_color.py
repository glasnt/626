from PIL import Image
from pathlib import Path
import sys

def avg_color(im):
    count, r, g, b = [0,0,0,0]
    for x in range(0, im.width):
        for y in range(0, im.height):
            r1, g1, b1 = im.getpixel((x, y))
            r += r1; g += g1; b += b1
            count += 1

    return int(r/count), int(g/count), int(b/count)

fn = sys.argv[1]
im = Image.open(fn)
color = avg_color(im)
r,g, b = color
hexcode = "#{:02x}{:02x}{:02x}".format(r, g, b)

thread_name = Path(fn).name.split("_")[2]
print(f"{thread_name},{hexcode}")
