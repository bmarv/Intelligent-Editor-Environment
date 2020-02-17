"author: Marvin Beese"
from Statistics import FileAnalysis
import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from ttkthemes import ThemedTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

class AnalysisFrame():
    def __init__(self, file):
        global currFile, fileAna
        self.currFile=file
        self.fileAna = FileAnalysis.FileAnalysis()
        global anaFrame, stylettk
        global plotterFrame, refreshPlotButton, plot, plot, a, canvas, b, graph, fig, scatterValue, x, y, word, x1,y1, word1, limit
        self.limit=50
        global checkFrame, textFrame, graphCheck, slopeCheck, exponentCheck, graphVar, slopeVar, expVar, textGraph, textSlope, textExp
        self.slopeVar=0; self.graphVar=0; self.expVar=0
        global tableFrame, refreshTableButton, listNodes, scrollbar, wordFrame, queryFrame, queryResult, queryResultText, totalWordsLabel
        global n, W, sortedW
        self.n, self.W = self.fileAna.textStats(self.currFile, True)

    def launchAnalysis(self):
        print("launching Analysis Frame")
        self.anaFrame = ThemedTk(theme='arc')
        title="IEE - Text Analysis for", os.path.basename(self.currFile)
        self.anaFrame.title(title)
        self.anaFrame.geometry("800x600")
        self.stylettk = ttk.Style()

        # menubar
        menubar = tk.Menu(self.anaFrame)
        plottingMenu = tk.Menu(menubar)
        plottingMenu.add_command(label='Refresh Plot', command=lambda: self.buildPlot(self.limit), accelerator="Ctrl+P")
        self.anaFrame.bind_all("<Control-p>", lambda x: self.buildPlot(self.limit))
        plottingMenu.add_command(label='Calculate Slope', command=lambda: self.calculateSlope(), accelerator="Ctrl+S")
        self.anaFrame.bind_all("<Control-s>", lambda x: self.calculateSlope())
        plottingMenu.add_command(label='Calculate Exponent')
        plottingMenu.add_separator()
        plottingMenu.add_command(label='Calculate Table', command=lambda: self.updateTable(), accelerator="Ctrl+T")
        self.anaFrame.bind_all("<Control-t>", lambda x: self.updateTable())
        plottingMenu.add_separator()
        plottingMenu.add_command(label='Exit Analysis', command= lambda:self.anaFrame.destroy(), accelerator="Ctrl+X")
        self.anaFrame.bind_all("<Control-x>", lambda x: self.anaFrame.destroy())
        menubar.add_cascade(label='Calculating', menu=plottingMenu)

        # menu for export
        outputMenu= tk.Menu(menubar)
        outputMenu.add_command(label='Save Plot as PDF', command=lambda: self.savePlotAsPDF(), accelerator="Ctrl+Shift+P")
        self.anaFrame.bind_all("<Control-P>", lambda x: self.savePlotAsPDF())
        outputMenu.add_command(label='Save Table as txt', command= lambda: self.saveTableAsTxt(), accelerator="Ctrl+Shift+T")
        self.anaFrame.bind_all("<Control-T>", lambda x: self.saveTableAsTxt())
        menubar.add_cascade(label='Export', menu=outputMenu)

        self.anaFrame.configure(menu=menubar)


        # plotting area
        self.buildPlotterFrameTop()
        self.buildPlot(self.limit)

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

        self.totalWordsLabel=ttk.Label(totalWordsFrame, text='Total Word Number (Duplicates resolved): 0')
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
        totalWordsNr="Total Word Number:",self.n
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
        self.sortedW = dict()
        self.sortedW = self.fileAna.sortTextStats(self.W)
        x=np.array([])
        y=np.array([])
        word=np.array([])
        i = 0
        for k,v in self.sortedW:
            if (i >= max):
                break
            i+=1
            x= np.append(x,i)
            y=np.append(y,v)
            word= np.append(word, k)
        return x,y,word


    def buildPlot(self, max):
        self.limit = max
        self.plotterFrame.destroy()
        self.buildPlotterFrameTop()
        self.fig = Figure(figsize=(4, 4), dpi=100)
        self.a = self.fig.add_subplot(111)
        # get values
        self.x, self.y, self.word = self.calcPlot(max)
        self.a.scatter(self.x, self.y, color='red')

        for i, txt in enumerate(self.word):
            self.a.annotate(txt, (i + 1, self.y[i]), xycoords='data')

        self.a.set_title("Most frequent Words", fontsize=16)
        self.a.set_ylabel("Occurrences", fontsize=8)
        self.a.set_xlabel("Word", fontsize=8)
        self.a.grid(True)
        self.a.set_xscale('log')
        self.a.set_yscale('log')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plotterFrame)
        self.canvas.get_tk_widget().pack(expand=True)
        # navigation bar
        toolbar= NavigationToolbar2Tk(self.canvas, self.plotterFrame)
        toolbar.update()
        self.canvas.draw()
        self.buildPlotterFrameBottom()
        # deselect gradient
        self.slopeVar = 0
        self.slopeCheck.deselect()


    # builds toplevel frame for plotting, builds part above plot (refresh button)
    def buildPlotterFrameTop(self):
        self.plotterFrame = ttk.Frame(self.anaFrame, width=400)
        self.plotterFrame.pack(side=LEFT, anchor=N, padx=10, pady=20)
        # set value for visualisation
        self.w2 = Scale(self.plotterFrame, from_=0, to=self.n, orient=HORIZONTAL, length=400, label="Number of Words")
        self.w2.set(self.limit)
        # refresh
        self.refreshPlotButton = ttk.Button(self.plotterFrame, text='Refresh Plot', width=13, command=lambda: self.buildPlot(self.w2.get()))
        self.refreshPlotButton.pack(side=TOP, anchor=W)
        self.w2.pack(side=TOP, padx=5)

    # builds part underneath plot (check buttons, textfields)
    def buildPlotterFrameBottom(self):
        # checkbutton frame
        self.checkFrame = ttk.Frame(self.plotterFrame, width=10)
        self.checkFrame.pack(side=LEFT, anchor=N)
        self.slopeCheck = Checkbutton(self.checkFrame, text='Slope', variable=self.slopeVar, command= lambda: self.calculateSlope())
        self.slopeCheck.pack(side=TOP, anchor=W)
        self.exponentCheck = Checkbutton(self.checkFrame, text='Exponent', variable=self.expVar, command= lambda: self.calculateExp())
        self.exponentCheck.pack(side=TOP, anchor=W)

        self.textFrame = ttk.Frame(self.plotterFrame, width=20)
        self.textFrame.pack(side=LEFT, anchor=N)
        self.textSlope = Text(self.textFrame, width=30, height=1)
        self.textSlope.config(state=DISABLED)
        self.textSlope.pack(side=TOP)
        self.textExp = Text(self.textFrame, width=30, height=1)
        self.textExp.pack(side=TOP)

    def calculateSlope(self):
        slope, intercept = np.polyfit(self.x, self.y, 1)
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
            startx=0; endx=self.x[-1:]
            starty=intercept; endy=intercept+self.x[-1:]*slope
            # draw
            self.graph = self.a.plot([startx, endx],[starty,endy], color='b')
            self.a.set_xscale('linear')
            self.a.set_yscale('linear')
            self.canvas.draw()
            # numerical slope
            self.textSlope.config(state=NORMAL)
            slopeVal="Slope: ", slope
            self.textSlope.insert(tk.END, slopeVal)
            self.textSlope.config(state=DISABLED)
            self.slopeVar=1
            self.slopeCheck.select()
            print("Slope activated")
        return slope, intercept

    # TODO: calculate exponent of distribution
    def calculateExp(self):
        raise NotImplementedError

    def savePlotAsPDF(self):
        filename= str(self.currFile).replace(".txt","_plot.pdf")
        try:
            self.fig.savefig(filename)
            print("plot saved as pdf in ", filename)
        except:
            tk.messagebox.showerror(title="Saving Error", message="Unable to save file")
            print("Failed to save file ", filename)

    def saveTableAsTxt(self):
        # get values
        i = 0
        outputTxt=""
        for k, v in self.sortedW:
            if (i >= 100):
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