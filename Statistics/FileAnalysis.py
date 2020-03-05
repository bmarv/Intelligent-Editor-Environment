__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

import getpass
import re

"""Analysis of the current File regarding the author of the text, the number of words 
    and the mapping of words to their occurrences"""
class FileAnalysis:
    def __init__(self):
        global author, wordList


    """determines user of Windows/Unix System"""
    def getAuthor(self):
        self.author = getpass.getuser()
        return self.author

    """gets words from input string and returns List of words"""
    def splitstring(self, textInput):
        self.wordList = re.split(r'[\.\,\;\s\:\"\!\?]\s*', str(textInput))
        return self.wordList

    """input file to count including words,
        returns number or Words, Dictionary(key: string word, value: int occurrences)"""
    def textStats(self, file, ReturnDict=False):
        # read file and save input in List
        print(file)
        f= open(file, mode='r')
        fileContent = f.read()
        currWordList = self.splitstring(fileContent)
        # count words
        wordDict=dict(); fullwordList=[]; upperWords=[]
        if(ReturnDict==True):
            for word in currWordList:
                if word.isalpha():
                    fullwordList.append(word)
                    # only get Eigennamen and Nomen through firstly checking all lowercase words and checking the remaining upper case letters afterwards
                    if(word[0].isupper()):
                        upperWords.append(word)
                        continue
                    # increment when already found in text
                    if word.casefold() in wordDict:
                        wordDict[word.casefold()]+=1
                    else:
                        wordDict[word]=1
                # special case: apostrophe in word
                elif "\'" in word:
                    fullwordList.append(word)
                    if word.casefold() in wordDict:
                        wordDict[word.casefold()]+=1
                    else:
                        wordDict[word]=1
            for word in upperWords:
                if word.casefold() in wordDict:
                    wordDict[word.casefold()]+=1
                elif word in wordDict:
                    wordDict[word]+=1
                else:
                    wordDict[word]=1
        wordOccurrences = len(fullwordList)
        return wordOccurrences, wordDict

    """sorts a list starting with the highest number of occurrences using lambda expression"""
    def sortTextStats(self, List):
        return sorted(List.items(), key=lambda x: x[1], reverse=True)