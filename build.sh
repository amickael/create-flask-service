#!/bin/bash

# Remove old files
rm -r build; rm -r *.egg-info; rm -r dist

# Build
python3 setup.py sdist bdist_wheel

# Upload
python3 -m twine upload dist/*