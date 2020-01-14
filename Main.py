import Basic_Gui.Window as Window
from os import path, environ

global globalFilename
globalFilename = "Untitled.txt"
global globalPath
globalPath = path.join(environ["HOMEPATH"], "Desktop")

if __name__ == "__main__":
    print("launching Window...")
    test = Window.Window()

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
