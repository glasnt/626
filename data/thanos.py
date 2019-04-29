#!/usr/bin/env python
import sys
import json
from skimage.color import deltaE_ciede2000, rgb2lab

# For reducing the colourset
# requires scikit-image

def rgb2one(r):
    return (float(r[0]/256),float(r[1]/256),float(r[2]/256))
    
TOP_LEVEL = 256

with open(sys.argv[1]) as f:
    colours = [x.strip() for x in f.readlines()]



def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

print("Colors: %s" % len(colours))

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
        
        result = {"left": f"{iname},{ihex}", "right": f"{jname},{jhex}", "distance": d}

        results.append(result)

print("Comparisons: %s" % len(results))

# prune
prune = []
uniq_dist = []


"""
for i, x in enumerate(results):
    if x["distance"] not in uniq_dist:
        prune.append(x)
        uniq_dist.append(x["distance"])
    if i % 1000 == 0:
        print("pruning... %s" % i)
"""

sortedresults = sorted(results, key=lambda x: x["distance"])

for i in range(0, len(sortedresults), 2):
    prune.append(sortedresults[i])


print("Prune: %s" % len(prune))

final = []

sort = sorted(prune, key=lambda x: x["distance"])

for x in sort:
    l = x["left"]
    if l in colours:
        colours.remove(l)
        print(f"removed {l}")
        if len(colours) == TOP_LEVEL:
            print("FINISHED\n\n\n")
            break


print("\n".join(colours))
    #for x in prune:
    
