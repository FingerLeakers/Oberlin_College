# Author: Trevor Martin
# Date of Completion: 21 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 4, monte.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# Takes the monte method from Lab 3 and adds try and except blocks to it to better handle
# incorrect user input
#===================================================================================================
# DEPENDENCIES
#===================================================================================================
import random
import picture
import numpy
#===================================================================================================

darts_thrown = eval(input("So, how many darts would you like to throw my friend?: "))

# set canvas width, make a blank canvas, draw an equally sized rectangle over it, and
# then draw the "dart board" which is a circle
width = 400
canvas=picture.Picture(width,width)
canvas.display()
canvas.setFillColor(255,255,200)
canvas.drawRectFill(0,0,width, width)
canvas.setOutlineColor(0,0,0)
canvas.setFillColor(0,0,255)
canvas.drawCircleFill(width//2,width//2,width//2)

# store the number of hits and the value for pi
hits = 0
pi=math.pi

try:
    # throw a dart (circle) at some random place within the radius of the circle
    for dart in range(darts_thrown):
        randX=random.randint(0,399)
        randY=random.randint(0,399)
        canvas.setFillColor(255,0,0)
        canvas.drawCircleFill(randX, randY,2.5)
        distance = math.sqrt((randX-200)**2+(randY-200)**2)
        
        # if the distance is less than the radius
        if distance < 200:
            # the darts hits
            hits = hits + 1
            # get the approximation for pi
            dart_hit_percent = hits / darts_thrown
            pi_approximation = 4 * dart_hit_percent
            pi_off_value = abs(((pi_approximation-pi)/pi)*100)
        
    print("The value of Pi after ",darts_thrown," iterations is ",pi_approximation,
          ", which is off by ",round(pi_off_value,2),"%.",sep = "")
    
    input()

except NameError:
    darts_thrown == 0
    print("Please enter another value my friend, preferably not 0 this time.")
    
except TypeError:
    darts_thrown == float
    print("Please enter another value my friend, preferably not an number with a decimal this time.")



