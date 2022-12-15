from datetime import datetime

class helper: 

    def formatDate(date, time):
        hours = 0
        minutes = 0

        dateString = date.split("/") 

        timeString = time.split(":")  
        if "PM" in time:
            hours = int(timeString[0]) + 12
            minutes = int(timeString[1].replace("PM", ""))
        elif "AM" in time:
            hours = int(timeString[0])
            minutes = int(timeString[1].replace("AM", ""))
        else: 
            hours = int(timeString[0])
            minutes = int(timeString[1])


        print(dateString)
        print(timeString)   

        dt = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), hours, minutes, 0, 0)
        
        return dt

    def formatTask(task):
        fTask = str(task)
        print(fTask)

        return fTask.replace("\'", "")

    def formatTag(tag):
        fTag = str(tag)
        print(fTag)

        return fTag.replace(":", "")