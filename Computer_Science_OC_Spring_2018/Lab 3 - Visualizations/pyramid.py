# Author: Trevor Martin
# Date of Completion: 21 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 3, pyramid.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program provides an approximation of Pi using the Monte Carlo method; this method takes n darts
# and determines what fraction of them landed within the circle. An approximate Pi value is then outputted.
#===================================================================================================
# DEPENDENCIES
#===================================================================================================
import random
import picture
import numpy
#===================================================================================================

# for random coloration
def Random():
    rand = numpy.random.randint(10,254)
    return rand
    
def main():
    # get the length and width
    user_specified_width = int(input("Please provide a positive width for your pyramid:"))
    user_specified_height = int(input("Please provide a number of bricks for your pyramid's height:"))

    # make a canvas
    canvas = picture.Picture(user_specified_width,user_specified_width)

    # get random color values for the canvas
    randX=random.randint(10,254)
    randY=random.randint(10,254)
    randZ=random.randint(10,254)
     
    # display the canvas    
    canvas.display()
    canvas.setFillColor(randX,randY,randZ)
    canvas.drawRectFill(0,0,user_specified_width, user_specified_width)  
    canvas.setOutlineColor(0,0,0)

    # side length of a single square 
    pyramid_side_length = (user_specified_width//user_specified_height)

    # prints each of the blocks in the pyramid
    for row in range(user_specified_height):
        number_of_bricks = (user_specified_height - row)
        for column in range(number_of_bricks):
            x = ((pyramid_side_length//2) *row) + pyramid_side_length * (column) 
            y = (user_specified_width - (row + 1) * pyramid_side_length)
            canvas.setFillColor(Random(), Random(), Random())
            canvas.drawRectFill(x, y, pyramid_side_length, pyramid_side_length)
    input()
main()



      
      
      

