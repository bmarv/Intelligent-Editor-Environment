import tkinter as tk
from tkinter.scrolledtext import *
from tkinter.filedialog import *
import Main
import Basic_Gui.WindowInstance as WinInstance
import Basic_Gui.Fileoperations as Fileoperations
from Statistics import TextinputStatistics as Textstats
from Statistics import FileStatistics as Filestats

class WindowTkinter:
    def __init__(self):
        global instance, fileOP
        self.instance = WinInstance.WindowInstance()
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
        global fontSize, technicalFont
        self.fontSize=12
        self.technicalFont=0
        self.launchWindow()


    def launchWindow(self):
        print("Window launched: Tkinter")
        self.fileOP = Fileoperations.Fileoperations()
        self.activeWindow = tk.Tk()
        self.activeWindow.title("Intelligent Editor Environment")
        self.activeWindow.geometry("800x600")

        # get Menubar for basic actions
        menubar = tk.Menu(self.activeWindow)

        # filemenu for menubar
        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label='New File', command=lambda: self.fileOP.newFile(self.textField), accelerator="Ctrl+N")
        self.activeWindow.bind_all("<Control-n>", lambda x:self.fileOP.newFile(self.textField))
        fileMenu.add_command(label='Open', command=lambda: self.fileOP.openFile(self.textField), accelerator="Ctrl+O")
        self.activeWindow.bind_all("<Control-o>", lambda x:self.fileOP.openFile(self.textField))
        fileMenu.add_command(label='Save', command=lambda: self.fileOP.saveFile(self.textField), accelerator="Ctrl+S")
        self.activeWindow.bind_all("<Control-s>", lambda x:self.fileOP.saveFile(self.textField))
        fileMenu.add_command(label='Save As', command=lambda: self.fileOP.saveAs(self.textField), accelerator="Ctrl+Shift+S")
        self.activeWindow.bind_all("<Control-S>", lambda x:self.fileOP.saveAs(self.textField))
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=lambda: self.exitActivity(self.activeWindow, self.textField),accelerator="Ctrl+X")
        self.activeWindow.bind_all("<Control-x>", lambda x:self.exitActivity(self.activeWindow, self.textField))

        menubar.add_cascade(label='File', menu=fileMenu)

        # Edit actions for menubar
        editMenu = tk.Menu(menubar)
        editMenu.add_command(label='Undo', command=lambda: self.textField.edit_undo(), accelerator="Ctrl+Z")
        editMenu.add_command(label='Redo', command=lambda: self.textField.edit_redo(), accelerator="Ctrl+Y")
        editMenu.add_separator()
        editMenu.add_command(label='Increase Text-Size', command=lambda: self.increaseTextSize(), accelerator="Ctrl++")
        self.activeWindow.bind_all("<Control-plus>", lambda x: self.increaseTextSize())
        editMenu.add_command(label='Decrease Text-Size', command=lambda: self.decreaseTextSize(), accelerator="Ctrl+-")
        self.activeWindow.bind_all("<Control-minus>", lambda x: self.decreaseTextSize())
        editMenu.add_command(label='Change Font', command=lambda: self.changeFont())
        menubar.add_cascade(label='Edit', menu=editMenu)

        self.activeWindow.config(menu=menubar)

        # frame for meta information
        self.metaFrame = LabelFrame(self.activeWindow, text="Document-Information", width=800, height=5)
        self.metaFrame.pack()

        # button and textview for metainformation
        self.metaRefresh = Button(self.metaFrame,  text="Save & Refresh", width=12, height=1, command= lambda: self.calculateFileStats(self.metaText, self.textField))
        self.metaRefresh.pack(side=LEFT)
        self.activeWindow.bind_all("<Control-r>", lambda x: self.calculateFileStats(self.metaText, self.textField))
        self.metaText = Text(self.metaFrame, width=100, height=1)
        self.metaValue = "please refresh to load"
        self.metaText.config(state=tk.NORMAL)
        self.metaText.delete(1.0, tk.END)
        self.metaText.insert(tk.END, self.metaValue)
        self.metaText.config(state=tk.DISABLED)
        self.metaText.pack()


        # frame for text
        self.textFrame = LabelFrame(self.activeWindow, text="Text-Input", relief='raised', width=800, height=400)
        self.textFrame.pack()

        #set ScrolledText-Field inside textFrame
        self.textField = ScrolledText(self.textFrame, font=('helvetica',12), undo=TRUE, width=100)
        self.textField.pack()

        # frame for statistics
        self.statsFrame = LabelFrame(self.activeWindow, text="Statistics", width=800, height=100)
        self.statsFrame.pack()

        # button and textview for textinput
        # invoke statistics
        self.calcStats = Button(self.statsFrame, text="Calculate", width=12, height=1, command= lambda: self.calculateStats(self.textField))
        self.calcStats.pack(side=LEFT)
        self.activeWindow.bind_all("<Control-C>", lambda x: self.calculateStats(self.textField))
        self.statsValue = "Letters: ", self.letterNumber, "\t Words: ", self.wordNumber,"\t Sentences: ", self.sentenceNumber,"\t Lines: ",self.linesNumber
        self.statsText = Text(self.statsFrame, width=100, height=1)
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
        # filename and author
        stats = Filestats.FileStatistics()
        self.fileName= self.instance.getGlobalFilename()
        self.author = stats.getAuthor()
        # filesize
        filesizemessage = re.sub("[{}(),'']","",self.instance.getFileSizeMessage())
        # write out stats
        self.metaValue = "Filename: ", self.fileName, "\tFilesize: ", filesizemessage,"\tAuthor:", self.author
        self.metaText.config(state=tk.NORMAL)
        self.metaText.delete(1.0, tk.END)
        self.metaText.insert(tk.END, self.metaValue)
        self.metaText.config(state=tk.DISABLED)
        self.metaText.pack()

    def exitActivity(self, activeWindow, textField):
        # check file-integrity
        filePath = os.path.join(self.instance.getGlobalPath(), self.instance.getGlobalFilename())
        if (os.path.isfile(filePath)):
            f = open(filePath, mode='r')
            content = f.read()
            # remove \n of last empty save
            if(content=="\n"):
                content = content[:-1]
            text = str(textField.get(0.0,END))
            # remove added \n
            if(text=="\n"):
                text = text[:-1]
            # ask whether it should be saved
            if (text != content):
                savePrompt = tk.messagebox.askquestion('Exit Application', 'Do you want to save the Document?', icon='warning')
                if(savePrompt=='yes'):
                    self.fileOP.saveFile(self.textField)
                    print("File saved on exit-activity")
                else:
                    print("File not saved on exit-activity")
        self.activeWindow.quit()
        print("activeWindow closed!")


    def increaseTextSize(self):
        self.fontSize+=1
        self.textField.configure(font=('helvetica', self.fontSize))
        self.textField.pack()

    def decreaseTextSize(self):
        self.fontSize-=1
        self.textField.configure(font=('helvetica', self.fontSize))
        self.textField.pack()

    def changeFont(self):
        if(self.technicalFont==0):
            self.technicalFont=1
            self.fontSize+=1
            self.textField.configure(font=('Times', self.fontSize))
        else:
            self.technicalFont=0
            self.fontSize-=1
            self.textField.configure(font=('helvetica', self.fontSize))
        self.textField.pack()
