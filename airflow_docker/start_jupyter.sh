#!/bin/bash
python port_check.py

jupyter notebook --no-browser --ip 0.0.0.0 --allow-root
