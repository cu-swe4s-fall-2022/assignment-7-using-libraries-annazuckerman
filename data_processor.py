import numpy as np
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt


def open_file(filename):
    """ Convenience function for catching file read errors.
        Parameters:
        ----------
        filename: (string) Path to file.

        Returns:
        -------

        file: Read-in file

    """
    if not os.path.exists(filename):
        raise FileNotFoundError('Input file ' + filename + ' could not be ' +
                                'found in directory ' + str(os.getcwd()))
    if os.path.isdir(filename):
        raise IsADirectoryError('Input file ' + filename + ' is a directory.')
    if not os.access(filename, os.R_OK):
        raise PermissionError('Input file ' + filename + ' is not readable.')
    if os.path.getsize(filename) == 0:
        raise FileNotFoundError('Input file must not be empty.')
    try:
        if filename.endswith('.csv'):
            file = pd.read_csv(filename)
        else:
            file = pd.read_csv(filename, header=None)

    except Exception:
        raise Exception('Could not open ' + filename +
                        ' for unkown reason, likely incorrect file format ' +
                        '(must be comma-separated)')

    return file


def get_random_matrix(num_rows, num_columns):
    """ Create a num_rows X num_columns matrix of floats randomly
        sampled from a uniform distribution over [0, 1).
        Parameters:
        ----------
        num_rows: (int) Number of rows in output matrix.
        num_columns: (int) Number of columns in output matrix.

        Returns:
        -------

        matrix: num_rows X num_columns matrix of randomly sampled floats

    """

    if type(num_rows) != int | type(num_columns) != int:
        raise TypeError('num_rows and num_columns must be integers.')
    if num_rows <= 0 | num_columns <= 0:
        raise ValueError('num_rows and num_columns must be postive integers.')
    rand_arr = np.random.rand(num_rows, num_columns)

    return rand_arr


def get_file_dimensions(file_name):
    """ Return the dimensions of a csv file.
        Parameters:
        ----------
        filename: (string) Path to comma-separated file.

        Returns:
        -------

        shape: (tuple of int) Shape of csv file

    """
    if not type(file_name) == str:
        raise TypeError('Input file name must be string.')

    file = open_file(file_name)
    shape = file.shape
    return shape


def write_matrix_to_file(num_rows, num_columns, file_name):
    """ Save input matrix to a csv file.
        Parameters:
        ----------
        filename: (string) Ouput file path.

        Returns:
        -------

        None

    """

    if not type(file_name) == str:
        raise TypeError('Output file name must be string.')

    matrix = get_random_matrix(num_rows, num_columns)

    df = pd.DataFrame(matrix)
    df.to_csv(file_name, index=False)
    return None


def make_box_plot(data, xticks, title, ylabel, xlabel, figsize,
                  output_file):
    """ Make a boxplot of input data.
        Parameters:
        ----------
        data: (array or list)
        xticks: (list of strings) labels for boxplot xticks.
        title: (string) Title of boxplots.
        ylabel: (string) Label for y-axis of boxplots.
        xlabel: (string) Label for x-axis of boxplots.
        figsize: (list of length 2) Size of output figure in Inches.
        output_file: (string) Path to save output image file.
        Returns:
        -------
        No returns.
        Output:
        ------
        Figure file is saved to output_file path.
    """

    try:
        fig = plt.figure(figsize=figsize, dpi=150)
    except Exception:
        print('Invalid figsize parameter.')
        sys.exit(1)
    ax = plt.gca()
    data = data[xticks]
    try:
        ax.boxplot(data)
    except Exception:
        print('Invalid data for plotting as boxplots.')
        sys.exit(1)
    try:
        ax.set_xticklabels(xticks, rotation='vertical')
    except Exception:
        print('Invalid xtick labels parameter.')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    try:
        plt.title(title)
    except Exception:
        print('Invalid plot title parameter.')
    try:
        fig.savefig(output_file, bbox_inches='tight')
        current_dir = os.getcwd()
        print('Output plot saved to: ' + current_dir + '/' + output_file)
    except Exception:
        print('Invalid output path to save plot.')


def make_scatter_plot(data, species, title, xcol, ycol, xlabel, ylabel,
                      figsize, output_file):
    """ Make a scatter plot of input data.
        Parameters:
        ----------
        data: (array or list)
        species: (list) List of species to plot
        title: (string) Title of boxplots.
        xcol: (string) Column name to plot on x-axis.
        ycol: (string) Column name to plot on y-axis.
        ylabel: (string) Label for y-axis of boxplots.
        xlabel: (string) Label for x-axis of boxplots.
        figsize: (list of length 2) Size of output figure in Inches.
        output_file: (string) Path to save output image file.
        Returns:
        -------
        No returns.
        Output:
        ------
        Figure file is saved to output_file path.
    """

    try:
        fig = plt.figure(figsize=figsize, dpi=150)
    except Exception:
        print('Invalid figsize parameter.')
        sys.exit(1)
    ax = plt.gca()
    try:
        for i in range(len(species)):
            species_mask = (data['name'] == species[i])
            plt.plot(data[species_mask][xcol], data[species_mask][ycol], '.',
                     label=species[i])
    except Exception:
        print('Invalid data for plotting as scatterplot.')
        sys.exit(1)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    try:
        plt.title(title)
    except Exception:
        print('Invalid plot title parameter.')
    try:
        fig.savefig(output_file, bbox_inches='tight')
        current_dir = os.getcwd()
        print('Output plot saved to: ' + current_dir + '/' + output_file)
    except Exception:
        print('Invalid output path to save plot.')


def make_multi_plot(data, species, title, xcol, ycol, scat_xlabel,
                    scat_ylabel, box_xlabel, box_ylabel, xticks, figsize,
                    output_file):
    """ Make a mulitpanet boxplot and scatter plot of input data.
        Parameters:
        ----------
        data: (array or list)
        species: (list) List of species to plot
        title: (string) Title of boxplots.
        xcol: (string) Column name to plot on x-axis.
        ycol: (string) Column name to plot on y-axis.
        scat_ylabel: (string) Label for y-axis of scatterplot.
        scat_xlabel: (string) Label for x-axis of scatterplot.
        box_ylabel: (string) Label for y-axis of boxplot.
        box_xlabel: (string) Label for x-axis of boxplot.
        xticks: (list of strings) labels for boxplot xticks.
        figsize: (list of length 2) Size of output figure in Inches.
        output_file: (string) Path to save output image file.
        Returns:
        -------
        No returns.
        Output:
        ------
        Figure file is saved to output_file path.
    """

    try:
        fig = plt.figure(figsize=figsize, dpi=150)
    except Exception:
        print('Invalid figsize parameter.')
        sys.exit(1)

    # add boxplots
    ax = fig.add_subplot(121)
    try:
        ax.boxplot(data[xticks])
    except Exception:
        print('Invalid data for plotting as boxplots.')
        sys.exit(1)
    try:
        ax.set_xticklabels(xticks, rotation='vertical')
    except Exception:
        print('Invalid xtick labels parameter.')
    plt.ylabel(box_ylabel)
    plt.xlabel(box_xlabel)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # add scatter plots
    ax = fig.add_subplot(122)
    try:
        for i in range(len(species)):
            species_mask = (data['name'] == species[i])
            plt.plot(data[species_mask][xcol], data[species_mask][ycol], '.',
                     label=species[i])
    except Exception:
        print('Invalid data for plotting as scatterplot.')
        sys.exit(1)
    plt.ylabel(scat_ylabel)
    plt.xlabel(scat_xlabel)
    plt.legend()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # add title
    try:
        plt.suptitle(title)
    except Exception:
        print('Invalid plot title parameter.')

    try:
        fig.savefig(output_file, bbox_inches='tight')
        current_dir = os.getcwd()
        print('Output plot saved to: ' + current_dir + '/' + output_file)
    except Exception:
        print('Invalid output path to save plot.')
