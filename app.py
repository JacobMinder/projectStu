import tkinter as tk

screenWidth = 0
screenHeight = 0

class App:
    def __init__(self):
        self.root = tk.Tk()

        screenWidth= self.root.winfo_screenwidth()
        screenHeight= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (screenWidth, screenHeight))

        self.main_screen = tk.Frame(self.root)
        
        self.main_screen.pack()
        
        self.root.mainloop()

class Semester:
    def __init__(self, startDate, endDate, schedule, classes, breaks):
        self.startDate = startDate
        self.endDate = endDate
        self.schedule = schedule
        self.classes = classes
        self.breaks = breaks

class Class:
    def __init__(self, subject, startDate, endDate, schedule, teacher, location):
        self.subject = subject
        self.startDate = startDate
        self.endDate = endDate
        self.schedule = schedule
        self.teacher = teacher
        self.location = location

class Breaks:
    def __init__(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate

class Tasks:
    def __init__(self, assignedDate, dueDate, title, classs, details):
        self.assignedDate = assignedDate
        self.dueDate = dueDate
        self.title = title
        self.classs = classs
        self.details = details

class Exam:
    def __init__(self, date, title, classs, details,length,seat):
        self.date = date
        self.title = title
        self.classs = classs
        self.details = details
        self.length = length
        self.seat = seat
        
if __name__ == '__main__':
    app = App()
