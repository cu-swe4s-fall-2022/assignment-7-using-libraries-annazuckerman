#!/usr/bin/bash

set -e  # stop on error
set -u  # raise error if variable is unset
set -o pipefail  # fail if any prior step failed

# run pycodestyle on new python scripts used in unit and functional testing
pycodestyle data_processor.py
pycodestyle plotter.py

# run unit testing
python -m unittest tests/unit_tests.py

# run functional testing
bash tests/functional_tests.sh