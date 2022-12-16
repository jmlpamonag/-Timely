# Imports
import sys
import sqlite3

from datetime import datetime
from dbHelper import dbHelper
from record import Record
from formatHelper import helper


# Client Code  
def main():

    con = sqlite3.connect("timely.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS RECORD (startDate datetime, endDate datetime, task text, tag text, timeSpent int)")

    while True:
        print("************** TIMELY **************")
        userInput = str(input("Please enter a request or [q] to quit:"))

        if userInput.lower() == "q":
            break
        
        if userInput == "":
            print("Please try again")
            continue

        request = userInput.split()
        length = request.__len__()

        task = ""
        tag = ""
        dt = ""

        if request[0] == "record":
            if(length > 6):
                tag = request[length -1]
                for i in range(length - 1):
                    if i > 3:
                        print(request[i])
                        task = task + request[i].replace("'", "") + " "
            else:
                task = request[4]
                tag = request[5]


            if request[1] == "today":
                dt = datetime.today().strftime("%Y/%m/%d")
            else: 
                dt = request[1]
                
            record = Record(dt, request[2], request[3], task.strip(), tag.strip())
            record.toString()

            cur.execute(dbHelper.insertQuery, [record.startDate, record.endDate, record.task, record.tag, record.timeSpent])
            print("Added the task!")
        elif request[0] == "query":
            if(length < 2):
                print("Invalid query request. Please try again")
                break

            if request[1] == "today" or "/" in request[1]:
                if request[1] == "today":
                    dt = datetime.today().strftime("%Y/%m/%d")
                else: 
                    dt = request[1]

                print(dt)
                res = cur.execute(dbHelper.getRecordByDate(dt))
                data = res.fetchall()
                helper.showResults("Activites from " + dt, data)
            elif "'" in request[1]:
                if length > 2:
                    for i in range(length):
                        if i > 0:
                            task = task + request[i].replace("'", "") + " "
                else:
                    task = request[1].replace("'", "")

                task = task.strip()

                res = cur.execute(dbHelper.getRecordByTask(task))
                data = res.fetchall()
                helper.showResults("Activites associated with " + task, data)
            elif ":" in request[1]:
                tag = request[1].replace(":", "")
                res = cur.execute(dbHelper.getRecordByTag(tag.upper()))
                data = res.fetchall()
                helper.showResults("Activites associated with the tag" + tag, data)
            else:
                print("Something went wrong. Please try again.")
        elif request[0] == "report":
            if length != 3:
                print("Invalid report request. Please try again")
                continue

            res = cur.execute(dbHelper.getRecordsBetweenDates(request[1], request[2]))
            data = res.fetchall()
            helper.showResults("Activities between" + str(request[1]) + " and " + str(request[2]), data)
        elif request[0] == "priority":
            res = cur.execute(dbHelper.getPriority())
            data = res.fetchall()
            helper.showResults("Top 2 Activites", data)
        else:
            print("Feature does not exist. Please try again.")

    con.close()

    sys.exit("Thank you for using Timely! Exiting the program...")


if __name__ == "__main__":
  main()