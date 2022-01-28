#!/usr/bin/env bash
cd ..
python setup.py install
cd tests
pythonw -m pytest -s
