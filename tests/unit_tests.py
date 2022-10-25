import unittest
import random
import numpy as np
import data_processor as dp
import os
import pandas as pd


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        """ Set up for unit testing by creating toy data
        """
        arr = [[1,2,3],[4,5,6]]
        np.savetxt('test1.data', arr, delimiter = ',')
        pd.DataFrame(arr).to_csv('test2.csv', index = False)

    @classmethod
    def tearDownClass(cls):

        """ Tear down unit testing toy data
        """
        os.remove('test1.data')
        os.remove('test2.csv')

    def test_get_random_matrix(cls):

        """ Unit tests for get_random_matrix() function
        """
        
        # positive tests:
        result_df = dp.get_random_matrix(2,3)
        cls.assertEqual(result_df.shape, (2,3))
        result_df = dp.get_random_matrix(3,4)
        cls.assertEqual(result_df.shape, (3,4))

        # negative tests:
        result_df = dp.get_random_matrix(5,6)
        cls.assertNotEqual(result_df.shape, (3, 4))
        
        # error raising tests
        cls.assertRaises(TypeError, dp.get_random_matrix, 'one', 'two')
        cls.assertRaises(TypeError, dp.get_random_matrix, 1.5, 2.5)
        cls.assertRaises(ValueError, dp.get_random_matrix, -1, 2)

    def test_get_file_dimensions(cls):

        """ Unit tests for get_file_dimensions() function
        """
        
        # positive tests:
        cls.assertEqual(dp.get_file_dimensions('iris.data'), (150, 5))
        cls.assertEqual(dp.get_file_dimensions('test1.data'), (2, 3))
        cls.assertEqual(dp.get_file_dimensions('test2.csv'), (2, 3))

        # negative tests:
        cls.assertNotEqual(dp.get_file_dimensions('test1.data'), (150, 5))
        
        # error raising tests
        cls.assertRaises(IsADirectoryError, dp.get_file_dimensions, './tests')
        cls.assertRaises(FileNotFoundError, dp.get_file_dimensions, 'testing.csv')

    def test_write_matrix_to_file(cls):

        """ Unit tests for write_matrix_to_file() function
        """

        # positive tests
        dp.write_matrix_to_file(2, 3, 'test_read1.csv')
        cls.assertEqual(dp.get_file_dimensions('test_read1.csv'), (2,3))
        os.remove('test_read1.csv')

        # negative tests
        dp.write_matrix_to_file(4, 5, 'test_read2.csv')
        cls.assertNotEqual(dp.get_file_dimensions('test_read.csv'), (3,3))
        os.remove('test_read2.csv')

        # error raising tests
        # cls.assertRaises(Exception, dp.write_matrix_to_file, 3, 4, 10)   
        cls.assertRaises(ValueError, dp.write_matrix_to_file, -1, 2, 'test_read3.csv')
