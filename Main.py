import Basic_Gui.Window as Window

global globalFilename
globalFilename = None
global globalPath
globalPath = None

if __name__ == "__main__":
    print("launching Window...")
    test = Window.Window()

def setGlobalFilename(filename):
    global globalFilename
    globalFilename=filename
    print("new globalfilename", globalFilename)

def getGlobalFilename():
    print("globalfilename",globalFilename)
    return globalFilename


def setGlobalPath(path):
    global globalPath
    globalPath = path
    print("new globalPath", globalPath)

def getGlobalPath():
    print("globalpath",globalPath)
    return globalPath
