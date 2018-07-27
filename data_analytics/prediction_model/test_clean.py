import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from clean import CleanFile
'''
class mockInputFilePath():
    def find_input_file_path(self):
        return '/home/student/data_analytics/bus_lines/single_bus_line/bus_25_merge.csv'


class mockOutputPath():
    def find_output_path(self):
        return '/home/student/data_analytics/prediction_model/clean_files'

class mockWeatherFile():
    def find_weatherFile(self):
       return '/home/student/data/weather/2017weatherClean.csv'


class mock_direction():
    def find_direction(self):
        return 1
'''


class CleanFile(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    @classmethod
    def setUpClass(cls):
        """ SetUp """
        test_input_dir = '/home/student/data_analytics/prediction_model/extracted/'
        test_file_name = 'bus_25B_merge.csv'
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
