import Basic_Gui.WindowTkinter as Window
import Basic_Gui.WindowPyQt5 as WindowQt
from os import path, environ


global globalFilename
globalFilename = "Untitled.txt"
global globalPath
globalPath = path.normpath(path.join(environ["HOMEPATH"], "Desktop"))
global test

if __name__ == "__main__":
    print("launching Window...")
    test = Window.WindowTkinter()
    # test = WindowQt.WindowPyQt5()


"--- getter and setter for fileoperations"
def setGlobalFilename(filename):
    global globalFilename
    globalFilename=filename
    print("\tnew globalfilename: ", globalFilename)

def getGlobalFilename():
    print("\tglobalfilename: ",globalFilename)
    return globalFilename


def setGlobalPath(path):
    global globalPath
    globalPath = path
    print("\tnew globalPath: ", globalPath)

def getGlobalPath():
    print("\tglobalpath: ",globalPath)
    return globalPath

def getFileSizeMessage():
    joinedpath= path.abspath(path.join(globalPath, globalFilename))
    print(joinedpath)
    filesize = path.getsize(joinedpath)
    # switch between byte, kilobyte and megabyte
    sizemessage=""
    if(filesize>1000000):
        sizemessage= filesize/1000000, " Megabyte"
    elif(filesize>=1000):
        sizemessage = filesize/1000, " Kilobyte"
    else:
        sizemessage = filesize," Byte"
    print("\tfilesize: ",sizemessage)
    return str(sizemessage)

