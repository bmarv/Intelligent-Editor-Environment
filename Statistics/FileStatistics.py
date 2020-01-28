import getpass

class FileStatistics:
    def __init__(self):
        global author



    def getAuthor(self):
        self.author = getpass.getuser()
        return self.author