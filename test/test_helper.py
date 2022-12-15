import unittest
from record import Record
from formatHelper import helper
from datetime import datetime

class HelperTest(unittest.TestCase):
    def test_formatDate(self):
        date = '2022/09/23'
        time = '09:30'
        self.assertEqual(helper.formatDate(date, time), datetime.strptime('2022-09-23 09:30:00', '%Y-%m-%d %H:%M:%S'))

    def test_formatTasl(self):
        task = "'Studied Java'"
        self.assertEqual(helper.formatTask(task), "Studied Java")

    def test_formatTag(self):
        tag = ":STUDY"
        self.assertEqual(helper.formatTag(tag), "STUDY")

    def test_getTimeSpent(self):
        timeSpent = 1800
        record = Record("2022/09/12", "09:30", "10:00", "'java'", ":STUDY")
        self.assertEqual(helper.getTimeSpent(record.startDate, record.endDate), timeSpent)

if __name__ == "__main__":
    unittest.main()