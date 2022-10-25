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
        raise FileNotFoundError('Input file ' + filename + ' could not be found in directory ' + str(os.getcwd()))
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
            file = pd.read_csv(filename, header = None)

    except Exception:
        raise Exception('Could not open ' + filename + ' for unkown reason, ' +
              'likely incorrect file format (must be comma-separated)')

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
    """ Return the dimensions of a csv file.
        Parameters:
        ----------
        filename: (string) Ouput file path.

        Returns:
        -------

        None

    """   
  #  if not type(file_name) == str:
  #      print('Output file name must be string.')
  #      sys.exit(1)
            
    matrix = get_random_matrix(num_rows, num_columns)

    df = pd.DataFrame(matrix)
    df.to_csv(file_name, index = False)
    return None