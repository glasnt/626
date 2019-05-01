from PIL import Image, ImageStat
import sys

def avg_color(im):
    stats = ImageStat.Stat(im)
    return tuple(stats.median)

fn = sys.argv[1]
im = Image.open(fn)
color = avg_color(im)
with open(f"{fn}.html", "w") as f:
    html = (f"""
            <span style='
                height: {im.height}; 
                width: {im.width * 2};
                background-color: rgb{color};
                display: inline-block;
            '>
            <img src='{fn}'>
            <span style='float: right'>{color}</span>
            </span>
            """)
    #    f.write(html)
    print(html)
