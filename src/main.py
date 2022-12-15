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


        if request[0] == "record":
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

    con.close()

    sys.exit("Exiting the program...")


if __name__ == "__main__":
  main()