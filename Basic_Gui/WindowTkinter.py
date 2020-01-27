import tkinter as tk
from tkinter.scrolledtext import *
import Basic_Gui.Fileoperations as Fileoperations
from tkinter.filedialog import *
from tkinter import messagebox


class WindowTkinter:


    def __init__(self):
        global activeWindow
        global text
        self.launchWindow()


    def launchWindow(self):
        print("Window launched: Tkinter")
        fileOP = Fileoperations.Fileoperations()
        global activeWindow
        activeWindow = tk.Tk()
        activeWindow.title("Intelligent Editor Environment")
        activeWindow.geometry("800x600")
        # activeWindow.minsize(width=800, height=600)
        # activeWindow.maxsize(width=1920, height=1080)

        # get Menubar for basic actions
        menubar = tk.Menu(activeWindow)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label='New File', command=lambda: fileOP.newFile(text))
        fileMenu.add_command(label='Open', command=lambda: fileOP.openFile(text))
        fileMenu.add_command(label='Save', command=lambda: fileOP.saveFile(text))
        fileMenu.add_command(label='Save As', command=lambda: fileOP.saveAs(text))
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=activeWindow.quit)

        menubar.add_cascade(label='File', menu=fileMenu)
        activeWindow.config(menu=menubar)

        # frame for text
        textFrame = LabelFrame(activeWindow, text="Text-Input", relief='raised', width=800, height=400)
        textFrame.pack()

        #set ScrolledText-Field inside textFrame
        global text
        text = ScrolledText(textFrame, font='helvetica 12')
        text.pack()
        global filename

        # frame dividing statistics
        bottomFrame = Frame(activeWindow, width=800,height=200)
        bottomFrame.pack()

        # frame for statistics
        statsFrame = LabelFrame(bottomFrame, text="Statistics", relief='raised',width=800, height=100)
        statsFrame.pack()

        # set button and textview for textinput
        global calcStats
        calcStats = Button(statsFrame, text="Calculate", width=20, height=1)
        calcStats.pack(side=LEFT)
        global statsText
        statsText = Text(statsFrame,width=50, height=1)
        statsText.insert(tk.END, "lettercount: EMPTY \t word-count: EMPTY")
        statsText.pack(side=RIGHT)

        # frame for meta information
        metaFrame= LabelFrame(bottomFrame, text="Meta-Information", width=800, height=5)
        metaFrame.pack()

        # textview for metainformation
        global metaText
        metaText= Text(metaFrame, width=70, height=1)
        metaText.insert(tk.END, "Meta-Information: EMPTY")
        metaText.pack()


        # mainloop
        activeWindow.mainloop()
        print("Window closed")

    def getActiveWindow(self):
        return activeWindow

    def getActiveText(self):
        return text
