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
        df = pd.DataFrame(arr)
        df.to_csv('test.csv', index = False)

    @classmethod
    def tearDownClass(cls):

        """ Tear down unit testing toy data
        """
        os.remove('test.csv')

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

        """ Unit tests for get_random_matrix() function
        """
        
        # positive tests:
        cls.assertEqual(dp.get_file_dimensions('iris.data'), (150, 5))

        # negative tests:
                
        # error raising tests

    def test_write_matrix_to_file(cls):

        """ Unit tests for get_random_matrix() function
        """

        # postive tests

        # negative tests

        # error raising tests
        cls.assertRaises(Exception, dp.write_matrix_to_file, '')      