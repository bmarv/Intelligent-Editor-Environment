import tkinter as tk
import Basic_Gui.Fileoperations as Fileoperations
from tkinter.filedialog import *
from tkinter import messagebox


class Window:

    def __init__(self):
        self.launchWindow()
        activeWindow= None
        text = None


    def launchWindow(self):
        fileOP = Fileoperations.Fileoperations()
        global activeWindow
        activeWindow = tk.Tk()
        activeWindow.title("Intelligent Editor Environment")
        # activeWindow.minsize(width=1920, height=1080)
        # activeWindow.maxsize(width=1920, height=1080)

        #set Textfield inside active Window
        global text
        text = tk.Text(activeWindow, width=50, height = 10)
        text.pack()


        # get Menubar for basic actions
        menubar = tk.Menu(activeWindow)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label='New File', command=self.newFile)
        fileMenu.add_command(label='Open', command=self.openFile)
        fileMenu.add_command(label='Save', command=self.saveFile)
        fileMenu.add_command(label='Save As', command=self.saveAs)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=activeWindow.quit)

        menubar.add_cascade(label='File', menu=fileMenu)
        activeWindow.config(menu=menubar)
        activeWindow.mainloop()
        print("Window closed")

    def getActiveWindow(self):
        return self.activeWindow

    #create new File
    def newFile(self):
        global filename
        filename = "Untitled"
        text.delete(0.0, END)
        print("new File \"Untitled\" created")

    # save changes in the file
    def saveFile(self):
        global filename
        t = text.get(0.0, END)
        # write into filename with 'w'
        f = open(filename, 'w')
        f.write(t)
        print("File ",filename," is saved")
        f.close

    # save File in custom path
    def saveAs(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
            print("Saving file ",f)
        except:
            messagebox.showerror(title="Saving Error", message="Unable to save file")
            print("Failed to save file")

    # open any file
    def openFile(self):
        f = askopenfile(mode='r')
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)
        print("File opened")