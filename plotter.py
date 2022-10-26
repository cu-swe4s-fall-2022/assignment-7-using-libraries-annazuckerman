import matplotlib.pyplot as plt
import pandas as pd
import data_processor as dp
import argparse


def main():
    """ Create _______.
    Parameters
    ----------
    No input parameters; paramters are passed from
    command line call using argparse.
    Returns
    -------
    No returned output.
    Output
    ------
    Saves output plots ______.
    """

    # parse arguments
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--filename', dest='filename',
                        type=str,
                        help='File to read input data from.',
                        required=True)
    parser.add_argument('--box_outfile', dest='box_outfile',
                        type=str,
                        help='Output file name to save boxplot.',
                        required=True)
    parser.add_argument('--scatter_outfile', dest='scatter_outfile',
                        type=str,
                        help='Output file name to save scatterplot.',
                        required=True)
    parser.add_argument('--multipanel_outfile', dest='multipanel_outfile',
                        type=str,
                        help='Output file name to save multipanelplot.',
                        required=True)
    args = parser.parse_args()
    filename = str(args.filename)
    box_outfile = str(args.box_outfile)
    scatter_outfile = str(args.scatter_outfile)
    multipanel_outfile = str(args.multipanel_outfile)

    # read in file
    file = dp.open_file(filename)
    file.columns = ['sepal_width', 'sepal_length', 'petal_width',
                    'petal_length', 'name']
    measurements = ['sepal_width', 'sepal_length', 'petal_width',
                    'petal_length']
    species = list(set(file['name']))

    # make boxplots
    dp.make_box_plot(file,
                     measurements,
                     'Iris Data Boxplot', 'Value [cm]', 'Measurement Type',
                     [10, 5],
                     box_outfile)

    # make scatterplots
    dp.make_scatter_plot(file, species,
                         'Iris Data Scatterplot', 'sepal_length',
                         'sepal_width', 'Sepal length [cm]',
                         'Sepal width [cm]', [10, 5],
                         scatter_outfile)

    # make multipanel plots
    dp.make_multi_plot(file, species, 'Iris Multi-panel Plot', 'sepal_length',
                       'petal_width', 'Sepal length [cm]', 'Sepal width [cm]',
                       'Value [cm]', 'Measurement Type',
                       measurements, [20, 10], multipanel_outfile)


if __name__ == "__main__":
    main()
