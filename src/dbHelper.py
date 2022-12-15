from datetime import datetime
from dateutil import tz
from datetime import timedelta

class dbHelper:
    insertQuery = """INSERT INTO RECORD(startDate, endDate, task, tag, timeSpent)
    VALUES (?, ?, ?, ?, ?)"""

    def getAll():
        return "SELECT * FROM RECORD"

    def getRecordByDate(date):
        dateString = date.split("/") 
     
        start = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), 0, 0, 0)
        end = start + timedelta(1)

        query = "SELECT * FROM RECORD WHERE startDate > '" + str(start) + "' AND endDate < '" + str(end) + "'"
        return query
    
    def getRecordByTask(task):
        query = "SELECT * FROM RECORD WHERE task like '%" + str(task) + "%'"
        return query

    def getRecordByTag(tag):
        query = "SELECT * FROM RECORD WHERE tag like '%" + str(tag) + "%'"
        return query

    def getRecordsBetweenDates(fromDate, endDate):
        start = fromDate.split("/") 
        end = endDate.split("/")
     
        start = datetime(int(start[0]), int(start[1]), int(start[2]), 0, 0, 0)
        end = datetime(int(end[0]), int(end[1]), int(end[2]), 0, 0, 0)
        
        query = "SELECT * FROM RECORD WHERE startDate > '" + str(start) + "' AND endDate < '" + str(end) + "'"
        return query

    def getPriority():
        query = "SELECT * FROM RECORD ORDER BY timeSpent DESC LIMIT 2"
        return query
