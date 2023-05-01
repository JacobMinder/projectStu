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

if __name__ == '__main__':
    app = App()
