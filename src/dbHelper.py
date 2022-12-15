from datetime import datetime
from dateutil import tz
from datetime import timedelta

class dbHelper:
    insertQuery = """INSERT INTO RECORD(startDate, endDate, task, tag)
    VALUES (?, ?, ?, ?)"""

    def insert(record):
        return f"INSERT INTO RECORD VALUES ({record.startDate}, {record.endDate}, {record.task}, {record.tag})"

    def getAll():
        return "SELECT * FROM RECORD"

    def getRecordByDate(date):
        dateString = date.split("/") 
     
        start = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), 0, 0, 0)
        print(start)

        end = start + timedelta(1)
        print(end)

        query = "SELECT * FROM RECORD WHERE startDate > '" + str(start) + "' AND endDate < '" + str(end) + "'"
        print(query)
        return query
    
    def getRecordByTask(task):

        query = "SELECT * FROM RECORD WHERE task like '%" + str(task) + "%'"
        print(query)
        return query

    def getRecordByTag(tag):

        query = "SELECT * FROM RECORD WHERE tag like '%" + str(tag) + "%'"
        print(query)
        return query
