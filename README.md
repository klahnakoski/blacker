
# More Black! - Denser Black formatting

This is s a fork of [the Blackcode formatter](https://github.com/psf/black)

### Problem

I love Black formatting because I agree with its formatting choices, but it does have one pathology: [Excessive indenting on data structures](https://github.com/psf/black/issues/626)

```python
schema = {
    "mappings": {
        "test": {
            "properties": {
                "one_value": {
                    "type": "keyword",
                    "store": True,
                }
            }
        }
    }
}
```

### Solution: More Black!

When there is only one property (or list item, or parameter), then do not make a new line.

```python
schema = {"mappings": {"test": {"properties": {"one_value": {
    "type": "keyword", 
    "store": True,
}}}}}

```

## Usage

Please [read the official Black documentation at time of fork](https://github.com/psf/black/blob/537ea8df35b1004bdb228b483907fb5dd92e5257/README.md#usage)


## Development

Be sure you are in the `mo-black` main directory

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pip install -r tests/requirements.txt
    export PYTHONPATH=src:.
    export SKIP_AST_PRINT=true
    python -m unittest tests/test_black.py

...or Windows...

    python -m pip install virtualenv
    python -m virtualenv .venv             
    .venv\Scripts\activate
    pip install -r requirements.txt
    pip install -r tests\requirements.txt
    set PYTHONPATH=src;.
    set SKIP_AST_PRINT=true
    python -m unittest tests\test_black.py

### Development Installation

You can install `mo-black` from the main directory

    python.exe -m pip install .
