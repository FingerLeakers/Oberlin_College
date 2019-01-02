#Author: Trevor Martin
#Date of Completion: 16 March 2018
#Data of Edits: 2 January 2019
#Language: Python 3
#Difficulty: Medium 

print("In this game there is a 4 letter code made from 6 colors.\n", "The colors are R(red), G(green), B(brown), Y(yellow), P(purple), or O(orange).\n", "Try to guess the color sequence; you have 10 guesses, and a white pegs means\n you got a color correct but in the wrong space and a black peg\n means you got a correct color in the correct place. Good luck.", sep=" ")

import random

#This program randonly generates codemaker's code.
def generateCode():
    Colors=["R","G","O","B","Y","P"]
    Color1=random.randint(1,6)
    Color2=random.randint(1,6)
    Color3=random.randint(1,6)
    Color4=random.randint(1,6)
    Code=""
    for i in range(1,5):
        Color1=random.randint(1,6)
        Code=Code+Colors[Color1-1]
    return Code

def codeAndGuess(Code):
    NUM_TURNS=0
    done=False
    while not done and NUM_TURNS<10:
        black=0
        white=0
        Guess=input(str("What's your guess:"))
        NewGuess=Guess
        NewCode=Code
        if NewGuess==Code:
            print("You got it friend")
            done=True
        else:
            NUM_TURNS=NUM_TURNS+1
            CurrentTurns=10-NUM_TURNS
            for i in range(len(NewGuess)):
                if NewGuess[i]==NewCode[i]:
                    black=black+1
                    NewGuess=NewGuess[0:i]+"x"+NewGuess[i+1:]
                    NewCode=NewCode[0:i]+"z"+NewCode[i+1:]
            for i in range(len(NewGuess)):
                for j in range(len(NewGuess)):
                    if NewGuess[j]!="x" and NewGuess[j]==NewCode[i]:
                        white=white+1
                        NewGuess=NewGuess[0:j]+"y"+NewGuess[j+1:]
                        NewCode=NewCode[0:i]+"w"+NewCode[i+1:]
  
        print("Your Guess:",Guess,"\nTry again you got it wrong. \nYou have",CurrentTurns,"guesses remaining. You also have",white,"white pegs and",black,"black pegs.")
        
def main():
    Code=generateCode()
    codeAndGuess(Code)

main()


    












