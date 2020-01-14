from tkinter.filedialog import *
from tkinter import messagebox
# import tkinter as tk
import Basic_Gui.Window as Window
import Main

class Fileoperations:
    def __init__(self):
        global filename
        global curDir
        global filePath

    # create new File
    def newFile(self, extText):
        global filename
        filename = "Untitled.txt"
        extText.delete(0.0, END)
        print("new File ", filename," in use")
        Main.setGlobalPath(os.path.join(os.environ["HOMEPATH"], "Desktop"))
        Main.setGlobalFilename(filename)

    # save changes in the file
    def saveFile(self, extText):
        global filename
        self.getFilePath()
        if(filename==None):
            filename = "Untitled"
        t = extText.get(0.0, END)
        # write into filename with 'w'
        f = open(filePath, 'w')
        f.write(t)
        f.close
        print("File ", filename, " is saved in: ", os.path.abspath(f.name))

    # save File in custom path
    def saveAs(self, extText):
        self.getFilePath()
        f = asksaveasfile(mode='w', defaultextension='.txt')
        print("saving file")
        t = extText.get(0.0, END)
        try:
            f.write(t.rstrip())
            global filename
            filename = os.path.basename(f.name)
            print("File ", filename, " is saved in: ", os.path.abspath(f.name))
            Main.setGlobalFilename(filename)
            Main.setGlobalPath(os.path.curdir)
        except:
            messagebox.showerror(title="Saving Error", message="Unable to save file")
            print("Failed to save file ", f.name)

    # open any file
    def openFile(self, extText):
        f = askopenfile(mode='r')
        t = f.read()
        extText.delete(0.0, END)
        extText.insert(0.0, t)
        filename = os.path.basename(f.name)
        Main.setGlobalPath(os.path.curdir)
        Main.setGlobalFilename(filename)
        print("File ",filename," opened")

    def getFilePath(self):
        global curDir
        curDir = Main.getGlobalPath()
        global filename
        filename = Main.getGlobalFilename()
        global filePath
        filePath = os.path.join(curDir, filename)