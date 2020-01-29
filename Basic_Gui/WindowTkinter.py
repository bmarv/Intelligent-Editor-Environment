import tkinter as tk
from tkinter.scrolledtext import *
from tkinter.filedialog import *
import Main
import Basic_Gui.Fileoperations as Fileoperations
from Statistics import TextinputStatistics as Textstats
from Statistics import FileStatistics as Filestats

class WindowTkinter:
    def __init__(self):
        global mainRef, fileOP
        global activeWindow
        global metaFrame, metaRefresh, metaText, metaValue
        global statsframe, statstext, statsValue
        global textframe, textField, text
        global letterNumber, sentenceNumber, linesNumber, wordNumber
        self.letterNumber=0
        self.wordNumber=0
        self.sentenceNumber=0
        self.linesNumber=1
        global calcStats, fileName,author,filesize
        self.launchWindow()


    def launchWindow(self):
        print("Window launched: Tkinter")
        self.fileOP = Fileoperations.Fileoperations()
        self.activeWindow = tk.Tk()
        self.activeWindow.title("Intelligent Editor Environment")
        self.activeWindow.geometry("800x600")

        # get Menubar for basic actions
        menubar = tk.Menu(self.activeWindow)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label='New File', command=lambda: self.fileOP.newFile(self.textField))
        fileMenu.add_command(label='Open', command=lambda: self.fileOP.openFile(self.textField))
        fileMenu.add_command(label='Save', command=lambda: self.fileOP.saveFile(self.textField))
        fileMenu.add_command(label='Save As', command=lambda: self.fileOP.saveAs(self.textField))
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=lambda: self.exitActivity(self.activeWindow, self.textField))

        menubar.add_cascade(label='File', menu=fileMenu)
        self.activeWindow.config(menu=menubar)

        # frame for meta information
        self.metaFrame = LabelFrame(self.activeWindow, text="Document-Information", width=800, height=5)
        self.metaFrame.pack()

        # button and textview for metainformation
        self.metaRefresh = Button(self.metaFrame,  text="Save & Refresh", width=12, height=1, command= lambda: self.calculateFileStats(self.metaText, self.textField))
        self.metaRefresh.pack(side=LEFT)
        self.metaText = Text(self.metaFrame, width=70, height=1)
        self.metaValue = "please click refresh"
        self.metaText.config(state=tk.NORMAL)
        self.metaText.delete(1.0, tk.END)
        self.metaText.insert(tk.END, self.metaValue)
        self.metaText.config(state=tk.DISABLED)
        self.metaText.pack()


        # frame for text
        self.textFrame = LabelFrame(self.activeWindow, text="Text-Input", relief='raised', width=800, height=400)
        self.textFrame.pack()

        #set ScrolledText-Field inside textFrame
        self.textField = ScrolledText(self.textFrame, font='helvetica 12')
        self.textField.pack()

        # frame for statistics
        self.statsFrame = LabelFrame(self.activeWindow, text="Statistics", width=800, height=100)
        self.statsFrame.pack()

        # button and textview for textinput
        self.calcStats = Button(self.statsFrame, text="Calculate", width=12, height=1, command= lambda: self.calculateStats(self.textField))
        # invoke statistics
        self.calcStats.pack(side=LEFT)
        self.statsValue = "Letters: ", self.letterNumber, "\t Words: ", self.wordNumber,"\t Sentences: ", self.sentenceNumber,"\t Lines: ",self.linesNumber
        self.statsText = Text(self.statsFrame, width=70, height=1)
        self.statsText.config(state=tk.NORMAL)
        self.statsText.delete(1.0, tk.END)
        self.statsText.insert(tk.END, self.statsValue)
        self.statsText.config(state=tk.DISABLED)
        self.statsText.pack(side=RIGHT)

        # close button triggered
        self.activeWindow.protocol("WM_DELETE_WINDOW", lambda: self.exitActivity(self.activeWindow, self.textField))

        # mainloop
        self.activeWindow.mainloop()
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
        self.statsText.config(state=tk.NORMAL)
        self.statsText.delete(1.0, tk.END)
        self.statsText.insert(tk.END, self.statsValue)
        self.statsText.config(state=tk.DISABLED)
        self.statsText.pack(side=RIGHT)

    def calculateFileStats(self, metaText, textField):
        # save File
        self.fileOP.saveFile(textField)
        self.mainRef = Main
        # filename and author
        stats = Filestats.FileStatistics()
        self.fileName= self.mainRef.getGlobalFilename()
        self.author = stats.getAuthor()
        # filesize
        filesizemessage = re.sub("[{}(),'']","",self.mainRef.getFileSizeMessage())
        # write out stats
        self.metaValue = "Author:", self.author, "\tFilename: ", self.fileName, "\tFilesize: ", filesizemessage
        self.metaText.config(state=tk.NORMAL)
        self.metaText.delete(1.0, tk.END)
        self.metaText.insert(tk.END, self.metaValue)
        self.metaText.config(state=tk.DISABLED)
        self.metaText.pack()

    def exitActivity(self, activeWindow, textField):
        # ask whether it should be saved
        savePrompt = tk.messagebox.askquestion('Exit Application', 'Do you want to save the Document?', icon='warning')
        if(savePrompt=='yes'):
            Fileoperations.Fileoperations().saveFile(self.textField)
        self.activeWindow.quit()
        print("activeWindow closed!")