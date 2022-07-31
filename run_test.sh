#!/bin/bash

chmod +x run_test.sh
$PWD/python3-virtualvenv/bin/python -m unittest discover -v tests/
