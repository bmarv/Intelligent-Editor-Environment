"author: Marvin Beese"
from Statistics import FileAnalysis
import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from ttkthemes import ThemedTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt

class AnalysisFrame():
    def __init__(self, file):
        global currFile, fileAna
        self.currFile=file
        self.fileAna = FileAnalysis.FileAnalysis()
        global anaFrame, stylettk
        global plotterFrame, refreshPlotButton, plot, plot, a, canvas, b
        global checkFrame, textFrame, graphCheck, gradientCheck, exponentCheck, graphVar, gradientVar, expVar, textGraph, textGradient, textExp
        global tableFrame, refreshTableButton, listNodes, scrollbar, wordFrame, queryFrame, queryResult, queryResultText, totalWordsLabel
        global n, W, sortedW

    def launchAnalysis(self):
        print("launching Analysis Frame")
        self.anaFrame = ThemedTk(theme='radiance')
        title="IEE - Text Analysis for", os.path.basename(self.currFile)
        self.anaFrame.title(title)
        self.anaFrame.geometry("800x600")
        self.stylettk = ttk.Style()

        # menubar
        menubar = tk.Menu(self.anaFrame)
        # TODO: menu for plotting
        plottingMenu = tk.Menu(menubar)
        plottingMenu.add_command(label='Refresh Graph', command=lambda: self.buildPlot(50), accelerator="Ctrl-R")
        self.anaFrame.bind_all("<Control-r>", lambda x: self.buildPlot(50))
        plottingMenu.add_command(label='Plot Gradient')
        plottingMenu.add_command(label='Calculate Exponent')
        plottingMenu.add_separator()
        plottingMenu.add_command(label='Calculate Table', command=lambda: self.updateTable(), accelerator="Ctrl-T")
        self.anaFrame.bind_all("<Control-t>", lambda x: self.updateTable())
        plottingMenu.add_separator()
        plottingMenu.add_command(label='Exit Analysis', command= lambda:self.anaFrame.destroy(), accelerator="Ctrl+X")
        self.anaFrame.bind_all("<Control-x>", lambda x: self.anaFrame.destroy())
        menubar.add_cascade(label='Calculating', menu=plottingMenu)

        # TODO: menu for output as .txt file
        outputMenu= tk.Menu(menubar)
        outputMenu.add_command(label='Save Plot as PDF')
        outputMenu.add_command(label='Save Table as .txt')
        menubar.add_cascade(label='Saving Tools', menu=outputMenu)

        self.anaFrame.configure(menu=menubar)

        # TODO: plotter on left side
        # TODO: Button plot gradient, calculate exponent of distribution

        # build top
        self.buildPlotterFrameTop()

        # plotting area
        self.fig = Figure(figsize=(4, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plotterFrame)
        self.buildPlot(50)
        # self.calcGradient(50)

        #  Table with word statistics
        self.wordFrame = ttk.Frame(self.anaFrame, width=10)
        self.wordFrame.pack(side=RIGHT, anchor=N, padx=5, pady=20)
        self.refreshTableButton = ttk.Button(self.wordFrame, text='Refresh Table', width=13, command= lambda: self.updateTable())
        self.refreshTableButton.pack(side=TOP, anchor=NW)

        # scrollable Table
        self.tableFrame= ttk.Frame(self.wordFrame)
        self.tableFrame.pack(side=TOP, fill=BOTH)
        self.listNodes = Listbox(self.tableFrame, width=50, height=20, font=("Helvetica", 10))
        self.listNodes.pack(side=LEFT, anchor=N, fill="y")

        self.scrollbar = Scrollbar(self.tableFrame, orient="vertical")
        self.scrollbar.config(command=self.listNodes.yview)
        self.scrollbar.pack(side=RIGHT, anchor=N, fill="y")
        self.listNodes.config(yscrollcommand=self.scrollbar.set)

        # total words
        totalWordsFrame=ttk.Frame(self.wordFrame)
        totalWordsFrame.pack(side=TOP, fill=BOTH)

        self.totalWordsLabel=ttk.Label(totalWordsFrame, text='Total Word Number:   0')
        self.totalWordsLabel.pack(side=TOP, anchor=W, fill="y")
        self.updateTable()  #update table and full count on startup

        # query for specific word
        self.queryFrame= ttk.Frame(self.wordFrame)
        self.queryFrame.pack(side=TOP, anchor=W, fill=BOTH)
        queryLabel1=ttk.Label(self.queryFrame, text='Word Occurrences for: ')
        queryLabel1.pack(side=LEFT, anchor=N, pady=6)
        queryEntry=ttk.Entry(self.queryFrame, width=10)
        queryEntry.bind('<Return>', lambda x: self.searchForWord(str(queryEntry.get()).casefold().strip()))
        queryEntry.pack(side=LEFT,anchor=N, pady=6)

        queryButton=ttk.Button(self.queryFrame, text='=>', width=2, command=lambda: self.searchForWord(str(queryEntry.get()).casefold().strip()))
        queryButton.pack(side=LEFT, anchor=W)
        self.queryResult=""
        self.queryResultText=Text(self.queryFrame, height=1, width=5)
        self.queryResultText.configure(state=DISABLED)
        self.queryResultText.pack(side=LEFT, anchor=W)

        # run mainloop
        self.anaFrame.mainloop()
        print("Analysis Frame closed")

    # reloads table with freshly calculated values
    # reloads label under table with total number of words
    def updateTable(self):
        # get TextStats
        self.n,self.W = self.fileAna.textStats(self.currFile, True)
        # fill table
        self.listNodes.delete(0,END)
        self.sortedW=dict()
        self.sortedW= self.fileAna.sortTextStats(self.W)
        i = 0
        for k,v in self.sortedW:
            if(i>=100):
                break
            i=i+1
            output=i,":\t",k,v
            self.listNodes.insert(END,output)
            if(str(k)[0].isupper()):
                self.listNodes.itemconfig(i-1,{'fg':'purple'})
        self.listNodes.pack(side="left", fill="y")
        self.scrollbar.configure(command=self.listNodes.yview)
        # fill label with total number of words
        totalWordsNr="Total Word Number:   ",self.n
        self.totalWordsLabel.config(text=totalWordsNr)
        self.totalWordsLabel.pack(side=TOP, anchor=W, fill="y")


    # query for word in file
    def searchForWord(self, query):
        self.n=0
        self.W=dict()
        self.updateTable() #consistency with table
        for key,v in self.W.items():
            if(query.casefold()==str(key).casefold()):
                self.queryResult=v
                print("Word \"",query,"\" found ",self.queryResult," times")
                break
        else:
            self.queryResult=0
            print("Word \"", query, "\" not found ")
        self.queryResultText.config(state=NORMAL)
        self.queryResultText.delete(1.0, END)
        self.queryResultText.insert(tk.END, self.queryResult)
        self.queryResultText.config(state=DISABLED)
        self.queryResultText.pack(side=LEFT, anchor=W)

    def calcPlot(self, max):
        self.n, self.W = self.fileAna.textStats(self.currFile, True)
        self.sortedW = dict()
        self.sortedW = self.fileAna.sortTextStats(self.W)
        x=np.array([])
        y=np.array([])
        word=np.array([])
        i = 0
        for k,v in self.sortedW:
            if(i>=max):
                break
            i+=1
            x= np.append(x,i)
            y=np.append(y,v)
            word= np.append(word, k)
        return x,y,word

    def buildPlot(self, max):

        self.plotterFrame.destroy()
        self.buildPlotterFrameTop()
        self.fig = Figure(figsize=(4, 4))
        self.a = self.fig.add_subplot(111)
        x, y, word = self.calcPlot(max)
        self.a.scatter(x, y, color='red')

        for i, txt in enumerate(word):
            self.a.annotate(txt, (i+1, y[i]), xycoords='data')

        self.a.set_title("Most frequent Words", fontsize=16)
        self.a.set_ylabel("Occurrences", fontsize=8)
        self.a.set_xlabel("Word", fontsize=8)
        self.a.grid(True)
        self.a.set_xscale('log')
        self.a.set_yscale('log')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plotterFrame)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        self.buildPlotterFrameBottom()

    # builds toplevel frame for plotting, builds part above plot (refresh button)
    def buildPlotterFrameTop(self):
        self.plotterFrame = ttk.Frame(self.anaFrame, width=400)
        self.plotterFrame.pack(side=LEFT, anchor=N, padx=10, pady=20)
        # refresh
        self.refreshPlotButton = ttk.Button(self.plotterFrame, text='Refresh Plot', width=13, command=lambda: self.buildPlot(50))
        self.refreshPlotButton.pack(side=TOP, anchor=NW)

    # builds part underneath plot (check buttons, textfields)
    def buildPlotterFrameBottom(self):
        # checkbutton frame
        self.checkFrame = ttk.Frame(self.plotterFrame, width=10)
        self.checkFrame.pack(side=LEFT, anchor=N)
        self.graphVar = IntVar()
        self.graphCheck = Checkbutton(self.checkFrame, text='Graph', variable=self.graphVar)
        self.graphCheck.pack(side=TOP, anchor=W)
        self.gradientVar = IntVar()
        self.gradientCheck = Checkbutton(self.checkFrame, text='Gradient', variable=self.gradientVar)
        self.gradientCheck.pack(side=TOP, anchor=W)
        self.expVar = IntVar()
        self.exponentCheck = Checkbutton(self.checkFrame, text='Exponent', variable=self.expVar)
        self.exponentCheck.pack(side=TOP, anchor=W)

        # TODO: Textbox for graph, gradient, exponent
        self.textFrame = ttk.Frame(self.plotterFrame, width=20)
        self.textFrame.pack(side=LEFT, anchor=N)
        self.textGraph = Text(self.textFrame, width=20, height=1)
        self.textGraph.pack(side=TOP)
        self.textGradient = Text(self.textFrame, width=20, height=1)
        self.textGradient.pack(side=TOP)
        self.textExp = Text(self.textFrame, width=20, height=1)
        self.textExp.pack(side=TOP)

    def calcGradient(self, max):
        x, y, word = self.calcPlot(max)
        x1,y1= x[0],y[0]
        x2,y2=x[-1:],y[-1:]
        self.b = self.fig.add_subplot(111)
        self.b.plot(x1, y1, x2, y2, color='b')
        self.canvas.draw()
