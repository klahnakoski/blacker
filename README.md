
# More Black! - Denser Black formatting

This is s a fork of [the Black code formatter](https://github.com/psf/black)

### Problem

I love Black formatting because I agree with its formatting choices, but it does have one pathology: [Excessive indenting on data structures](https://github.com/psf/black/issues/626)

Here is an example of Black formatting; many lines are wasted on lonely brackets:  

```python
my_method(
    [
        {
            "name": "a",
            "value": 42
        }
    ]
)
```

## Solution: More Black!

When there is only one property (or list item, or parameter), then do not make a new line.

```python
my_method([{
    "name": "a",
    "value": 42
}])
```


## Usage

Please [read the official Black documentation at time of fork](https://github.com/psf/black/blob/537ea8df35b1004bdb228b483907fb5dd92e5257/README.md#usage)

    pip install mo-black


## More about this fork

The `right_hand_split()` function has [additional code](https://github.com/klahnakoski/mo-black/blob/25e1fd648530279dffbf701721df76d52213651a/src/black/__init__.py#L4786) that attempts to identify "simple" structures inside brackets. If it is simple, then block the multiline formatting and, recurse into deeper brackets to find something more complicated to split.

## Development

Be sure you are in the `mo-black` main directory

Setup virtual environment

    python -m venv .venv
    source .venv/bin/activate

Install requirements 

    pip install -r requirements.txt
    pip install -r tests/requirements.txt

Set some environment variables

    export PYTHONPATH=src:.
    export SKIP_AST_PRINT=true

Run the tests 

    python -m unittest tests/test_black.py

Here is the same for Windows...

    c:\Python38\python -m pip install virtualenv
    c:\Python38\python -m virtualenv .venv             
    .venv\Scripts\activate
    pip install -r requirements.txt
    pip install -r tests\requirements.txt
    set PYTHONPATH=src;.
    set SKIP_AST_PRINT=true
    python -m unittest tests\test_black.py


### Development Installation

You can install `mo-black` from the main directory

    python.exe -m pip install .
