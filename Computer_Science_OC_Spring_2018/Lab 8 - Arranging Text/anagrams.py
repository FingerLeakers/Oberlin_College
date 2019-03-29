# Author: Trevor Martin
# Date of Completion: 17 April 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 8, anagrams.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program rearranges letters from a word or phrase into any new combination of words or phrases.
#===================================================================================================
# DEPENDENCIES
#===================================================================================================
import sys
#===================================================================================================

def main():
    soFar=[]
    words=set()
    fileName=sys.argv[2]
    string=sys.argv[1]
    contents=open(fileName,"r")
    lines=contents.readlines()
    for word in lines:
        strippedWord=word.strip()
        words.add(strippedWord)
    minLength=int(sys.argv[3])
    maxWords=int(sys.argv[4])
    grams(string,words,soFar, minLength, maxWords)
    contents.close()
    
def contains(bigWord, smallWord):
    tally=0
    small=len(smallWord)
    for letter in range(len(bigWord)):
        for instance in range(len(smallWord)):
            if bigWord[letter] == smallWord[instance] and tally<small:
               bigWord=bigWord.replace(bigWord[letter]," ",1)
               smallWord=smallWord.replace(smallWord[instance],"?",1)
               tally=tally+1
    if tally == small:
        bigWord=bigWord.replace(" ","")
        return True, bigWord
    else:
        return False, ""
    
def grams(bigWord,words,soFar, minLength, maxWords):
    if len(bigWord)==0:
        print(soFar)
    else:
        for word in words:
            truFalse,newBigWord=contains(bigWord,word)
            if truFalse==True and len(word) >= minLength and len(soFar) + 1 <= maxWords :
                newSoFar=list(soFar)
                newSoFar.append(word)
                grams(newBigWord,words,newSoFar,minLength,maxWords)
        
main()

