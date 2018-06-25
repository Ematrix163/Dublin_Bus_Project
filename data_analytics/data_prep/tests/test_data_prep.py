
import sys, os
import unittest
sys.path.append('..')

print(sys.path)


from data_prep import DataPrep

# check = DataPrep(trips_2016, trips_dtypes, 'summary_trips_2016')
# print(check)

def setUpModule():
    print("setup module")


def tearDownModule():
    print("teardown module")


if __name__ == '__main__':
    unittest.main()