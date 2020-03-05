__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

import Basic_Gui.WindowTkinter as Window
from os import path
from os.path import expanduser

"""Class for invoking new WindowTkinter-Instances of the Program.
    Every Instance includes the same Meta-Data
    (filename, path, filesize).
"""
class WindowInstance:

    def __init__(self):
        global globalFilename
        globalFilename = "Untitled.txt"
        global globalPath
        # globalPath = path.normpath(path.join(environ["HOMEPATH"], "Desktop"))
        globalPath = path.normpath(path.join(expanduser("~"),"Desktop"))
        global instance

    def newInstance(self):
        # new program-instance
        print("launching Instance...")
        self.instance = Window.WindowTkinter()


    """getter and setter for fileoperations"""
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

    """calculation of the filesize of the current file. Separate values for byte, kilobyte and megabyte"""
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

