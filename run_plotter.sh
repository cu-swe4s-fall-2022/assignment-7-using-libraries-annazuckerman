#!/usr/bin/bash

set -e  # stop on error
set -u  # raise error if variable is unset
set -o pipefail  # fail if any prior step failed

python plotter.py \
    --filename iris.data \
    --box_outfile iris_boxplot.png \
    --scatter_outfile petal_width_v_length_scatter.png \
    --multipanel_outfile multi_panel_figure.png
