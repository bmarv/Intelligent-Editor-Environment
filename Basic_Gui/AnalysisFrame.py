__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from ttkthemes import ThemedTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from Statistics import FileAnalysis
from Statistics import MathematicalAnalysis

""" GUI for mathematical analyses calculated in Statistics/MathematicalAnalysis.
    Display and Interaction for a graphical plot, a word table, word-occurrences search,
    slope-calculation of the distribution, Zipf-exponent of the distribution
    and probability calculation of the Zipf-Probability-Mass-Function
"""
class AnalysisFrame():
    def __init__(self, file):
        global currFile, fileAna, MathAna
        self.currFile=file
        self.fileAna = FileAnalysis.FileAnalysis()
        self.MathAna= MathematicalAnalysis.MathematicalAnalysis()
        global anaFrame, stylettk
        # n= total words in text, max= distinct words in text, limit= limit for calculation
        global plotterFrame, refreshPlotButton, plot, plot, a, canvas, b, graph, fig, scatterValue, x, y, word, x1,y1, word1, limit, max
        self.limit=100
        self.max=100
        global checkFrame, textFrame, graphCheck, slopeCheck, exponentCheck, graphVar, slopeVar, expVar, textGraph, textSlope, textExp
        self.slopeVar=0; self.graphVar=0; self.expVar=0
        global tableFrame, refreshTableButton, listNodes, scrollbar, wordFrame, queryFrame, queryResult, queryResultText, totalWordsLabel, rankedWordCount, probResult, probResultText
        global n, W, sortedW
        self.n, self.W = self.fileAna.textStats(self.currFile, True)

    def launchAnalysis(self):
        print("launching Analysis Frame for {0}".format(os.path.basename(self.currFile)))
        self.anaFrame = ThemedTk(theme='arc')
        title="IEE - Text Analysis for {0}".format(os.path.basename(self.currFile))
        self.anaFrame.title(title)
        self.anaFrame.geometry("900x750")
        self.stylettk = ttk.Style()

        # build Frames for menubar, plotting, texttable
        self.buildmenuBar()
        self.buildPlotArea()
        self.buildWordTable()

        # run mainloop
        self.anaFrame.mainloop()
        print("Analysis Frame closed for {0}".format(os.path.basename(self.currFile)))

    """menubar for calculation and exporting of data"""
    def buildmenuBar(self):
        # menubar
        menubar = tk.Menu(self.anaFrame)
        plottingMenu = tk.Menu(menubar)
        plottingMenu.add_command(label='Refresh Data', command=lambda: self.limitUpdated(self.limit), accelerator="Ctrl+R")
        self.anaFrame.bind_all("<Control-r>", lambda x: self.limitUpdated(self.limit))
        plottingMenu.add_command(label='Calculate Slope', command=lambda: self.calcSlope(), accelerator="Ctrl+S")
        self.anaFrame.bind_all("<Control-s>", lambda x: self.calcSlope())
        plottingMenu.add_command(label='Calculate Exponent', command=lambda: self.calcExpZipf(), accelerator="Ctrl+E")
        self.anaFrame.bind_all("<Control-e>", lambda x: self.calcExpZipf())
        plottingMenu.add_separator()
        plottingMenu.add_command(label='Exit Analysis', command=lambda: self.anaFrame.destroy(), accelerator="Ctrl+X")
        self.anaFrame.bind_all("<Control-x>", lambda x: self.anaFrame.destroy())
        menubar.add_cascade(label='Calculation', menu=plottingMenu)

        # menu for export
        outputMenu = tk.Menu(menubar)
        outputMenu.add_command(label='Save Plot as .pdf', command=lambda: self.savePlotAsPDF(),
                               accelerator="Ctrl+Shift+P")
        self.anaFrame.bind_all("<Control-P>", lambda x: self.savePlotAsPDF())
        outputMenu.add_command(label='Save Table as .txt', command=lambda: self.saveTableAsTxt(),
                               accelerator="Ctrl+Shift+T")
        self.anaFrame.bind_all("<Control-T>", lambda x: self.saveTableAsTxt())
        menubar.add_cascade(label='Export', menu=outputMenu)

        self.anaFrame.configure(menu=menubar)

    """plot area consists of FrameTop, Plot and FrameBottom (invoked in buildPlot())"""
    def buildPlotArea(self):
        # plotting area
        self.buildPlotterFrameTop()
        self.buildPlot(self.limit)

    """calc plot with defined word-limit. Rank (i), Occurrences (v) and Word (k) are used"""
    def calcPlot(self, limit):
        self.sortedW = dict()
        self.sortedW = self.fileAna.sortTextStats(self.W)
        x=np.array([])
        y=np.array([])
        word=np.array([])
        i = 0
        for k,v in self.sortedW:
            if (i >= limit):
                break
            i+=1
            x= np.append(x,i)
            y=np.append(y,v)
            word= np.append(word, k)
        return x,y,word

    """frame for setting the limit using a scale and an entry"""
    def buildPlotterFrameTop(self):
        self.plotterFrame = ttk.Frame(self.anaFrame, width=400)
        self.plotterFrame.pack(side=LEFT, anchor=N, padx=10, pady=20)
        # set value for visualisation
        plotLimitFrame = ttk.Frame(self.plotterFrame, width=400)
        self.w2 = Scale(plotLimitFrame, from_=0, to=self.max, orient=HORIZONTAL, length=400,
                        label="Number of Words")
        self.w2.set(self.limit)
        plotLimitEntry = ttk.Entry(plotLimitFrame, width=8)
        plotLimitEntry.bind('<Return>', lambda x: self.limitUpdated(int(plotLimitEntry.get())))
        # refresh
        self.refreshPlotButton = ttk.Button(self.plotterFrame, text='Refresh Data', width=13,
                                            command=lambda: self.limitUpdated(self.w2.get()))
        self.refreshPlotButton.pack(side=TOP, anchor=W)
        plotLimitFrame.pack(side=TOP, anchor=W)
        self.w2.pack(side=LEFT, padx=3)
        plotLimitEntry.pack(side=LEFT)

    """builds plot and build word table for new setted limit"""
    def limitUpdated(self, value):
        self.limit= value
        if(int(value)>int(self.max)):
            self.max= value
        self.buildPlot(value)
        self.wordFrame.destroy()
        self.buildWordTable()

    """points are scattered in double-log scale using matplotlib. """
    def buildPlot(self, limit):
        self.limit = limit
        self.plotterFrame.destroy()
        self.buildPlotterFrameTop()
        self.fig = Figure(figsize=(5,5), dpi=100)
        self.a = self.fig.add_subplot(111)
        # get values
        self.x, self.y, self.word = self.calcPlot(self.limit)
        self.a.scatter(self.x, self.y, color='red')

        for i, txt in enumerate(self.word):
            self.a.annotate(txt, (i + 1, self.y[i]), xycoords='data')

        self.a.set_title("Most frequent Words", fontsize=16)
        self.a.set_ylabel("Occurrences", fontsize=9)
        self.a.set_xlabel("Word Rank", fontsize=9)
        self.a.grid(True)
        self.a.tick_params(labelsize=8)
        self.a.set_xscale('log')
        self.a.set_yscale('log')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plotterFrame)
        self.canvas.get_tk_widget().pack(expand=True)
        # navigation bar
        toolbar= NavigationToolbar2Tk(self.canvas, self.plotterFrame)
        toolbar.update()
        self.canvas.draw()
        # build the bottom area accordingly (dependence to buildPlot)
        self.buildPlotterFrameBottom()
        # deselect gradient
        self.slopeVar = 0
        self.slopeCheck.deselect()
        self.expVar = 0
        self.exponentCheck.deselect()

    """frame for slope and zipfian exponent"""
    def buildPlotterFrameBottom(self):
        # checkbutton frame
        self.checkFrame = ttk.Frame(self.plotterFrame, width=10)
        self.checkFrame.pack(side=LEFT, anchor=N)
        self.slopeCheck = Checkbutton(self.checkFrame, text='Slope', variable=self.slopeVar, command= lambda: self.calcSlope())
        self.slopeCheck.pack(side=TOP, anchor=W)
        self.exponentCheck = Checkbutton(self.checkFrame, text='Exponent of Zipf-Distribution', variable=self.expVar, command= lambda: self.calcExpZipf())
        self.exponentCheck.pack(side=TOP, anchor=W)

        self.textFrame = ttk.Frame(self.plotterFrame, width=20)
        self.textFrame.pack(side=LEFT, anchor=N)
        self.textSlope = Text(self.textFrame, width=30, height=1)
        self.textSlope.config(state=DISABLED)
        self.textSlope.pack(side=TOP)
        self.textExp = Text(self.textFrame, width=30, height=1)
        self.textExp.pack(side=TOP)

    """exports current plot to a .pdf-file"""
    def savePlotAsPDF(self):
        filename= str(self.currFile).replace(".txt","_plot.pdf")
        try:
            self.fig.savefig(filename)
            print("plot saved as pdf in ", filename)
        except:
            tk.messagebox.showerror(title="Saving Error", message="Unable to save file")
            print("Failed to save file ", filename)

    """word table contains a scrolled list, a frame for the total number of words in the text,
        a frame for the query of a rank of specific words, a frame for the zipfian probability mass function
        and a frame for the estimated occurrences and the corresponding deviation"""
    def buildWordTable(self):
        #  Table with word statistics
        self.wordFrame = ttk.Frame(self.anaFrame, width=10)
        self.wordFrame.pack(side=RIGHT, anchor=N, padx=5, pady=20)

        # scrollable Table
        self.tableFrame = ttk.Frame(self.wordFrame)
        self.tableFrame.pack(side=TOP, fill=BOTH)
        self.listNodes = Listbox(self.tableFrame, width=50, height=20, font=("Helvetica", 10))
        self.listNodes.pack(side=LEFT, anchor=N, fill="y")

        self.scrollbar = Scrollbar(self.tableFrame, orient="vertical")
        self.scrollbar.config(command=self.listNodes.yview)
        self.scrollbar.pack(side=RIGHT, anchor=N, fill="y")
        self.listNodes.config(yscrollcommand=self.scrollbar.set)

        # total words
        totalWordsFrame = ttk.Frame(self.wordFrame)
        totalWordsFrame.pack(side=TOP, fill=BOTH)

        self.totalWordsLabel = ttk.Label(totalWordsFrame, text='Total Word Number: 0')
        self.totalWordsLabel.pack(side=TOP, anchor=W, fill="y")
        self.updateTable()  # update table and full count on startup

        # query for specific word
        self.queryFrame = ttk.Frame(self.wordFrame)
        self.queryFrame.pack(side=TOP, anchor=W, fill=BOTH)
        queryLabel1 = ttk.Label(self.queryFrame, text='Word Occurrences for: ')
        queryLabel1.pack(side=LEFT, anchor=N, pady=6)
        queryEntry = ttk.Entry(self.queryFrame, width=10)
        queryEntry.bind('<Return>', lambda x: self.searchForWord(str(queryEntry.get()).casefold().strip()))
        queryEntry.pack(side=LEFT, anchor=N, pady=6)

        queryButton = ttk.Button(self.queryFrame, text='=>', width=2,
                                 command=lambda: self.searchForWord(str(queryEntry.get()).casefold().strip()))
        self.queryResult = ""
        self.queryResultText = Text(self.queryFrame, height=1, width=8)
        self.queryResultText.configure(state=DISABLED)
        self.queryResultText.pack(side=RIGHT, anchor=N, pady=5)
        queryButton.pack(side=RIGHT, anchor=N)

        #query: probability for rank
        self.rankProbFrame = ttk.Frame(self.wordFrame)
        self.rankProbFrame.pack(side=TOP, anchor=W, fill=BOTH)
        rankProbLabel = ttk.Label(self.rankProbFrame, text='Zipfian Probability for Rank: ')
        rankProbLabel.pack(side=LEFT, anchor=N, pady=6)
        rankEntry = ttk.Entry(self.rankProbFrame, width=3)
        rankEntry.bind('<Return>', lambda x: self.getProbZipf(int(rankEntry.get())))
        rankEntry.pack(side=LEFT, anchor=N, pady=6)

        rankButton = ttk.Button(self.rankProbFrame, text='=>', width=2,
                                 command=lambda: self.getProbZipf(int(rankEntry.get())))
        self.probResult = ""
        self.probResultText = Text(self.rankProbFrame, height=1, width=8)
        self.probResultText.configure(state=DISABLED)
        self.probResultText.pack(side=RIGHT, anchor=N, pady=5)
        rankButton.pack(side=RIGHT, anchor=N, padx=2)

        # frame for estimated occurrences
        self.estFrame = ttk.Frame(self.wordFrame)
        self.estFrame.pack(side=TOP, anchor=W, fill=BOTH)
        estimatedLabel = ttk.Label(self.estFrame, text='Estimated Occurrences: ')
        estimatedLabel.pack(side=LEFT, anchor=N, pady=6)
        self.estimatedResult = ""
        self.estimatedText = Text(self.estFrame, height=1, width=5)
        self.estimatedText.configure(state=DISABLED)
        self.estimatedText.pack(side=LEFT, anchor=N, padx=5, pady=5)

        deviationLabel = ttk.Label(self.estFrame, text='Deviation: ')
        deviationLabel.pack(side=LEFT, anchor=N, pady=6, padx=5)
        self.deviationResult = ""
        self.deviationResultText = Text(self.estFrame, height=1, width=8)
        self.deviationResultText.configure(state=DISABLED)
        self.deviationResultText.pack(side=LEFT, anchor=N, padx=5, pady=5)

    """ reloads table with freshly calculated values
        reloads label under table with total number of words"""
    def updateTable(self):
        # get TextStats
        self.n,self.W = self.fileAna.textStats(self.currFile, True)
        # fill table
        self.listNodes.delete(0,END)
        self.sortedW=dict()
        self.sortedW= self.fileAna.sortTextStats(self.W)
        i = 0
        self.rankedWordCount=0
        # get value - occurrences mapping:
        self.valOcc = dict()
        for k,v in self.sortedW:
            if(i>=self.limit):
                break
            i+=1
            self.rankedWordCount+=v
            self.valOcc[i]=v
            output = "{0}:  {1}  {2}  ".format(i, k, v)
            self.listNodes.insert(END,output)
            if(str(k)[0].isupper()):
                self.listNodes.itemconfig(i-1,{'fg':'purple'})
        wordCountOutput = "----------"
        self.listNodes.insert(END, wordCountOutput)
        wordCountOutput = "WORDCOUNT:  {0}".format(self.rankedWordCount)
        self.listNodes.insert(END, wordCountOutput)
        wordCountOutput = "----------"
        self.listNodes.insert(END, wordCountOutput)
        self.listNodes.pack(side="left", fill="y")
        self.scrollbar.configure(command=self.listNodes.yview)
        # fill label with total number of words
        totalWordsNr="Total Word Number:  {0}".format(self.n)
        self.totalWordsLabel.config(text=totalWordsNr)
        self.totalWordsLabel.pack(side=TOP, anchor=W, fill="y")

    """ query for word in file"""
    def searchForWord(self, query):
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
        self.queryResultText.pack(side=RIGHT, anchor=N, pady=5)

    """saves table in a .txt-file"""
    def saveTableAsTxt(self):
        # get values
        i = 0
        outputTxt=""
        for k, v in self.sortedW:
            if (i >= self.limit):
                break
            i = i + 1
            outputTxt += "{0}:\t{1}\t{2}\n".format(i, k, v)
        # write into file
        try:
            filename = str(self.currFile).replace(".txt","_table.txt")
            f = open(filename, 'w')
            f.write(outputTxt)
            f.close
            print("File ", filename, " is saved")
        except:
            tk.messagebox.showerror(title="Saving Error", message="Unable to save file")
            print("Failed to save file ", filename)

    """calculates the slope of the deviation using linear regression analysis
        plots in a double linear graph"""
    def calcSlope(self):
        slope = self.MathAna.linRegSlope(self.x, self.y, self.x.size)
        # remove old calculation
        if(self.slopeVar==1):
            self.graph.pop(0).remove()
            self.a.set_xscale('log')
            self.a.set_yscale('log')
            self.canvas.draw()
            self.textSlope.config(state=NORMAL)
            self.textSlope.delete(1.0, tk.END)
            self.textSlope.config(state=DISABLED)
            self.slopeVar=0
            self.slopeCheck.deselect()
            print("Slope removed")
        # activate slope
        elif(self.slopeVar==0):
            startx=self.x[0]; endx=self.x[-1:]
            starty=self.y[0]; endy=starty+self.x[self.x.size-1]*slope
            # draw
            self.graph = self.a.plot([startx, endx],[starty,endy], color='b')
            self.a.set_xscale('linear')
            self.a.set_yscale('linear')
            self.canvas.draw()
            # numerical slope
            self.textSlope.config(state=NORMAL)
            slopeVal="Slope: {0}".format(slope)
            self.textSlope.insert(tk.END, slopeVal)
            self.textSlope.config(state=DISABLED)
            self.slopeVar=1
            self.slopeCheck.select()
            print("Slope activated")
        return slope

    """calculates the zipfian exponent"""
    def calcExpZipf(self):
        expZipf = self.MathAna.exponentZipf(self.x, self.y, self.x.size)
        if (self.expVar == 1):
            self.textExp.config(state=NORMAL)
            self.textExp.delete(1.0, tk.END)
            self.textExp.config(state=DISABLED)
            self.expVar = 0
            self.exponentCheck.deselect()
            print("Exponent of Zipf-Distribution removed")
            # activate exponent
        elif (self.expVar == 0):
            # numerical slope
            self.textExp.config(state=NORMAL)
            expVal = "Zipf-Exponent: {0}".format(expZipf)
            self.textExp.insert(tk.END, expVal)
            self.textExp.config(state=DISABLED)
            self.expVar = 1
            self.exponentCheck.select()
            print("Exponent of Zipf-Distribution activated")
        return expZipf

    "set fields for Zipf-Probability-Mass-Function, estimated Occurrences, deviation"
    def getProbZipf(self, rank):
        if(self.x.size< self.limit):
            self.limit=self.x.size
        probResult, probResultPercentage= self.MathAna.pmfZipf(rank, self.limit, self.x, self.y)
        rank1, estOccurrences = self.MathAna.estOccurrences(rank, self.rankedWordCount, probResult)
        deviation, deviationPercentage, zipfy = self.MathAna.estToRealOccurrences(rank, self.valOcc.get(rank), estOccurrences, self.rankedWordCount)
        # probability
        if 'e' in str(probResult):
            probability = probResult
        else:
            probability = probResultPercentage
        self.probResultText.config(state=NORMAL)
        self.probResultText.delete(1.0, END)
        self.probResultText.insert(tk.END, probability)
        self.probResultText.config(state=DISABLED)
        self.probResultText.pack(side=RIGHT, anchor=N, pady=5)
        # estimated occurrences
        self.estimatedText.config(state=NORMAL)
        self.estimatedText.delete(1.0, END)
        self.estimatedText.insert(tk.END, estOccurrences)
        self.estimatedText.config(state=DISABLED)
        self.estimatedText.pack(side=LEFT, anchor=N, padx=5, pady=5)
        # deviation
        if 'e' in str(deviation):
            deviationResult = deviation
        else:
            deviationResult = deviationPercentage
        self.deviationResultText.config(state=NORMAL)
        self.deviationResultText.delete(1.0, END)
        self.deviationResultText.insert(tk.END, deviationResult)
        self.deviationResultText.config(state=DISABLED)
        self.deviationResultText.pack(side=LEFT, anchor=N, padx=5, pady=5)