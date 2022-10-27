Anna Zuckerman\
CSCI6118\
HW7 Repository

## Repository Summary

This repository contains a python file called `plotter.py` which reads an\
input data file and creates plots to vizualize the data. For the data file\
`iris.data`, this script produces a boxplot of sepal width, sepal length,\
petal width, and petal length; a scatter plot of sepal width against sepal\
length, and a multipanel plot containing both the boxplot and the scatter\
plot. The script must be passed an input file name and the intended names\
of output files for each plot.

In addition, this repository contains a library of auxiliary functions\
called `data_processor.py`. This library includes a function called\
`get_random_matrix` which creates a matrix a specified size of\
floats randomly sampled from a uniform distribution from 0 (inclusive\
to 1 (exclusive). `get_file_dimensions` returns the dimensions of a\
specified csv file.  `write_matrix_to_file` saves an input matrix to a\
csv file. Three additional functions, `make_box_plot`, `make_scatter_plot`\
and `make_multi_plot` are called in `plotter.py` to make the output plots.

This repository also contains a script `unit_tests.py` for unit testing\
and a script `functional_tests.sh for` functional testng. Unit and functional\
testing are performed on all funtions in `data_processor.py`.\
These tests are run in the `run_tests.sh` shell script.\
In addition, the tests are run on commits and pull requests to\
main using continuous integration.

## Installation
This package will run with the standard python library.

## Usage

The Iris data plots can be made using the following syntax:\
`python plotter.py`\
    `--filename [INPUT_FILE]`\
    `--box_outfile [BOX_OUTPUT_FILE]`\
    `--scatter_outfile [SCATTER_OUTPUT_FILE]`\
    `--multipanel_outfile [MULTI_OUTPUT_FILE]``

The arguments are:\
`--filename`: (string) Filepath to Iris data.\
`--box_outfile`: (string) Output file name to save boxplot.\
`--scatter_outfile`: (string) Output file name to save scatterplot.\
`--multipanel_outfile`: (string) Output file name to save multipanel plot.

## Input File

The expected input Iris data file is a csv or text file with columns\
corresponding to measurements of the Iris flower. 
THe file must be comma delimited.

## Examples
To produce output plots for Iris data:\
`python plotter.py`\
    `--filename iris.data \
    `--box_outfile iris_boxplot.png \
    `--scatter_outfile petal_width_v_length_scatter.png \
    `--multipanel_outfile multi_panel_figure.png`\
    
Output of the above:\
See output plots in the `example_outputs` directory.
