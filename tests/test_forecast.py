import unittest
import forecast
from forecast import Forecast



class TestForecast(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

     # method to test that forecast.py's method 'connecting_method' returns an instance of class Forecast
    def test_connecting_method(self):
        self.testinstance = forecast.connecting_method()
        self.assertIsInstance(self.testinstance, Forecast)


    def test_api_request(self):
        """Tests api request to see if it returns a dictionary (json file from api request is turned into dictionary in api_request function)"""
        self.testinstance = forecast.connecting_method()
        self.dict = self.testinstance.api_request()
        self.assertTrue(type(self.dict) == dict)





if __name__ == '__main__':
    unittest.main()
