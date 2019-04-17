import sys
from tabula import read_pdf, convert_into

# TODO - this only parses the first page. 
fn = sys.argv[1]
csv = convert_into(fn, f"{fn}.csv", output_format="csv", pages="all")

