from tkinter.filedialog import *
from tkinter import messagebox
import Main
from Basic_Gui import WindowInstance as WinInstance
from Basic_Gui import WindowTkinter as window

class Fileoperations:
    def __init__(self):
        global filename
        global curDir
        global filePath
        global instance
        instance= WinInstance.WindowInstance()

    # create new File
    def newFile(self, extText):
        self.filename = "Untitled.txt"
        extText.delete(0.0, END)
        # newInstance = Main.WinInstance.WindowInstance()
        # newInstance.newInstance()
        instance.setGlobalFilename(self.filename)
        instance.setGlobalPath(os.path.join(os.environ["HOMEPATH"], "Desktop"))
        print("new File ", self.filename," in use")

    # save changes in the file
    def saveFile(self, extText):
        self.getFilePath()
        if(self.filename==None):
            self.filename = "Untitled"
        t = extText.get(0.0, END)
        # remove automatically added \n at end of file
        t = t[:-1]
        # check for fileintegrity
        if(self.checkFileIntegrity(t)=='yes'):
            # write into filename with 'w'
            f = open(self.filePath, 'w')
            f.write(t)
            f.close
            print("File ", self.filename, " is saved in: ", os.path.abspath(f.name))
        else:
            print("File ", self.filename, " could not be saved")
    #         TODO: prompt file wasn't saved

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
            instance.setGlobalPath(self.curDir)
            instance.setGlobalFilename(self.filename)
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
        instance.setGlobalPath(self.curDir)
        instance.setGlobalFilename(self.filename)
        print("File ",self.filename," opened")

    def getFilePath(self):
        self.curDir = instance.getGlobalPath()
        self.filename = instance.getGlobalFilename()
        self.filePath = os.path.join(self.curDir, self.filename)

    def checkFileIntegrity(self, extText):
        # get path
        self.getFilePath()
        # read out file content --> matches extText?
        integrPrompt = 'yes'
        if(os.path.isfile(self.filePath)):
            f= open(self.filePath, mode='r')
            content = f.read()
            if(extText!=content):
                integrPrompt = messagebox.askquestion('File Integrity', 'This File already exists. Do you want to overwrite this File?', icon='warning')
                if(integrPrompt=='yes'):
                    print("file ", self.filename," was overwritten")
        return integrPrompt