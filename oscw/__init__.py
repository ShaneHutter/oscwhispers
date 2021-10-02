#!/usr/bin/env python3
"""OSCW Package __init__
"""

from os.path    import exists

## Determine and load documentation
_docs_dir = "/usr/share/doc"
# README file
_README = None
if exists( f"{_docs_dir}/README.md" ):
    _README= open( f"{_docs_dir}/README.md" ).read()
elif exists( "../README.md" ):
    _README= open( "../README.md" ).read()
# LICENSE file
_LICENSE = None
if exists( f"{_docs_dir}/LICENSE" ):
    _README= open( f"{_docs_dir}/LICENSE" ).read()
elif exists( "../LICENSE" ):
    _LICENSE = open( "../LICENSE.md" ).()

## Setup variables for installation/packaging
_data_files = [
    (   # Executables
        "/usr/bin",
        [
            "oscwhispers",
            ],
        ),
    (   # Documentation
        _docs_dir,
        [
            "README.md",
            "LICENSE",
            ],
        ),
    (   # Config
        "/etc",
        [
            "conf/oscwhispers.yml",
            ],
        ),
    ]

_packages = [ "oscw" ]

_setup = {
    "name": "oscwhispers",
    "version": "0.0.1",
    "author": "Shane Hutter",
    "authot_email": "shane@intentropycs.com",
    "description": "An Open Sound Control proxying server",
    "long_description": _README,
    "license": _LICENSE,
    "packages": _packages,
    "data_files": _data_files,
    }