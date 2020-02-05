"author: Marvin Beese"
from Basic_Gui import WindowInstance as instance
from Basic_Gui import WindowTkinter
import tkinter as tk
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from tkinter import ttk
from ttkthemes import ThemedTk

class AnalysisFrame():
    def __init__(self):
        global anaFrame, stylettk
        global plotterFrame, refreshPlotButton, plot
        global checkFrame, textFrame, graphCheck, gradientCheck, exponentCheck, graphVar, gradientVar, expVar, textGraph, textGradient, textExp
        global tableFrame, refreshTableButton, Table

    def launchAnalysis(self):
        print("launching Analysis Frame")
        self.anaFrame = ThemedTk(theme='radiance')
        self.anaFrame.title("IEE - Text Analysis")
        self.anaFrame.geometry("800x600")
        self.stylettk = ttk.Style()

        # menubar
        menubar = tk.Menu(self.anaFrame)
        # TODO: menu for plotting
        plottingMenu = tk.Menu(menubar)
        plottingMenu.add_command(label='Refresh Graphs')
        plottingMenu.add_command(label='Plot Gradient')
        plottingMenu.add_command(label='Calculate Exponent')
        plottingMenu.add_separator()
        plottingMenu.add_command(label='Calculate Table')
        menubar.add_cascade(label='Calculating', menu=plottingMenu)

        # TODO: menu for output as .txt file
        outputMenu= tk.Menu(menubar)
        outputMenu.add_command(label='Save Plot as PDF')
        outputMenu.add_command(label='Save Table as .txt')
        menubar.add_cascade(label='Saving Tools', menu=outputMenu)

        self.anaFrame.configure(menu=menubar)
        # TODO: plotter on left side
        # TODO: Button plot gradient, calculate exponent of distribution
        self.plotterFrame = ttk.Frame(self.anaFrame, width=400)
        self.plotterFrame.pack(side=LEFT, anchor=N)
        # refresh
        self.refreshPlotButton = ttk.Button(self.plotterFrame, text='Refresh Plot', width=13)
        self.refreshPlotButton.pack(side=TOP, anchor=NW)
        # plotting area
        self.plot = Text(self.plotterFrame, width = 50)
        self.plot.pack(side=TOP)
        # TODO: checkbox and textfield for graph, gradient, distribution
        # checkbutton frame
        self.checkFrame= ttk.Frame(self.plotterFrame, width=10)
        self.checkFrame.pack(side=LEFT, anchor=N)
        self.graphVar = IntVar()
        self.graphCheck = Checkbutton(self.checkFrame, text='Graph', variable=self.graphVar)
        self.graphCheck.pack(side=TOP,anchor=W)
        self.gradientVar= IntVar()
        self.gradientCheck = Checkbutton(self.checkFrame, text='Gradient', variable=self.gradientVar)
        self.gradientCheck.pack(side=TOP, anchor=W)
        self.expVar=IntVar()
        self.exponentCheck = Checkbutton(self.checkFrame, text='Exponent', variable=self.expVar)
        self.exponentCheck.pack(side=TOP, anchor=W)
        # textbox frame
        self.textFrame= ttk.Frame(self.plotterFrame, width=20)
        self.textFrame.pack(side=LEFT, anchor=N)
        self.textGraph = Text(self.textFrame, width=20, height=1)
        self.textGraph.pack(side=TOP)
        self.textGradient = Text(self.textFrame, width=20, height=1)
        self.textGradient.pack(side=TOP)
        self.textExp = Text(self.textFrame, width=20, height=1)
        self.textExp.pack(side=TOP)
        # TODO: text statistics from WindowInstance
        self.tableFrame = ttk.Frame(self.anaFrame, width=10)
        self.tableFrame.pack(side=RIGHT, anchor=N)
        self.refreshTableButton = ttk.Button(self.tableFrame, text='Refresh Table', width=13)
        self.refreshTableButton.pack(side=TOP, anchor=NW)
        # plotting area
        self.table = Text(self.tableFrame, width=50)
        self.table.pack(side=TOP)
        # TODO: scrollable Table
        # TODO: Textbox for graph, gradient, exponent

        self.anaFrame.mainloop()
        print("Analysis Frame closed")