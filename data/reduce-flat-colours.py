#!/usr/bin/env python
import sys
import json
from skimage.color import deltaE_ciede2000, rgb2lab

# For reducing the colourset
# requires scikit-image

def rgb2one(r):
    return (float(r[0]/256),float(r[1]/256),float(r[2]/256))
    
TOP_LEVEL = 100

with open(sys.argv[1]) as f:
    colours = f.readlines()

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

results = []
for i in colours:
    iname, ihex = i.strip().split(",")
    irgb = hex_to_rgb(ihex)

    for j in colours:
        jname, jhex = j.strip().split(",")
        jrgb = hex_to_rgb(jhex)

        if ihex == jhex:
            continue

        io = rgb2one(irgb) 
        jo = rgb2one(jrgb)

        d = deltaE_ciede2000(io, jo)
        
        result = f"<tr><td>{d}</td>"
        result += f"<td>{iname}</td><td>{ihex}</td><td style='background-color: {ihex}'>&nbsp; &nbsp; &nbsp; &nbsp;</td>"
        result += f"<td style='background-color: {jhex}'>&nbsp; &nbsp; &nbsp; &nbsp;</td><td>{jhex}</td><td>{jname}</td>"
        result += "</tr>"

        results.append(result)

print(f"Top {TOP_LEVEL} similar colours for {sys.argv[1]}")
print("<table>")
sort = sorted(results)
print("\n".join(sort[:100]))
print("</table>")
