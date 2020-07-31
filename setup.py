# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from __future__ import unicode_literals
from setuptools import setup
setup(
    author='Various',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Environment :: Console","Intended Audience :: Developers","License :: OSI Approved :: MIT License","Operating System :: OS Independent","Programming Language :: Python","Programming Language :: Python :: 3.6","Programming Language :: Python :: 3.7","Programming Language :: Python :: 3.8","Programming Language :: Python :: 3 :: Only","Topic :: Software Development :: Libraries :: Python Modules","Topic :: Software Development :: Quality Assurance"],
    description='Blacker! Denser Black formatting',
    entry_points={"console_scripts":["black=black:patched_main","blackd=blackd:patched_main [d]","black-primer=black_primer.cli:main"]},
    include_package_data=True,
    install_requires=["aiohttp","aiohttp_cors","appdirs","attrs==18.1.0","click==6.5","dataclasses==0.6","mo-files","mo-json","mo-logs","mo-math","pathspec","regex==2020.1.8","toml==0.9.4","typed-ast==1.4.0"],
    license='MIT',
    long_description='\n# Blacker - Denser Black formatting\n\nThis is s a fork of [the Blackcode formatter](https://github.com/psf/black)\n\n### Problem\n\nI love Black formatting because I agree with its formatting choices, but it does have one pathology: Excessive indenting on data structures\n\n```python\nschema = {\n    "mappings": {\n        "test": {\n            "properties": {\n                "one_value": {\n                    "type": "keyword",\n                    "store": True,\n                }\n            }\n        }\n    }\n}\n```\n\n### Solution: Blacker!\n\nWhen there is only one property (or list item, or parameter), then do not make a new line.\n\n```python\nschema = {"mappings": {"test": {"properties": {"one_value": {\n    "type": "keyword", \n    "store": True,\n}}}}}\n\n```\n\n## Development\n\n\nBe sure you are in the `blacker` main directory\n\n    python -m venv .venv\n    source .venv/bin/activate\n    pip install -r requirements.txt\n    export PYTHONPATH=src:.\n    export SKIP_AST_PRINT=true\n    python -m unittest tests/test_black.py\n\n...or Windows...\n\n    python -m pip install virtualenv\n    python -m virtualenv .venv             \n    .venv\\Scripts\\activate\n    pip install -r requirements.txt\n    set PYTHONPATH=src;.\n    set SKIP_AST_PRINT=true\n    python -m unittest tests\\test_black.py\n\n\n',
    long_description_content_type='text/markdown',
    name='blacker',
    package_dir={"":"src"},
    packages=["blackd","black","blib2to3","blib2to3.pgen2"],
    url='https://github.com/klahnakoski/blacker',
    version='3.89.20213'
)