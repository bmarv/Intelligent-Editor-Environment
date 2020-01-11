from tkinter.filedialog import *
from tkinter import messagebox
import tkinter as tk
import Basic_Gui.Window as win

#NOT RELEVANT ANY MORE
#TODO: use class for fileoperations instead of having one big window class
class Fileoperations:
    def __init__(self):
        filename = None
        Text = win.Text

    def newFile(self):
        global filename
        filename = "Untitled"
        Text.delete(0.0, END)
        print("new File \"Untitled\" created")

    # save changes in the file
    def saveFile(self):
        global filename
        t = Text.get(0.0, END)
        # write into filename with 'w'
        f = open(filename, 'w')
        f.write(t)
        print("File \"filename\" is saved")
        f.close

    def saveAs(self, Text):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = Text.get(0.0, END)
        try:
            f.write(t.rstrip())
            print("Saving file ...")
        except:
            messagebox.showerror(title="Saving Error", message="Unable to save file")
            print("Failed to save file")

    def openFile(self, Text):
        f = askopenfile(mode='r')
        t = f.read()
        Text.delete(0.0, END)
        Text.insert(0.0, t)
        print("File opened")


# menubar = Menu(activeWindow)
        # activeWindow.config(menu=menubar)
        # filemenu = Menu(menubar)
        # # filemenu.add_command(label="New File", command=fileOP.newFile(text))
        # filemenu.add_command(label="Open File", command=fileOP.openFile(text))
        # # filemenu.add_command(label="Save", command=fileOP.saveFile(text))
        # # filemenu.add_command(label="Save As", command=fileOP.saveAs(text))
        # filemenu.add_separator()
        # filemenu.add_command(label="Quit", command=activeWindow.quit())
        # menubar.add_cascade(label="File", menu=filemenu)