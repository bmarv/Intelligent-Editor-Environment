__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

import re

"""Calculation of the Statistics of the current Textfile regarding the letter-, word-, sentence- and linescount"""
class TextinputStatistics:
    def __init__(self):
        global letterNumber
        global wordNumber
        global sentenceNumber
        global linesNumber

    """ count letters"""
    def countLetters(self, extText):
        self.letterNumber = len(extText)-1
        print("letternumber:\t",self.letterNumber)
        return self.letterNumber

    """count words"""
    def countWords(self, extText):
        # split string for blank spaces and interpunction
        splittedpunctuation = re.split(r'[\.\,\;\s\:\"\!\?]\s*', str(extText))
        # include only alphabetic-elements in array
        splittedWords = []
        for el in splittedpunctuation:
            if el.isalpha():
                splittedWords.append(el)
            elif "\'" in el:
                splittedWords.append(el)
        # count array of words
        self.wordNumber = len(splittedWords)
        print("wordnumber:\t", self.wordNumber)
        return self.wordNumber

    """count sentences"""
    def countSentences(self, extText):
        # split extText for punctuation
        extText = re.sub("(\.(\.)+)","",str(extText))
        extText = re.sub("\\n","",str(extText))
        splittedPunctuation = re.split(r'[.!?]+', extText)
        self.sentenceNumber = len(splittedPunctuation)-1
        print("sentencenumber:\t", self.sentenceNumber)
        return self.sentenceNumber

    """count Lines"""
    def countLines(self, extText):
        # split for newlines
        splittedLines = str(extText).split("\n")
        self.linesNumber = len(splittedLines)-1
        print("linesnumber:\t", self.linesNumber)
        return self.linesNumber