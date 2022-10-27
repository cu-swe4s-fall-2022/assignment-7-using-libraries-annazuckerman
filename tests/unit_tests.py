import unittest
import random
import numpy as np
import os
import pandas as pd
import sys
sys.path.append('../')
import data_processor as dp  # nopep8


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        """ Set up for unit testing by creating toy data
        """
        arr = [[1, 2, 3], [4, 5, 6]]
        np.savetxt('test1.data', arr, delimiter=',')
        pd.DataFrame(arr).to_csv('test2.csv', index=False)

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
        result_df = dp.get_random_matrix(2, 3)
        cls.assertEqual(result_df.shape, (2, 3))
        result_df = dp.get_random_matrix(3, 4)
        cls.assertEqual(result_df.shape, (3, 4))

        # negative tests:
        result_df = dp.get_random_matrix(5, 6)
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
        cls.assertRaises(IsADirectoryError, dp.get_file_dimensions, '../tests')
        cls.assertRaises(FileNotFoundError, dp.get_file_dimensions,
                         'testing.csv')

    def test_write_matrix_to_file(cls):

        """ Unit tests for write_matrix_to_file() function
        """

        # positive tests
        dp.write_matrix_to_file(2, 3, 'test_read1.csv')
        cls.assertEqual(dp.get_file_dimensions('test_read1.csv'), (2, 3))
        os.remove('test_read1.csv')

        # negative tests
        dp.write_matrix_to_file(4, 5, 'test_read2.csv')
        cls.assertNotEqual(dp.get_file_dimensions('test_read2.csv'), (2, 3))
        os.remove('test_read2.csv')

        # error raising tests
        cls.assertRaises(Exception, dp.write_matrix_to_file, 3, 4, 10)
        cls.assertRaises(ValueError, dp.write_matrix_to_file, -1, 2,
                         'test_read3.csv')

    def test_make_scatter_plot(cls):

        # positive tests
        if os.path.isfile('test_scatter.png'):
            os.remove('test_scatter.png')
        file = pd.read_csv('iris.data', header=None)
        file.columns = ['sepal_width', 'sepal_length', 'petal_width',
                        'petal_length', 'name']
        dp.make_scatter_plot(file,
                             ['Iris-setosa', 'Iris-virginica',
                              'Iris-versicolor'],
                             'Iris Data Scatterplot', 'sepal_length',
                             'sepal_width', 'Sepal length [cm]',
                             'Sepal width [cm]', [10, 5],
                             'test_scatter.png')
        cls.assertTrue(os.path.isfile('test_scatter.png'))
        os.remove('test_scatter.png')

        # error catching tests
        cls.assertRaises(Exception, dp.make_scatter_plot, 'iris.data',
                         ['Iris-setosa', 'Iris-virginica',
                          'Iris-versicolor'],
                         'Iris Data Scatterplot', 'sepal_length',
                         'sepal_width', 'Sepal length [cm]',
                         'Sepal width [cm]', ['ten', 'five'],
                         'test_scatter.png')

    def test_make_box_plot(cls):

        # positive tests
        if os.path.isfile('test_box.png'):
            os.remove('test_box.png')
        file = pd.read_csv('iris.data', header=None)
        file.columns = ['sepal_width', 'sepal_length', 'petal_width',
                        'petal_length', 'name']
        dp.make_box_plot(file,
                         ['sepal_width', 'sepal_length', 'petal_width',
                          'petal_length'],
                         'Iris Data Boxplot', 'Value [cm]',
                         'Measurement Type',
                         [10, 5],
                         'test_box.png')
        cls.assertTrue(os.path.isfile('test_box.png'))
        os.remove('test_box.png')

        # error catching tests
        cls.assertRaises(Exception, dp.make_box_plot, file,
                         ['sepal_width', 'sepal_length', 'petal_width',
                          'petal_length'],
                         'Iris Data Boxplot', 'Value [cm]',
                         'Measurement Type', ['ten', 'five'],
                         'test_box.png')

    def test_make_multi_plot(cls):

        # positive tests
        if os.path.isfile('test_multi.png'):
            os.remove('test_multi.png')
        file = pd.read_csv('iris.data', header=None)
        file.columns = ['sepal_width', 'sepal_length', 'petal_width',
                        'petal_length', 'name']
        dp.make_multi_plot(file, ['Iris-setosa', 'Iris-virginica',
                                  'Iris-versicolor'],
                           'Iris Multi-panel Plot', 'sepal_length',
                           'petal_width', 'Sepal length [cm]',
                           'Sepal width [cm]', 'Value [cm]',
                           'Measurement Type',
                           ['sepal_width', 'sepal_length', 'petal_width',
                            'petal_length'], [20, 10], 'test_multi.png')
        cls.assertTrue(os.path.isfile('test_multi.png'))
        os.remove('test_multi.png')

        # error catching tests
        cls.assertRaises(Exception, dp.make_multi_plot, 'iris.data',
                         ['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'],
                         'Iris Multi-panel Plot', 'sepal_length',
                         'petal_width', 'Sepal length [cm]',
                         'Sepal width [cm]', 'Value [cm]', 'Measurement Type',
                         ['sepal_width', 'sepal_length', 'petal_width',
                          'petal_length'], ['ten', 'five'], 'test_multi.png')
