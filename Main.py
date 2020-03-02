#!/usr/bin/env python
__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

""" Intelligent Editor Environment
    Main-Class for Invoking an Instance of the Program
"""

from Basic_Gui import WindowInstance as WinInstance

global instance

if __name__ == "__main__":
    print("Starting IEE")
    instance = WinInstance.WindowInstance()
    instance.newInstance()
