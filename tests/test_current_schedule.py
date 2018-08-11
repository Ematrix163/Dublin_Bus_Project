from unittest import TestCase
import sys, os, shutil
import unittest

sys.path.append('/home/student')
from data_analytics.scripts.current_schedule import CurrentSchedule


class SelfDrivingCarTest(TestCase):

    def setUp(self):
        self.schedule = CurrentSchedule()

    # Test that a file actually downloads and returns a response code of 200
    def test_download(self):
        self.assertEqual(self.schedule.download(), 200)

    # Test that folders are actually created
    def test_create_directory(self):
        if os.path.isdir(self.schedule._download_URL_path):
            shutil.rmtree(self.schedule._download_URL_path, ignore_errors=True)
        self.schedule.create_directory()
        self.assertTrue(os.path.exists(self.schedule._download_URL_path))



if __name__ == '__main__':
    unittest.main()
