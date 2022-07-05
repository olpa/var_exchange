# Share Python variables over Dropbox

## Usage

One location:

```
from var_exchange.kaggle_dropbox import get_putv_getv

putv, getv = get_putv_getv(basedir='/a/b/c')
putv('hello from location 1', 'x')
```

Another location:

```
from var_exchange.kaggle_dropbox import get_putv_getv

putv, getv = get_putv_getv(basedir='/a/b/c')
x = getv('x')
print(x)
```

Command line tool `kd_run.py`:

```
usage: kd_run.py [-h] [--setup] [--basedir BASEDIR] [--get-file GET_FILE]
                 [--put-file PUT_FILE] [--get-var GET_VAR]

Exchange Python variables through Dropbox

optional arguments:
  -h, --help           show this help message and exit
  --setup              create auth file
  --basedir BASEDIR    parent directory on Dropbox
  --get-file GET_FILE
  --put-file PUT_FILE
  --get-var GET_VAR    get file from dropbox and print as python variable

```

## Installation and setup

1. Install the package

```
VERSION=1.0.0
pip3 install https://github.com/olpa/var_exchange/archive/refs/tags/1.0.0.zip
```

2. Create an application in dropbox, get the application key and secret.

3. Run

```
kd_run.py --setup
```

Follow the instructions. As the result, you'll have a json with an authentification data, something like:

```
{
  "key": "xxxxxxxxxxxxxxx",
  "secret": "yyyyyyyyyyyyyyy",
  "oauth": "zzzzzzzz...zzzzzzz="
}
```

4. Store the json in the file `~/.kaggle/dropbox.json`

5. On Kaggle, go to a notebook and create a secret named `dropbox`. Store the json as the value of the secret.

## License

MIT
