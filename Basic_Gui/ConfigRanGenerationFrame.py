#!/usr/bin/env python
__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

import tkinter as tk
import os
from tkinter import ttk
from ttkthemes import ThemedTk
from Basic_Gui import WindowInstance

""" Frame for the Configuration of the Generation of a random text. 
    The text can be inserted to the end of the current document or into a new document.
"""
class ConfigRanGenerationFrame:
    def __init__(self):
        pass


    def launchWindow(self, file):
        # build frame
        print("Window launched: Configuration for Random Text-Generation")
        self.activeWindow = ThemedTk(theme='arc')
        self.activeWindow.title("Configuration for Random Text-Generation {0}".format(file))
        self.activeWindow.geometry('700x650')
        self.stylettk = ttk.Style()
        # build title
        self.buildTitleArea()
        # build probability
        self.buildProbabilityArea()
        # build linebreaks
        self.buildLineBreakArea()
        # build steps & start
        self.buildStepsArea()

        # close button triggered
        self.activeWindow.protocol("WM_DELETE_WINDOW", lambda: self.exitActivity())

        # mainloop
        self.activeWindow.mainloop()
        print("Config closed")

    def buildTitleArea(self):
        titleFrame = tk.Frame(self.activeWindow, height=100)
        titleFrame.pack(fill=tk.BOTH)
        titleLabel = tk.Label(titleFrame, text="Configuration for Random Text-Generation")
        titleLabel.config(font=('Verdana', 20))
        titleLabel.pack(side=tk.TOP, pady=50)

    """sets the probability of letter occurrences and calculates the probability of splitting occurrences"""
    def buildProbabilityArea(self):
        probabilityFrame = tk.Frame(self.activeWindow, height=100)
        probabilityFrame.pack(fill=tk.BOTH, pady=10)
        # letter
        letterFrame = tk.Frame(probabilityFrame, height=50)
        letterFrame.pack(fill=tk.BOTH, anchor=tk.N)
        letterLabel = tk.Label(letterFrame, text='Probability for Letters:')
        letterLabel.config(font=('Verdana', 15))
        letterLabel.pack(side=tk.LEFT,padx=20)
        letterEntry = ttk.Entry(letterFrame, width=8)
        letterEntry.bind('<Return>', lambda x: self.letterProbUpdated(float(letterEntry.get())))
        refreshLetterButton = ttk.Button(letterFrame, text='Continue', width=13,
                                            command=lambda: self.letterProbUpdated(float(letterEntry.get())))
        letterEntry.pack(side=tk.LEFT, padx=15)
        refreshLetterButton.pack(side=tk.RIGHT,padx=15)
        # splitting
        splittingFrame= tk.Frame(probabilityFrame, height=50)
        splittingFrame.pack(fill=tk.BOTH, anchor=tk.N)
        splittingLabel = tk.Label(splittingFrame, text='Probability for Space/Interpunction:')
        splittingLabel.config(font=('Verdana', 15))
        splittingLabel.pack(side=tk.LEFT, padx=20)
        self.splittingProba = ""
        self.splittingProbLabel = tk.Label(splittingFrame, text=self.splittingProba)
        self.splittingProbLabel.config(font=('Verdana', 8))
        self.splittingProbLabel.pack(side=tk.LEFT, padx=10)

    """splitting probability added based on letter probability"""
    def letterProbUpdated(self, letterProb):
        self.letterProba = letterProb
        self.splittingProba = round(1-self.letterProba,4)
        self.splittingProbLabel.config(text=self.splittingProba)
        self.splittingProbLabel.pack(side=tk.LEFT, padx=10)

    """sets the nummber of symbols before a linebreak periodically"""
    def buildLineBreakArea(self):
        linebreakFrame = tk.Frame(self.activeWindow, height=100)
        linebreakFrame.pack(fill=tk.BOTH, pady=10)
        linebreakLabel = tk.Label(linebreakFrame, text='Linebreaks after No. of Steps:')
        linebreakLabel.config(font=('Verdana', 15))
        linebreakLabel.pack(side=tk.LEFT, padx=20)
        linebreakEntry = ttk.Entry(linebreakFrame, width=8)
        linebreakEntry.bind('<Return>', lambda x: self.linebreakUpdate(int(linebreakEntry.get())))
        refreshlinebreakButton = ttk.Button(linebreakFrame, text='Continue', width=13,
                                         command=lambda: self.linebreakUpdate(int(linebreakEntry.get())))
        linebreakEntry.pack(side=tk.LEFT, padx=15)
        refreshlinebreakButton.pack(side=tk.RIGHT, padx=15)

    def linebreakUpdate(self, linebreakAfter):
        self.lineBreak = linebreakAfter

    """sets the number of characters in the output text"""
    def buildStepsArea(self):
        stepsFrame = tk.Frame(self.activeWindow, height=100)
        stepsFrame.pack(fill=tk.BOTH, pady=10)
        stepsLabel = tk.Label(stepsFrame, text='Stepsize / No. of Characters')
        stepsLabel.config(font=('Verdana', 15))
        stepsLabel.pack(side=tk.LEFT, padx=20)
        stepsEntry = ttk.Entry(stepsFrame, width=8)
        stepsEntry.bind('<Return>', lambda x: self.stepsUpdate(int(stepsEntry.get())))
        refreshStepsButton = ttk.Button(stepsFrame, text='Start Generation', width=13,
                                            command=lambda: self.stepsUpdate(int(stepsEntry.get())))
        stepsEntry.pack(side=tk.LEFT, padx=15)
        refreshStepsButton.pack(side=tk.RIGHT, padx=15)

    def stepsUpdate(self, stepsize):
        self.stepSize= stepsize
        self.getAttributes()
        self.exitActivity()

    def getAttributes(self):
        print("Letter-Probability ",self.letterProba,", Linebreak: ", self.lineBreak,", Stepsize: ", self.stepSize)
        self.writeToConfigFile()
        return self.letterProba, self.lineBreak, self.stepSize

    """exit activity: stops the mainloop and closes the window"""
    def exitActivity(self):
        self.activeWindow.quit() #stopping the mainloop
        self.activeWindow.destroy() #closing the window
        print("Configuration for Random Text-Generation closed!")

    """configuration saved in a config file for further calculations"""
    def writeToConfigFile(self):
        instance = WindowInstance.WindowInstance()
        currPath=instance.getGlobalPath()
        location = os.path.join(currPath,"RandomTextConfig.txt")
        file = open(location, "w")
        info= "{0} {1} {2}".format(self.letterProba, self.lineBreak, self.stepSize)
        file.write(info)
        file.close()

