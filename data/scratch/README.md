# Scratch space

Mostly a mirror of sample code presented in ["A Right Stitch Up"](https://us.pycon.org/2019/schedule/presentation/229/), with more explanation. 

## `avg_color.py`

Using a sample image, get the average color. 

Cavets: applying this across multiple images shot in different lightning may not yield the results you expect. 

## `DMC_TAPTESRY_WOOL.zip`

A cache of all the raw wool images displayed on the [DMC website](https://www.dmc.com/us/tapestry-wool-100-colors-available-9001711.html), as of 17-APR-2019. Images marked "OUTOFSTOCK" based on the same flag on the website. 

Collected using XHR setting in [Save All Resources](https://chrome.google.com/webstore/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb/related?hl=en-US)

## creating a palette of colours

```shell
for i in $(ls DMC_TAPESTRY_WOOL/*.jpg | grep -v OUT); do python avg_color.py $i >> results.html; done
open results.html
```

## `color-csv-parser.py`

Combines: 

* A generic pdf parser method, using tabular ([reference](https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302))

and

* Using the csv output of pdf-parser, usefully parse the data out of the 

Note: tabula requires java

Results in mappings.json


## Consolidate into a palette format.

Convert the CSV and Mappings into one nice format

What makes a good palette format?
 
 * The Thread Type (normally as the file name)
 * For each thread: 
  * The Manufacturer Code
  * The Descriptive Name
  * The Hex Code

Descriptive names are optional, therefore, there is just CODE and HEX

Given this simplicity, all palettes are now CSV files, comma seperated CODE,HEX. 

## paletteplot.py

A ipython notebook of the visualisation of palettes (note: inline copy of data for ease of notebook)

## reduce-flat-colours.py

Given a palette of CODE,NAME reduce it to only 256 values, removing one of each to the closest palette pairs.

Uses `delta_ciede2000` to determine colour distance
