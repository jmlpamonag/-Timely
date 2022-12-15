import datetime
from dateutil import tz
from datetime import timedelta

class dbHelper:
    insertQuery = """INSERT INTO RECORD(startDate, endDate, task, tag)
    VALUES (?, ?, ?, ?)"""

    def insert(record):
        return f"INSERT INTO RECORD VALUES ({record.startDate}, {record.endDate}, {record.task}, {record.tag})"

    def getAll():
        return "SELECT * FROM RECORD"

    def getToday():
        # TO DO:
        today = datetime.datetime.date()
        print(today)
        
        start = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc())
        print(start)

        end = start + timedelta(1)

        return "SELECT * FROM RECORD WHERE STARTDATE > {start} AND ENDDATE < {end}"
