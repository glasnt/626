# 626

Ih. 

## Setup

Requires Python 3, and installed `requirements.txt`

```
pyenv local 3.6.3
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Test

```
./ih test_image.png -s2
```

## Usage

```
Usage: ih [OPTIONS] IMAGE

  Given a image filename, and optional parameters; generate a chart

Options:
  -p, --palette TEXT     Choices: wool, floss, alpaca. Default: wool
  -s, --scale INTEGER    Rescale factor. Default: 1
  -c, --colours INTEGER  Limit palette to N colors. Default: 256
  -n, --no-open          Don't auto-open result file
  -t, --thread           Preview threaded display
  --help                 Show this message and exit.
```

Now with added alpaca

Pending proper documentation. 
