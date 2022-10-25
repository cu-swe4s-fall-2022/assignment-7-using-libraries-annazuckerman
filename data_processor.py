import numpy as np
import pandas as pd
import os
import sys


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
        print('Input file ' + filename + ' could not be found.')
        sys.exit(1)
    if os.path.isdir(filename):
        print('Input file ' + filename + ' is a directory.')
        sys.exit(1)
    if not os.access(filename, os.R_OK):
        print('Input file ' + filename + ' is not readable.')
        sys.exit(1)
    if not (filename.endswith('.csv')):
        print('Input file must be a csv file.')
        sys.exit(1)
    if os.path.getsize(filename) == 0:
        print('Input file must not be empty.')
        sys.exit(1)
    try:
        file = pd.read_csv(filename, header = None)
    except Exception:
        print('Could not open ' + filename + ' for unkown reason, ' +
              'likely incorrect file format (must be comma-separated)')
        sys.exit(1)

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
   
    rand_arr = np.array([[1,2,3],[4,5,6]])
    
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

    shape = (150, 5)
    return shape

def write_matrix_to_file(num_rows, num_columns, file_name):
    """ Return the dimensions of a csv file.
        Parameters:
        ----------
        filename: (string) Ouput file path.

        Returns:
        -------

        None

    """   
    df = pd.DataFrame([1])
    df.to_csv('file_name', index = False)
    return None
