from tkinter.filedialog import *
from tkinter import messagebox
# import tkinter as tk
import Basic_Gui.Window as Window
import Main

#TODO: use class for fileoperations instead of having one big window class
class Fileoperations:
    def __init__(self):
        global filename
        global curDir
        global filePath
        # pass

    # create new File
    def newFile(self, extText):
        global filename
        filename = "Untitled"
        extText.delete(0.0, END)
        print("new File \"Untitled\" created")
        Main.setGlobalPath(os.path.join(os.environ["HOMEPATH"], "Desktop"))
        Main.setGlobalFilename(filename)

    # save changes in the file
    def saveFile(self, extText):
        filename = Main.getGlobalFilename()
        self.getFilePath()
        if(self.filename==None):
            filename = "Untitled"
        t = extText.get(0.0, END)
        # write into filename with 'w'
        f = open(filePath, 'w')
        f.write(t)
        print("File ", filename, " is saved", os.path.abspath(f.name))
        f.close

    # save File in custom path
    def saveAs(self, extText):
        self.getFilePath()
        f = asksaveasfile(mode='w', defaultextension='.txt')
        print("\tsaving file")
        t = extText.get(0.0, END)
        try:
            f.write(t.rstrip())
            global filename
            filename = os.path.basename(f.name)
            print("File ", filename, " saved")
            Main.setGlobalFilename(filename)
            Main.setGlobalPath(os.path.curdir)
        except:
            messagebox.showerror(title="Saving Error", message="Unable to save file")
            print("Failed to save file ", f)

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