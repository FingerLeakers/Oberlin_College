# Author: Trevor Martin
# Date of Completion: 
# Language: Python3
# Class: CSCI374 | Machine Learning | Oberlin College
# Homework#: 1,knn.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# Program takes in five parameters
# 1. The path to a file containing the dataset
# 2. The name of the distance function to use, from the set {H,E} (H is Hamming function and E is Euclidian)
# 3. The value of k to use in k-Nearest Neighbor
# 4. The percentage of instances to use for training set
# 5. A random seed as an integer

# Example: python3 knn.py mnist_100.csv E 1 0.75 12345

# The program outputs a confusion matrix
    
#===================================================================================================
#DEPENDENCIES
#===================================================================================================
import sys
import math
import unittest
#=======================================================================================================

def euclidian_distance(measurementX, measurementY):
    unittest.assertEqual(len(measurementX),len(measurementY))
    distance = math.sqrt(((measurementX[0]-measurementY[0])**2))
    return distance

#def hamming_distance(measurementX, measurementY):
    #unittest.assertEqual(len(measurementX),len(measurementY))
    #distance =
    
def read_file_contents(file):
    try:
        file_contents = open(file, "r")
    except FileNotFoundError:
        print("The file you've entered does not seem to exist in the current directory")
        print("If the does exist, please check if there are errors in the file name")
        sys.exit(-1)
    file_lines = file_contents.readlines()
    
    
    
    labels = labels.split(",")
    #for line in 
    
        
    
    
def main():
    command_line_arguments = sys.argv
    #program_name = command_line_arguments[0]
    file_name = command_line_arguments[1]
    distance_function = command_line_arguments[2]
    k_nearest_neighbor = command_line_arguments[3]
    percentage_of_allocated_training_data = command_line_arguments[4]
    random_seed_for_replication = command_line_arguments[5]
    
    read_file_contents(file_name)
    
    
main()
















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











