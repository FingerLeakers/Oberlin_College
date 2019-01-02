# A program for predicting the species of flowers from their measurements.
#
# Note: some of the code for this program is already provided to you.
# Your goal is to fill out several of the functions below to make this program work.
#
#Author: Trevor Martin and Adam Eck (mostly Eck)
#Date of Completion: 15 March 2018
#Data of Edits: 2 January 2019
#Language: Python 3
#Difficulty: Medium 

# many of the functions needed are already provided in the predict_helpers module
import predict_helpers
import math

# A function for calculating the distance between two flowers' measurements
#
# Inputs: flower1   A list of measurements for the first flower
#         flower2   A list of measurements for the second flower
# Output: the Euclidian distance between flower1 and flower2
def calculateDistance(flower1, flower2):
    # calculate the distance between flower1 and flower2

    dist=math.sqrt(((flower1[0]-flower2[0])**2)+((flower1[1]-flower2[1])**2)+((flower1[2]-flower2[2])**2)+((flower1[3]-flower2[3])**2))
    
    # return the distance so we can use it outside this function
    return dist

# A function for predicting the species of a single unknown flower
#
# Inputs: newFlower     A list of measurements for the unknown flower for which we want to predict a species
#         knownFlowers  The measurements of known flowers we will compare newFlower against
#         knownSpecies  The species of the known flowers in knownFlowers 
# Output: the predicted species for newFlower
def predict(newFlower, knownFlowers, knownSpecies):
    # create two variables needed to find the closest flower to newFlower
                 
    # the index of the flower in knownFlowers that is closest to newFlower
    # this should change below if a some other flower than knownFlowers[0] is closer to newFlower 
    closestIndex = 0 
    
    # the distance between newFlower and knownFlowers[closestIndex]
    closestDistance = calculateDistance(newFlower, knownFlowers[0])
    
    # find which flower in knownMeasurements that newFlower is closest to
    # note: closest = smallest distance

    #This looks through all knownFlowers and continually changes closestDistance based on the newFlower 's distance
    for i in range(len(knownFlowers)):          
        if calculateDistance(newFlower, knownFlowers[i]) < closestDistance:
            closestDistance = calculateDistance(newFlower,knownFlowers[i])
            closestIndex=i
            
    # predict the same species as the flower in knownFlowers that newFlower is closest to
    return knownSpecies[closestIndex]

# A function for predicting the species of a list of unknown flowers
#
# Inputs: unknownFlowers   A list of unknown flowers for which we want to make predictions,
#                          where each flower in the list is itself a list of measurements
#         knownFlowers     The measurements of known flowers we will compare unknownFlowers against
#         knownSpecies     The species of the known flowers in knownFlowers
# Outputs: a list of predictions, one species for each flower in unknownFlowers
def makePredictions(unknownFlowers, knownFlowers, knownSpecies):
    # create a list to store the species predictions for each flower in unknownFlowers


    predictions = []
    for i in unknownFlowers:
        predictions.append(predict(i,knownFlowers,knownSpecies))

    # send back the predictions that we made
    return predictions

# The main function runs our program
def main():
    # read in the known flower information from file
    measurements = predict_helpers.readMeasurementsFromFile(predict_helpers.KNOWN_MEASUREMENTS_FILE)
    species = predict_helpers.readSpeciesFromFile(predict_helpers.KNOWN_SPECIES_FILE)
    
    # read in the unknown flower information from file
    unknownFlowers = predict_helpers.readMeasurementsFromFile(predict_helpers.UNKNOWN_MEASUREMENTS_FILE)
    
    # make the predictions for each unknown flower
    predictions = makePredictions(unknownFlowers, measurements, species)
    
    # calculate how many predictions are correct
    predict_helpers.calculateAccuracy(predictions)
    
# call main to start the program
main()
        
        
    
