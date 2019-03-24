#Author: Trevor Martin
#Date of Completion: 25 November 2018
#Language: Python 3

import matplotlib.pyplot as plt
import numpy as np
import pylab
from scipy.optimize import curve_fit
#=======================================================================================================
def standardError():
    
    line,caps,bars=plt.errorbar([100,80,50,40,32,20],[32.1,26.7,21.3,8.2,4.3,1.1],
        yerr=[4.5,5,6.7,3.2,1.9,0.8],
        fmt = "rs--",linewidth=2,elinewidth=0.5,ecolor='red',capsize=8,capthick=0.5)
    
    line2,caps2,bars2=plt.errorbar([100,80,50,40,32,20],[35.7,37.5,31.1,27.2,24.3,17.4],
        yerr=[5.8,4.3,6.2,5.8,7.3,7.3],       
        fmt = "gs--",linewidth=2,elinewidth=0.6,ecolor='green',capsize=8,capthick=0.5)

    plt.setp(line2,label="With Amphetamine")
    
    plt.setp(line,label="Without Amphetamine")

    plt.rc('font',family = 'Times New Roman')
    
    plt.legend(numpoints=2,loc=('upper left'))
    
    plt.xlim((0,120))
    
    plt.xticks([100,80,50,40,32,20])
    
    plt.yticks([0,5,10,15,20,25,30,35,40,45])
    
    plt.xlabel('Hz Frequency', fontname = "Times New Roman",fontsize = 12)
    
    plt.ylabel('Number of Bar Presses per Minute', fontname = "Times New Roman",fontsize = 12)
    
    plt.title("NSCI 211 ISCC Lab", fontname = "Times New Roman")
    
    plt.show()
#=======================================================================================================
def sigmoid(x, b, a):
    y = 40 / (1 + np.exp(-a*(x-b)))
    return y 
#=======================================================================================================
def sigmoidal():
    
    xdata = np.array([20,32,40,50,80,100])
    
    ydata = np.array([1.1,4.3,8.2,21.3,26.7,32.1])

    ydata2 = np.array([17.4,24.3,27.2,31.1,37.5,35.7])
    
    popt, pcov = curve_fit(sigmoid, xdata, ydata, method ='dogbox')
    
    popt2, pcov2 = curve_fit(sigmoid, xdata, ydata2, method ='dogbox')
    #print popt
    x = np.linspace(-1, 120)
    #print("This is the sigmoidal equations y = 40 / (1 + np.exp(-a*(x-b)))")
    y = sigmoid(x, *popt)
    #print ("These are the values forf the No Drug Condition:", x, popt)
    z = sigmoid(x, *popt2)
    #print ("These are the values forf the Drug Condition:", x, popt2)
    pylab.plot(xdata, ydata, 'o', color = 'b')
    
    pylab.plot(xdata, ydata2, 'o', color = 'r')
    
    pylab.plot(x,z, color = 'r', label='drug')
    
    pylab.plot(x,y, color = 'b', label='no drug')
    
    pylab.ylim(0, 80)
    
    pylab.rc('font',family = 'Times New Roman')
    
    pylab.legend(loc='upper left')
    
    pylab.xlabel('Hz Frequency', fontname = "Times New Roman",fontsize = 12)
    
    pylab.ylabel('Number of Bar Presses per Minute', fontname = "Times New Roman",fontsize = 12)
    
    pylab.title("Sigmoidal Curves for Drug/No Drug Conditions NSCI 211 ISCC Lab",fontname = "Times New Roman")
    #print(popt, popt2)
    pylab.show()
#=======================================================================================================
def main():
    
    command=[]
    
    loopCommands=True
    
    while loopCommands:
        
        decision = input("\nOPTIONS:\"sterr\",\"sigmoid\":\n")
        
        if decision == "sterr":
            
            standardError()
            
        if decision == "sigmoid":
            
            sigmoidal()
main()

    
    
    
    
    
    
    
