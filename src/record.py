from formatHelper import helper 

class Record:
    startDate = ""
    endDate = ""
    task = ""
    tag = ""
    timeSpent = 0

    def __init__(self, date, fromTime, toTime, task, tag):
            self.startDate = helper.formatDate(date, fromTime)
            self.endDate = helper.formatDate(date, toTime)
            self.task = helper.formatTask(task)
            self.tag = helper.formatTag(tag)
            self.timeSpent = helper.getTimeSpent(self.startDate, self.endDate)

    def toString(self):
        print(f"Record: {self.startDate}, {self.endDate}, {self.task}, {self.tag}")

    def getTimeSpent(self):
        duration = self.endDate - self.startDate
        duration_s = duration.total_seconds()

        self.timeSpent = int(duration_s)
        

