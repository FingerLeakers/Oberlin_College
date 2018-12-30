#Author: Trevor Martin
#Date of Completion: 21 February 2018
#Data of Edits: 30 December 2018
#Language: Python 3
#Difficulty: Easy

#ALL COMMENTS BELOW THIS POINT ARE NOTES

import random
import picture
import math

#width=int(input("Please provide a positive width for your canvas:"))

print("This program provides an approximation of Pi using the Monte Carlo method; this method takes n darts and determines what fraction of them landed within the circle. An approximate Pi value is then given.")
n=eval(input("So, how many darts would you like to throw my friend?:"))

width=400
canvas=picture.Picture(width,width)
canvas.display()
canvas.setFillColor(255,255,200)
canvas.drawRectFill(0,0,width, width)
canvas.setOutlineColor(0,0,0)
canvas.setFillColor(0,0,255)
canvas.drawCircleFill(width//2,width//2,width//2)

hits=0

Pi=math.pi

for i in range(0,n):
    randX=random.randint(0,399)
    randY=random.randint(0,399)
    canvas.setFillColor(255,0,0)
    canvas.drawCircleFill(randX, randY,2.5)
    dist=math.sqrt((randX-200)**2+(randY-200)**2)
    
    if dist<200:
        hits=hits+1
        FHit=hits/n
        AppPi=4*FHit
        OffBy=abs(((AppPi-Pi)/Pi)*100)
        
        
print("The value of Pi after",n,"iterations is",AppPi,",which is off by",round(OffBy,2),"%.", sep=" ")
    
input()