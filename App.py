from Tkinter import *
from tkFileDialog   import askopenfilename

class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)

        fileMenu.add_command(label="New", underline=1, command=self.NewFile)
        fileMenu.add_command(label="Open...", underline=1, command=self.OpenFile)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)

        helpMenu = Menu(self, tearoff=False)
        self.add_cascade(label="Help",underline=0, menu=helpMenu)

        helpMenu.add_command(label="About...", underline=1, command=self.About)
    def NewFile(self):
        print "New File!"
    def OpenFile(self):
        name = askopenfilename()
        print name
    def About(self):
        print "This is a simple example of a menu"
    def quit(self):
        sys.exit(0)

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        menubar = MenuBar(self)
        master.config(menu=menubar)

root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(600, 480))

app = Application(master=root)

app.mainloop()
root.destroy()