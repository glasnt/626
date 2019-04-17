import sys
import csv
import json
from tabula import read_pdf, convert_into

fn = sys.argv[1]
cfn = f"{fn}.csv"

convert_into(fn, cfn, output_format="csv", pages="all")
headers = ["description", None, "floss"] 

mappings = []

with open(cfn) as f:
    data = csv.reader(f, delimiter=",")


    for i, line in enumerate(data):
        
        # ignore headings on every page.
        if line[0].split(" ")[0] in ["", "COLOR", "AND", "SWATCH"]:
            continue

        thread = {}

        for idx, header in enumerate(headers):
            if header:
                thread[header] = line[idx]
        # uugghh
        thread["wool"] = line[-1]
        mappings.append(thread)


with open("mappings.json", "w") as f:
    json.dump(mappings, f)
