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

