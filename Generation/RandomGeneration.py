__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

import numpy as np
import string

""" Generation of random words and splitter (space and punctuation).
    The methods have been tested for their correctness with PyTest.
"""
class RandomGeneration:
    def __init__(self):
        pass

    def setAttributes(self, letterProb, lineBreak, stepSize):
        self.letterProb=letterProb
        self.lineBreak = lineBreak
        self.stepSize= stepSize

    """creates randomly a letter of the eng/ger alphabet"""
    def randomLetter(self):
        alphabetList = np.array(list(string.ascii_letters))
        germanLetters = np.array(['ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß'])
        alphabetList= np.concatenate((alphabetList, germanLetters), axis=None)
        letter = np.random.choice(alphabetList)
        return letter

    """creates randomly a space or punctuation"""
    def randomSplitter(self):
        splitSymb = np.array([' ',',','.',';',':','!','?']) #[\.\,\;\s\:\"\!\?]
        splitter = np.random.choice(splitSymb)
        return splitter

    """creates words and splitter depending on respective probability of given size. 
        Linebreaks are included after a given number of elements"""
    def randomTextGeneration(self, letterProb, linebreakNr, size):
        # Probabilities
        letterProbability = letterProb
        splitterProbability = 1-letterProbability
        linebreak = linebreakNr

        randomText=""
        for step in range (1,size+1):
            if(step%linebreak==0):
                randomText+="\n"
            else:
                letter=self.randomLetter()
                splitter=self.randomSplitter()
                choosenChar= np.random.choice([letter,splitter],1,p=[letterProbability, splitterProbability])
                randomText+=choosenChar[0]
        randomText = str(randomText)
        print(randomText)
        return randomText

