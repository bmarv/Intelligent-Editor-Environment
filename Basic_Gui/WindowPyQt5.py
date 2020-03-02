__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

""" PyQt5 is GUI-Framework
    The Development with that has been discontinued due to extreme Performance-Problems
    compared with Tkinter
"""
# import Basic_Gui.Fileoperations as Fileoperations
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QWidget, QPushButton, QVBoxLayout
# import sys
#
# """ window implementation with pyqt5
# missing implementation: actions for fileoperations, Textedit, fields for statistics and interaction
# """
# class WindowPyQt5():
#     def __init__(self):
#         global app
#         app = QApplication(sys.argv)
#         global win
#         win = QMainWindow()
#         self.window()
#
#
#     def window(self):
#         win.setGeometry(200, 200, 300, 300)
#         win.setWindowTitle("Intelligent Editor Env")
#
#         # Menu Bar
#         menuBar = win.menuBar()
#         fileMenu = menuBar.addMenu('File')
#         editMenu = menuBar.addMenu('Edit')
#
#         # actions for menus
#         newFileAction = QAction("New File")
#         newFileAction.setShortcut("Ctrl+N")
#
#         saveAction = QAction('Save')
#         saveAction.setShortcut('Ctrl+S')
#
#         quitAction = QAction('Quit')
#         quitAction.setShortcut('Ctrl+Q')
#
#         findAction = QAction('Find')
#         findAction.setShortcut('Ctrl+F')
#
#         fileMenu.addAction(newFileAction)
#         fileMenu.addAction(saveAction)
#         editMenu.addAction(findAction)
#         fileMenu.addAction(quitAction)
#
#         # events for menus
#         quitAction.triggered.connect(lambda: self.quitApp())
#
#         # build Notepad
#         self.textEdit = QtWidgets.QTextEdit()
#         self.textEdit.move(150,80)
#         # self.textEdit.acceptRichText(False)
#         self.clr_btn = QPushButton("Clear")
#
#         # init Notepad-ui
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.textEdit)
#         layout.addWidget(self.clr_btn)
#
#         win.setLayout(layout)
#
#
#         # label = QtWidgets.QLabel(win)
#         # label.setText("my first label")
#         # label.move(50,50)
#
#         win.show()
#         print("Window launched: PyQt5")
#         sys.exit(app.exec_())
#
#
#
#
#     def quitApp(self):
#         print("Window closed")
#         self.app.quit()
