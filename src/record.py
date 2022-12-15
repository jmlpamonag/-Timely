from formatHelper import helper 

class Record:
    startDate = ""
    endDate = ""
    task = ""
    tag = ""

    def __init__(self, date, fromTime, toTime, task, tag):
            self.startDate = helper.formatDate(date, fromTime)
            self.endDate = helper.formatDate(date, toTime)
            self.task = helper.formatTask(task)
            self.tag = helper.formatTag(tag)

    def toString(self):
        print(f"Record: {self.startDate}, {self.endDate}, {self.task}, {self.tag}")