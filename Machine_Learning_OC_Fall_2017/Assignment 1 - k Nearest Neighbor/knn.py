#Author: Trevor Martin
#Date of Completion: 29 December 2018
#Language: Python 3
#Difficulty: ?

#Program takes in five parameters
#1.The path to a file containing the dataset
#2.The name of the distance function to use, from the set {H,E} (H is Hamming function and E is Euclidian)
#3.The value of k to use in k-Nearest Neighbor
#4.The percentage of instances to use for training set
#e.A random seed as an integer
    

#I have to learn how to deal with command line input in python
#I have to learn more about Pandas and dataframe.loc
#I have to touch on generating csv files

#I also must learn what a k-Nearest neighbor is
#Additionally using number for confidence intervals


import numpy
from sys import argv
from pandas import read_csv, DataFrame
from matplotlib import pyplot 
from sklearn.neighbors import KNeighborsClassifier


command_line_arguments = sys.argv
#at index 1 will be the dataset, at 2 the activation function, at 3 the value of k

read_in_file = pandas.read_csv(sys.argv[1])

dataframe = pandas.DataFrame(read_in_file)

features = dataframe.iloc[0]







