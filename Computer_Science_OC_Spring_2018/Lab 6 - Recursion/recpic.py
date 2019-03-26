# Author: Trevor Martin
# Date of Completion: 1 April 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 6, recpic.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program recursively creates a series of image that the user may choose to display.
#===================================================================================================
# DEPENDENCIES
#===================================================================================================
import picture
import math
import random
#===================================================================================================
print("\nWelcome fellow citizen! I am your fractal friend - here, at your service.")
print("Today you will be drawing some awesome art. Prepare to have some fun!!!\n")

def main():
    width = int(input("Please provide a positive size for your canvas: "))
    depth = int(input("Please provide a positive depth for your canvas (preferably <= 5 or 6): "))
    prompts = []
    finished = False
    while not finished:
        #print("\nHere are your options amigo (use these to fill your canvas): Beautiful Bubbles(type B), Scintillating Squares(type S),
        #Triumphant Triangles(type T), Stellar Snowflakes(type Sn), or Quit(type Quit)")
        print('\n{}\n{}\n{}\n{}\n{}'.format("1. Bubbles","2. Squares","3. Triangles","4. Snowflakes","5. Quit"))
        user_command=str(input("So, what user_command will it be?: "))
        if user_command == "Bubbles" or user_command == "1":
            base_picture=picture.Picture(width,width)
            base_picture.setFillColor(0,0,0)
            base_picture.drawRectFill(0,0,width,width)
            edited_picture = Bubbles(width//2,width//2,width//4,depth,base_picture)
            edited_picture.display()
            print("\nO.o *_* Mighty trippy! How pulchritudinous!\n")
        elif user_command == "Squares"or user_command=="2":
            base_picture=picture.Picture(width,width)
            base_picture.setFillColor(0,0,0)
            base_picture.drawRectFill(0,0,width,width)
            edited_picture=Squares(0,0,width//3,depth,base_picture)
            edited_picture.display()
            print("\no.O *.* Mighty trippy! How pulchritudinous!\n")
        elif user_command=="Triangles"or user_command=="3":
            base_picture=picture.Picture(width,width)
            base_picture.setFillColor(0,0,0)
            base_picture.drawRectFill(0,0,width,width)
            base_picture.setFillColor(0,0,0)
            base_picture.setOutlineColor(255,255,255)
            base_picture.drawPolygonFill([(width//2,0),(0,2*width//2),(2*width//2,2*width//2)])                                                             
            edited_picture=Triangles(0,0,width//2,depth,base_picture)
            edited_picture.display()
            print("\nO.o *_* Mighty trippy! How pulchritudinous!\n")
        elif user_command=="Snowflakes" or user_command=="4":
            base_picture=picture.Picture(width,width)
            base_picture.setFillColor(0,0,0)
            base_picture.drawRectFill(0,0,width,width)
            base_picture.setPosition(width//4,3*width//4)
            Snowflakes(width//2,depth,base_picture)
            base_picture.rotate(240)
            Snowflakes(width//2,depth,base_picture)
            base_picture.rotate(240)
            Snowflakes(width//2,depth,base_picture)
            base_picture.rotate(240)
            base_picture.display()
            print("\no.O *.* Mighty trippy! How pulchritudinous!\n")
        elif user_command=="Quit" or user_command == "5":
            finished = True
            print("\nSorry you had to go so soon, sad face.")
            
def Bubbles(x,y,radius,depth,base_picture):
    if depth == 0:
        return ""
    elif depth>0:
        base_picture.setFillColor(255,0,230)
        base_picture.setOutlineColor(255,0,230)
        base_picture.drawCircleFill(x,y,radius)
        Bubbles(x-radius,y-radius,radius//2,depth-1,base_picture)
        Bubbles(x+radius,y-radius,radius//2,depth-1,base_picture)
        Bubbles(x-radius,y+radius,radius//2,depth-1,base_picture)
        Bubbles(x+radius,y+radius,radius//2,depth-1,base_picture)
    return base_picture

def Squares(x,y,width,depth,base_picture):
    if depth == 0:
        return ""
    elif depth>0:
        randX=random.randint(10,254)
        randY=random.randint(10,254)
        randZ=random.randint(10,254)
        base_picture.setFillColor(randX,randY,randZ)
        base_picture.setOutlineColor(255,255,255)
        base_picture.drawRectFill(x+width,y+width,width,width)
        Squares(x,y,width//3,depth-1,base_picture)
        Squares(x,width+y,width//3,depth-1,base_picture)
        Squares(x,y+2*width,width//3,depth-1,base_picture)
        Squares(x+width,y,width//3,depth-1,base_picture)
        Squares(x+2*width,y,width//3,depth-1,base_picture)
        Squares(x+width,y+2*width,width//3,depth-1,base_picture)
        Squares(x+2*width,y+2*width,width//3,depth-1,base_picture)
        Squares(x+2*width,y+width,width//3,depth-1,base_picture)
    return base_picture

def Triangles(x,y,width,depth,base_picture):
    if depth == 0:
       return ""
    elif depth>0:
        randX=random.randint(10,254)
        randY=random.randint(10,254)
        randZ=random.randint(10,254)
        base_picture.setFillColor(randX,randY,randZ)
        base_picture.setOutlineColor(255,255,255)
        base_picture.drawPolygonFill([(x+3*width//2,y+width),(x+width,y+2*width),(x+width//2,y+width)])
        Triangles(x+width//2,y,width//2,depth-1,base_picture)
        Triangles(x,y+ width,width//2,depth-1,base_picture)
        Triangles(x+width,y+width,width//2,depth-1,base_picture)
    return base_picture

def Snowflakes(d,depth,base_picture):
    if depth == 0:
        return ""
    elif depth == 1:
        base_picture.drawForward(d)
    elif depth>0:
        randX=random.randint(10,254)
        randY=random.randint(10,254)
        randZ=random.randint(10,254)
        base_picture.setOutlineColor(randX,randY,randZ)
        Snowflakes(d//3,depth-1,base_picture)
        base_picture.rotate(60)
        randX1=random.randint(10,254)
        randY1=random.randint(10,254)
        randZ1=random.randint(10,254)
        base_picture.setOutlineColor(randX1,randY1,randZ1)
        Snowflakes(d//3,depth-1,base_picture)
        base_picture.rotate(240)
        randX2=random.randint(10,254)
        randY2=random.randint(10,254)
        randZ2=random.randint(10,254)
        base_picture.setOutlineColor(randX2,randY2,randZ2)
        Snowflakes(d//3,depth-1,base_picture)
        base_picture.rotate(60)
        randX3=random.randint(10,254)
        randY3=random.randint(10,254)
        randZ3=random.randint(10,254)
        base_picture.setOutlineColor(randX3,randY3,randZ3)
        Snowflakes(d//3,depth-1,base_picture)
    return base_picture


main()
















