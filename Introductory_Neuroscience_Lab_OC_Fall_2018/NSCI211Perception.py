#Author: Trevor Martin
#Date of Completion: 3 December 2018
#Language: Python 3

import matplotlib.pyplot as plt
import numpy as np
import pylab
from scipy.optimize import curve_fit
#=======================================================================================================
trevor = [2,2,2,4,4,1,1,4,1,3,2,2,1,4,4,1]
berryB1=[2,1,3,1,1,2,3,1,1,2,1,1,2,1,2,1,1,2,1]
berryB2=[2, 2, 1, 3, 1, 4, 4, 3, 3, 1, 3, 4, 3, 1, 3, 2, 3, 3, 2]
berryB3=[2, 3, 3, 4, 2, 4, 4, 4, 3, 2, 2, 4, 5, 2, 5, 1, 3, 2, 3]
berryB4=[4, 3, 2, 2, 3, 5, 2, 2, 2, 4, 4, 3, 3 ,2, 4 ,4 ,3 ,2 ,3] 
berryB5=[4, 2, 2, 4, 2, 3, 3, 3, 2, 3, 2, 3, 5, 1, 3 ,3 ,4 ,1 ,2]
berryB6=[1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 2 ,1, 1, 1, 1]
berryB7=[1, 1, 1, 1, 1, 1, 1 ,2 ,2, 1, 1, 2, 1, 1, 3, 2 ,1 ,1, 1]
berryB8=[4 ,4, 2, 4, 3, 5, 2 ,4, 4, 5, 5, 3, 5, 3, 4, 3, 5 ,5, 5]
lemonB1=[1, 3, 3 ,1, 1, 2, 1, 2, 2, 1, 1, 3, 2, 1 ,4 ,1 ,2 ,1 ,2]
lemonB2=[3 ,4 ,3 ,2 ,3 ,4 ,1 ,2 ,2 ,3 ,2 ,2 ,3 ,2 ,3 ,4 ,2 ,4 ,3]
lemonB3=[2 ,1 ,1, 1, 1, 1 ,1, 2, 1, 2, 2, 1, 1, 1, 1, 4, 3, 1, 2]
lemonB4=[2 ,3 ,2 ,2 ,3 ,1 ,2 ,1 ,1 ,1 ,1 ,1 ,2 ,1, 1 ,1 ,2 ,5 ,2]
lemonB5=[1 ,1 ,1 ,1 ,1 ,1 ,1, 1, 1, 2, 2 ,2 ,1 ,1 ,1, 3 ,2, 2, 1]
lemonB6=[4 ,2 ,2 ,2 ,2 ,2 ,2 ,4, 3 ,4 ,4 ,4 ,3 ,2 ,4 ,4 ,3 ,2, 3]
lemonB7=[4 ,3 ,2 ,3 ,4 ,5 ,2 ,4 ,4 ,5 ,5 ,4 ,4 ,2 ,3 ,3 ,4 ,5 ,5]
lemonB8=[1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,2 ,2 ,1 ,1, 1]
#=======================================================================================================
def bTS(scoreList):
    dang = 0.000
    for bingus in range(len(scoreList)):
        dang = dang + scoreList[bingus]
    bottleTasteMean = dang/len(scoreList)
    return bottleTasteMean
#=======================================================================================================
def stdev(scoreList):
    sqrDiff = 0.000
    mean = bTS(scoreList)
    for i in range(len(scoreList)):
        sqrDiff += (i - mean)**2
    stdv = sqrDiff/(len(scoreList)-1)
    return np.sqrt(stdv)
#======================================================================================================= 
def sterr(scoreList):
    stdv = stdev(scoreList)
    sterr = stdv / np.sqrt(len(scoreList))
    return sterr
#=======================================================================================================
plt.figure(figsize = (7,7))

line,caps,bars=plt.errorbar([1,2,3,4,5,6,7,8],     
        [bTS(berryB1),bTS(berryB2),bTS(berryB3),bTS(berryB4),bTS(berryB5),bTS(berryB6),bTS(berryB7),bTS(berryB8)],
        yerr=[sterr(berryB1),sterr(berryB2),sterr(berryB3),sterr(berryB4),sterr(berryB5),sterr(berryB6),sterr(berryB7),sterr(berryB8)],        
        fmt = "gs--", linewidth=2,elinewidth=0.6,ecolor='green',capsize=8,capthick=0.5)

line2,caps2,bars2=plt.errorbar([1,2,3,4,5,6,7,8],     
        [bTS(lemonB1),bTS(lemonB2),bTS(lemonB3),bTS(lemonB4),bTS(lemonB5),bTS(lemonB6),bTS(lemonB7),bTS(lemonB8)],    
        yerr=[sterr(lemonB1),sterr(lemonB2),sterr(lemonB3),sterr(lemonB4),sterr(lemonB5),sterr(lemonB6),sterr(lemonB7),sterr(lemonB8)],
        fmt = "bs--",linewidth=2,elinewidth=0.6,ecolor='blue',capsize=8,capthick=0.5)

line3 = plt.plot([1,2,3,4,5,6,7,8],[2,2,2,4,4,1,1,4],linewidth=2,color='green')

line4 = plt.plot([1,2,3,4,5,6,7,8], [1,3,2,2,1,4,4,1],linewidth=2,color='blue')

plt.setp(line,label="Berryness Rating")

plt.setp(line2,label="Lemonness Rating")

plt.setp(line3,label="Trevor's Berry Rating")

plt.setp(line4,label="Trevor's Lemon Rating")

plt.rc('font',family = 'Times New Roman')

plt.legend(numpoints=2,loc=('upper left'))

plt.xlim((0,9))                 

plt.xticks([1,2,3,4,5,6,7,8],["1\nSweet\nNoSmell\nYellow","2\nSour\nStrawBry\nRed","3\nSour\nNoSmell\nRed","4\nSweet\nLemon\nYellow","5\nSour\nNoSmell\nYellow","6\nSweet\nNoSmell\nRed","7\nSweet\nStrawBry\nRed","8\nSour\nLemon\nYellow"])

plt.yticks([1,2,3,4,5])

plt.xlabel('Drink Number (1 --> 8)', fontname = "Times New Roman",fontsize = 12)

plt.ylabel('Score Rating', fontname = "Times New Roman",fontsize = 12)

plt.title("Gustation/Olfaction Lab", fontname = "Times New Roman")

plt.show()


