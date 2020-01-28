import tkinter as tk
from tkinter.scrolledtext import *
from tkinter.filedialog import *
import Main
import Basic_Gui.Fileoperations as Fileoperations
from Statistics import TextinputStatistics as Textstats
from Statistics import FileStatistics as Filestats

class WindowTkinter:
    def __init__(self):
        global statsframe
        global statstext
        global statsValue
        global activeWindow
        global textField
        global text
        global letterNumber
        self.letterNumber=0
        global wordNumber
        self.wordNumber=0
        global sentenceNumber
        self.sentenceNumber=0
        global linesNumber
        self.linesNumber=1
        global metaText
        global metaValue
        global fileName
        global author
        self.launchWindow()


    def launchWindow(self):
        print("Window launched: Tkinter")
        fileOP = Fileoperations.Fileoperations()
        global activeWindow
        activeWindow = tk.Tk()
        activeWindow.title("Intelligent Editor Environment")
        activeWindow.geometry("800x600")

        # get Menubar for basic actions
        menubar = tk.Menu(activeWindow)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label='New File', command=lambda: fileOP.newFile(textField))
        fileMenu.add_command(label='Open', command=lambda: fileOP.openFile(textField))
        fileMenu.add_command(label='Save', command=lambda: fileOP.saveFile(textField))
        fileMenu.add_command(label='Save As', command=lambda: fileOP.saveAs(textField))
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=activeWindow.quit)

        menubar.add_cascade(label='File', menu=fileMenu)
        activeWindow.config(menu=menubar)

        # frame for meta information
        metaFrame = LabelFrame(activeWindow, text="Meta-Information", width=800, height=5)
        metaFrame.pack()

        # textview for metainformation
        self.metaText = Text(metaFrame, width=80, height=1)
        self.calculateFileStats(self.metaText)
        self.metaValue = "Author:", self.author,"\tFileName: ", self.fileName
        self.metaText.delete(1.0, tk.END)
        self.metaText.insert(tk.END, self.metaValue)
        self.metaText.pack()


        # frame for text
        global textframe
        textFrame = LabelFrame(activeWindow, text="Text-Input", relief='raised', width=800, height=400)
        textFrame.pack()

        #set ScrolledText-Field inside textFrame
        global textField
        textField = ScrolledText(textFrame, font='helvetica 12')
        textField.pack()

        # frame for statistics
        self.statsFrame = LabelFrame(activeWindow, text="Statistics", relief='raised',width=800, height=100)
        self.statsFrame.pack()

        # set button and textview for textinput
        global calcStats
        calcStats = Button(self.statsFrame, text="Calculate", width=10, height=1, command= lambda: self.calculateStats(textField))
        # invoke statistics
        calcStats.pack(side=LEFT)
        self.statsValue = "Letters: ", self.letterNumber, "\t Words: ", self.wordNumber,"\t Sentences: ", self.sentenceNumber,"\t Lines: ",self.linesNumber
        self.statsText = Text(self.statsFrame, width=70, height=1)
        self.statsText.delete(1.0, tk.END)
        self.statsText.insert(tk.END, self.statsValue)
        self.statsText.pack(side=RIGHT)

        # mainloop
        activeWindow.mainloop()
        print("Window closed")

    def getActiveWindow(self):
        return activeWindow

    def getActiveText(self):
        return text

    def calculateStats(self, textField):
        global text
        text = textField.get(1.0, tk.END)
        # count letters
        self.letterNumber = Textstats.TextinputStatistics().countLetters(text)
        # count words
        self.wordNumber = Textstats.TextinputStatistics().countWords(text)
        # count sentences
        self.sentenceNumber = Textstats.TextinputStatistics().countSentences(text)
        # count lines
        self.linesNumber = Textstats.TextinputStatistics().countLines(text)
        # write out stats
        self.statsValue = "Letters: ", self.letterNumber, "\t Words: ", self.wordNumber,"\t Sentences: ", self.sentenceNumber,"\t Lines: ",self.linesNumber
        self.statsText.delete(1.0, tk.END)
        self.statsText.insert(tk.END, self.statsValue)
        self.statsText.pack(side=RIGHT)

    def calculateFileStats(self, metaText):
        stats = Filestats.FileStatistics()
        self.fileName= Main.getGlobalFilename()
        self.author = stats.getAuthor()
        # write out stats
        self.metaValue = "Author:", self.author, "\tFileName: ", self.fileName
        self.metaText.delete(1.0, tk.END)
        self.metaText.insert(tk.END, self.metaValue)
        self.metaText.pack()