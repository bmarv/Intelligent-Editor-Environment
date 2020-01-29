from tkinter.filedialog import *
from tkinter import messagebox
import Main

class Fileoperations:
    def __init__(self):
        global filename
        global curDir
        global filePath

    # create new File
    def newFile(self, extText):
        self.filename = "Untitled.txt"
        extText.delete(0.0, END)
        print("new File ", self.filename," in use")
        Main.setGlobalPath(os.path.join(os.environ["HOMEPATH"], "Desktop"))
        Main.setGlobalFilename(self.filename)

    # save changes in the file
    def saveFile(self, extText):
        self.getFilePath()
        if(self.filename==None):
            self.filename = "Untitled"
        t = extText.get(0.0, END)
        # write into filename with 'w'
        f = open(self.filePath, 'w')
        f.write(t)
        f.close
        print("File ", self.filename, " is saved in: ", os.path.abspath(f.name))

    # save File in custom path
    def saveAs(self, extText):
        self.getFilePath()
        f = asksaveasfile(mode='w', defaultextension='.txt')
        print("saving file")
        t = extText.get(0.0, END)
        try:
            f.write(t.rstrip())
            self.filename = os.path.basename(f.name)
            self.curDir = os.path.split(str(f.name))[0]
            print("File ", self.filename, " is saved in: ", os.path.abspath(f.name))
            Main.setGlobalPath(self.curDir)
            Main.setGlobalFilename(self.filename)
        except:
            messagebox.showerror(title="Saving Error", message="Unable to save file")
            print("Failed to save file ", f.name)

    # open any file
    def openFile(self, extText):
        f = askopenfile(mode='r')
        print("open File ",f.name)
        t = f.read()
        extText.delete(0.0, END)
        extText.insert(0.0, t)
        self.filename = os.path.basename(f.name)
        self.curDir = os.path.split(str(f.name))[0]
        Main.setGlobalPath(self.curDir)
        Main.setGlobalFilename(self.filename)
        print("File ",self.filename," opened")

    def getFilePath(self):
        self.curDir = Main.getGlobalPath()
        self.filename = Main.getGlobalFilename()
        self.filePath = os.path.join(self.curDir, self.filename)