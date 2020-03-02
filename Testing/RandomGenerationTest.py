__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

import unittest
import re
from Generation import RandomGeneration

class MyTestCase(unittest.TestCase):

    RandomGen = RandomGeneration.RandomGeneration()

    # randomLetter: single german/english letter
    def testRandomLetter(self):
        letterPattern = re.compile('[a-zA-ZäöüßÄÖÜ]')
        randomLetter = self.RandomGen.randomLetter()
        assert letterPattern.fullmatch(randomLetter)!=None

        # randomSplitter: single splitter
    def testRandomSplitter(self):
        splitterPattern = re.compile('[\.\,\;\s\:\"\!\?]')
        randomSplitter= self.RandomGen.randomSplitter()
        assert splitterPattern.fullmatch(randomSplitter)!=None

    def testGenerationLength(self, letterProb=0.9, linebreakNr=50, size = 20000):
        randomWord=self.RandomGen.randomTextGeneration(letterProb,linebreakNr,size)
        assert len(randomWord) == size

if __name__ == '__main__':
    unittest.main()
