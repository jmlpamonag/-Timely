import unittest
from record import Record
from dbHelper import dbHelper

class dbHelperTest(unittest.TestCase):
    def test_insert(self):
        record = Record("2022/09/23", "09:30", "10:30", "'Studied Java'", ":STUDY")
        query = f"INSERT INTO RECORD VALUES ({record.startDate}, {record.endDate}, {record.task}, {record.tag})"

        self.assertEqual(dbHelper.insert(record), query)

    def test_getAll(self):
        query = "SELECT * FROM RECORD"

        self.assertEqual(dbHelper.getAll(), query)
        

if __name__ == "__main__":
    unittest.main()