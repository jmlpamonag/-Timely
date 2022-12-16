import unittest
from dbHelper import dbHelper
from datetime import datetime

class dbHelperTest(unittest.TestCase):
    def test_getAll(self):
        query = "SELECT * FROM RECORD"

        self.assertEqual(dbHelper.getAll(), query)

    def test_getRecordsBetweenDates(self):
        fromDate = '2022/01/01'
        endDate = '2022/02/02'

        start = fromDate.split("/") 
        end = endDate.split("/")

        start = datetime(int(start[0]), int(start[1]), int(start[2]), 0, 0, 0)
        end = datetime(int(end[0]), int(end[1]), int(end[2]), 0, 0, 0)
        
        query = "SELECT * FROM RECORD WHERE startDate > '" + str(start) + "' AND endDate < '" + str(end) + "'"

        self.assertEqual(dbHelper.getRecordsBetweenDates(fromDate, endDate), query)
    
    def test_getPriority(self):
        query = "SELECT * FROM RECORD ORDER BY timeSpent DESC LIMIT 2"
        self.assertEqual(dbHelper.getPriority(), query)

        

if __name__ == "__main__":
    unittest.main()