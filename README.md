
# Blacker - Denser Black formatting

This is s a fork of [the Blackcode formatter](https://github.com/psf/black)

### Problem

I love Black formatting because I agree with its formatting choices, but it does have one pathology: Excessive indenting on data structures

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

### Solution: Blacker!

When there is only one property (or list item, or parameter), then do not make a new line.

```python
schema = {"mappings": {"test": {"properties": {"one_value": {
    "type": "keyword", 
    "store": True,
}}}}}

```

## Development


Be sure you are in the `blacker` main directory

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    export PYTHONPATH=src:.
    export SKIP_AST_PRINT=true
    python -m unittest tests/test_black.py

...or Windows...

    python -m pip install virtualenv
    python -m virtualenv .venv             
    .venv\Scripts\activate
    pip install -r requirements.txt
    set PYTHONPATH=src;.
    set SKIP_AST_PRINT=true
    python -m unittest tests\test_black.py


