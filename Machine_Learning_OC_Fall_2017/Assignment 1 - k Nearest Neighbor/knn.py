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

#=======================================================================================================
#DEPENDENCIES
#=======================================================================================================
import numpy
import random
from sys import argv 
from pandas import read_csv, DataFrame
from matplotlib import pyplot 
from sklearn.neighbors import KNeighborsClassifier
#=======================================================================================================
#Reads file, distance function, value of k, percentages of instance of training set, and the random seed
#=======================================================================================================
#at index 1 will be the dataset, at 2 the activation function, at 3 the value of k
command_line_arguments = argv
#activation_function = argv[2]
#value_of_k = argv[3]
#activation_function = argv[2]
#training_percentage = argv[3]
#random_integer_seed = argv[4]

# import random
# random.seed(random_integer_seed)
# shuffled = list(yourInstances)
# random.shuffle(shuffled)

file = read_csv(argv[1])
data = DataFrame(file)

print("Here we see the first ten row of our new dataframe")
print(data.head(10))

labels = data.iloc[0]

print("Here are the labels")
print(labels)

rows_of_data = []
for data_row in range(data.shape[0]):
    rows_of_data.append(data.iloc[data_row])
       
random_seed = random.seed(argv[3])
shuffled_data = list(rows_of_data)
random.shuffle(shuffled_data)

cut_off_index = round(len(shuffled_data)*argv[2])
training_set = shuffled_data[:(cut_off_index+1)]
testing_set = shuffled_data[cut_off_index+1:]

#one data point is a row,I need to randomly select a percentage of rows for i in range:
print(cut_off_index)
print("\n",training_set)
print("\n",testing_set)


#data = [random.randint(0,30) for x in range(data.shape[0])]











