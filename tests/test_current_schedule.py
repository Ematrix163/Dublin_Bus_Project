from unittest import TestCase
import sys

sys.path.append('/home/student')
from data_analytics.scripts.current_schedule.py import CurrentSchedule
print(sys.path)


class SelfDrivingCarTest(TestCase):

    def setUp(self):
        self.schedule = CurrentSchedule()

    def test1(self):
        self.assertRaises(SomeCoolException, self.schedule.create_directory())