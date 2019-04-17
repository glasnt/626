import sys
import csv

fn = sys.argv[1]

with open(fn) as f:
    data = csv.reader(f, delimiter=",")

    header_lines = 5

    for line in data:
        print(line)
        # TODO parse out into usefulness
