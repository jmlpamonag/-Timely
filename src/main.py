# Imports
import sys
import sqlite3

from datetime import datetime
from dbHelper import dbHelper
from record import Record


# Client Code  
def main():

    con = sqlite3.connect("timely.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS RECORD (startDate datetime, endDate datetime, task text, tag text)")

    while True:
        userInput = str(input("Command or [q] to quit:"))

        if userInput.lower() == "q":
            break
        
        if userInput == "":
            print("Please try again")
            continue

        request = userInput.split()
        print(request)

        length = request.__len__()
        print(f'Size: {length}')

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

            print(f"TASK: {task}")
            print(f"TAG: {tag}")

            if request[1] == "today":
                dt = datetime.today().strftime("%Y/%m/%d")
            else: 
                dt = request[1]
                
            print(f"DATE: {dt}")

            record = Record(dt, request[2], request[3], task.strip(), tag.strip())
            record.toString()

            cur.execute(dbHelper.insertQuery, [record.startDate, record.endDate, record.task, record.tag])
            

            # TEST INSERT
            res = cur.execute(dbHelper.getAll())
            data = res.fetchall()
            print(data)
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
                print(data)
            elif "'" in request[1]:
                if length > 2:
                    for i in range(length):
                        if i > 0:
                            print(request[i])
                            task = task + request[i].replace("'", "") + " "
                else:
                    task = request[1].replace("'", "")

                task = task.strip()

                res = cur.execute(dbHelper.getRecordByTask(task))
                data = res.fetchall()
                print(data)
            elif ":" in request[1]:
                tag = request[1].replace(":", "")
                res = cur.execute(dbHelper.getRecordByTag(tag.upper()))
                data = res.fetchall()
                print(data)
            else:
                print("Something went wrong. Please try again.")



        else:
            print("Feature does not exist. Please try again.")

    con.close()

    sys.exit("Exiting the program...")


if __name__ == "__main__":
  main()