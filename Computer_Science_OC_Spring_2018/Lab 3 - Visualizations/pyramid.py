#Author: Trevor Martin
#Date of Completion: 21 February 2018
#Data of Edits: 30 December 2018
#Language: Python 3
#Difficulty: Easy

import picture
 
user_specified_width = int(input("Please provide a positive width for your pyramid:"))
user_specified_height = int(input("Please provide a number of bricks for your pyramid's height:"))

canvas = picture.Picture(user_specified_width,user_specified_width)

canvas.display()
canvas.setFillColor(0,0,0)
canvas.drawRectFill(0,0,user_specified_width, user_specified_width)  
canvas.setOutlineColor(0,0,0)

pyramid = (user_specified_width//user_specified_height)

for row in range(0, user_specified_height):
    number_of_bricks = (user_specified_height-row)
    for column in range(0, number_of_bricks):
        x=((pyramid//2)*row)+pyramid*(column) 
        y=(user_specified_width-(row+1)*pyramid)
        canvas.setFillColor(255,0,255)
        canvas.drawRectFill(x,y, pyramid, pyramid)
        


      
      
      

