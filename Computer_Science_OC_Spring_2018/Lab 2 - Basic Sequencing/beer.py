#Author: Trevor Martin
#Date of Completion: 20 February 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Very Easy

NUM_BOTTLES=100

a="bottles of beer on the wall"
b="bottles of beer!"
c="Take one down, pass it around"

for bottles in range(1, NUM_BOTTLES+1):
    NUM_BOTTLES=NUM_BOTTLES-1
    print(NUM_BOTTLES,a,"\n",NUM_BOTTLES,b,"\n",c,"\n",NUM_BOTTLES,a,"!")
