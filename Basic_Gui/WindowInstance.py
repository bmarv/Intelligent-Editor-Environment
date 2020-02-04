"author: Marvin Beese"

import Basic_Gui.WindowTkinter as Window
import Basic_Gui.WindowPyQt5 as WindowQt
from os import path, environ
class WindowInstance:

    global globalFilename
    globalFilename = "Untitled.txt"
    global globalPath
    globalPath = path.normpath(path.join(environ["HOMEPATH"], "Desktop"))
    global test
    print("launching Window...")

    def __init__(self):
        pass

    def newInstance(self):
        test = Window.WindowTkinter()
        # print("new Instance ", test)

    "--- getter and setter for fileoperations"
    def setGlobalFilename(self, filename):
        global globalFilename
        globalFilename = filename
        print("\tnew globalfilename: ", globalFilename)

    def getGlobalFilename(self):
        print("\tglobalfilename: ", globalFilename)
        return globalFilename

    def setGlobalPath(self,path):
        global globalPath
        globalPath = path
        print("\tnew globalPath: ", globalPath)

    def getGlobalPath(self):
        print("\tglobalpath: ", globalPath)
        return globalPath

    def getFileSizeMessage(self):
        joinedpath = path.abspath(path.join(globalPath, globalFilename))
        print(joinedpath)
        filesize = path.getsize(joinedpath)
        # switch between byte, kilobyte and megabyte
        sizemessage = ""
        if (filesize > 1000000):
            sizemessage = filesize / 1000000, " Megabyte"
        elif (filesize >= 1000):
            sizemessage = filesize / 1000, " Kilobyte"
        else:
            sizemessage = filesize, " Byte"
        print("\tfilesize: ", sizemessage)
        return str(sizemessage)

