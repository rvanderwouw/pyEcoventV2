#!/bin/bash
#

alias python=python3.10

python setup.py build; 
python setup.py sdist;
sudo python setup.py install
