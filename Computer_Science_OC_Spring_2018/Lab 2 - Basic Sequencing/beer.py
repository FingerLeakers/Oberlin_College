# Author: Trevor Martin
# Date of Completion: 20 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 2, beer.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# Prints the "n bottles of beer on the wall" song
#===================================================================================================

BOTTLES = 100

line_1 = " bottles of beer on the wall"
line_2 = " bottles of beer!"
line_3 = "Take one down, pass it around"

for a_bottle in range(1, BOTTLES + 1):
    BOTTLES = BOTTLES - 1
    print(BOTTLES,line_1,"\n",BOTTLES,line_2,"\n",line_3,"\n",BOTTLES,line_1,"!",sep="")
