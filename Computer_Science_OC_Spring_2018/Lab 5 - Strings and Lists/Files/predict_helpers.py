# A small module for evaluating whether a prediction was correct for a given unknown flower
#
# Adam Eck
# 03/06/2018

import sys

# the name of the file containing the measurements of the known flowers
KNOWN_MEASUREMENTS_FILE = "iris_measurements.csv"

# the name of the file containing the species of the known flowers
KNOWN_SPECIES_FILE = "iris_species.csv"

# the name of the file containing the measurements of the unknown flowers whose species we want to guess
UNKNOWN_MEASUREMENTS_FILE = "iris_measurements_unknown.csv"

# the name of the file containing the correct species of the unknown flowers (for calculating accuracy)
UNKNOWN_SPECIES_FILE = "iris_species_unknown.csv"

# A function for reading in the measurements of flowers from a given file
#
# Input: filename   The path to the file from which we will read flower measurements
# Output: a list containing all of the measurements for each flower in filename,
#         where the measurements for each flower is itself a list
def readMeasurementsFromFile(filename):
    # open the measurements file
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(filename, "is missing from your current directory")
        sys.exit(-1) # quits the program
    
    # read in the measurements as a list of lines
    lines = file.readlines()
    
    # close the file
    file.close()
    
    # create the list of measurements
    measurements = []
    
    # ignore the first line since it is only the names of the types of measurements
    for i in range(1, len(lines)):
        # create a list of each mesurement in the line, which are separated by a comma
        flower = lines[i].split(",")
        
        # convert the measurements from strings to floats
        for j in range(len(flower)):
            measure = flower[j]
            flower[j] = float(measure)
        
        # add the flower to the list
        measurements.append(flower)
    
    # return the measurement of each known flower       
    return measurements

# A function for reading in the species of the flowers from file
#
# Input: filename   The path to the file from which we will read flower species
# Output: a list containing the species of each flower in filename
def readSpeciesFromFile(filename):
    # open the known species file
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(filename, "is missing from your current directory")
        sys.exit(-1) # quits the program
    
    # read in the types as a list of lines
    lines = file.readlines()
    
    # close the file
    file.close()
    
    # ignore the first line since it is simply a column header
    species = lines[1:]
    
    # return the species of each known flower
    return species

# A function for checking to see if the prediction for a single flower is correct
#
# Inputs: unknownFlowerNum   The index of the unknown flower in the list of all unknown flowers
#         prediction         The predicted species for the unknown flower
# Output: True if prediction is correct, else False
def checkIfCorrect(unknownFlowerNum, prediction):
    # get the actual species for this particular unknown flower
    actualSpecies = UNKNOWN_SPECIES[unknownFlowerNum]
    
    # was the prediction correct (is it equal to the actual species of the flower)?
    correct = actualSpecies == prediction
    
    # return True if prediction was right, else False
    return correct

# A function for calculating the accuracy of our predictions
#
# Input: prediction     A list of species predictions for each unknown flower
# Output: prints the count and percentage of predictions that were correct
def calculateAccuracy(predictions):
    total = len(predictions)
    correct = 0
    for i in range(total):
        wasCorrect = checkIfCorrect(i, predictions[i])
        
        if wasCorrect:
            correct = correct + 1
            
    print("We were correct on", correct, "out of", total, "predictions")
    print("Our accuracy was ", (100 * correct / total), "%", sep="")

# the correct species for each unknown flower
# Please do *not* use this anywhere except in the checkIfCorrect function
UNKNOWN_SPECIES = readSpeciesFromFile(UNKNOWN_SPECIES_FILE)