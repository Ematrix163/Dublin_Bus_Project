import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from data_analytics.prediction_model.NN_model import NeuralNetworkModel

class NeuralNetworkModel(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    @classmethod
    def setUpClass(cls):
        """ SetUp """
        test_input_dir = '/home/student/data_analytics/prediction_model/clean_files/'
        test_file_name = '25_1.csv'
        try:
            data = pd.read_csv(test_input_dir + test_file_name, sep = ',')
        except IOError:
            print('Cannot Open File')
        cls.fixture = data

    def test_dataFrame_constrcuted_as_expected(self):
        """ Test that the dataframe read in equals what you expect"""
        foo = pd.DataFrame()
        assert_frame_equal(self.fixture, foo)


if __name__ == '__main__':
    unittest.main()