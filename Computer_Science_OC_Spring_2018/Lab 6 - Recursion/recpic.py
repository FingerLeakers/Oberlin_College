#Author: Trevor Martin
#Date of Completion: 1 April 2018
#Data of Edits: 5 January 2019
#Language: Python 3
#Difficulty: Easy

import picture
import math
import random
print("Welcome fellow citizen! I am your fractal friend - here, at your service. Today you will be drawing some awesome art. Prepare to have some fun!!!\n")

def main():
    width=int(input("Please provide a postitive size for your canvas:"))
    depth=int(input("Please provide a postitive depth for your canvas (preferably <= 5 or 6):"))
##    pic=picture.Picture(width,width)
##    pic.setFillColor(0,0,0)
##    pic.drawRectFill(0,0,width,width)
    
    prompts=[]
    Commanding=True
    while Commanding:
        print("\nHere are your options amigo (use these to fill your canvas): Beautiful Bubbles(type B), Scintillating Squares(type S), Triumphant Triangles(type T), Stellar Snowflakes(type Sn), or Quit(type Quit)")
        Command=input("\nSo, what command will it be?:")
        if Command=="B":
            pic=picture.Picture(width,width)
            pic.setFillColor(0,0,0)
            pic.drawRectFill(0,0,width,width)
            pic2=Bubbles(width//2,width//2,width//4,depth,pic)
            pic2.display()
            prompts.append(pic2)
            print("\nO.o *_* Mighty trippy! How pulchritudinous!")
        elif Command=="S":
            pic=picture.Picture(width,width)
            pic.setFillColor(0,0,0)
            pic.drawRectFill(0,0,width,width)
            pic2=Squares(0,0,width//3,depth,pic)
            pic2.display()
            prompts.append(pic2)
            print("\no.O *.* Mighty trippy! How pulchritudinous!")
        elif Command=="T":
            pic=picture.Picture(width,width)
            pic.setFillColor(0,0,0)
            pic.drawRectFill(0,0,width,width)
            pic.setFillColor(0,0,0)
            pic.setOutlineColor(255,255,255)
            pic.drawPolygonFill([(width//2,0),(0,2*width//2),(2*width//2,2*width//2)])                                                             
            pic2=Triangles(0,0,width//2,depth,pic)
            pic2.display()
            prompts.append(pic2)
            print("\nO.o *_* Mighty trippy! How pulchritudinous!")
        elif Command=="Sn":
            pic=picture.Picture(width,width)
            pic.setFillColor(0,0,0)
            pic.drawRectFill(0,0,width,width)
            pic.setPosition(width//4,3*width//4)
            Snowflakes(width//2,depth,pic)
            pic.rotate(240)
            Snowflakes(width//2,depth,pic)
            pic.rotate(240)
            Snowflakes(width//2,depth,pic)
            pic.rotate(240)
            pic.display()
            prompts.append(pic)
            print("\no.O *.* Mighty trippy! How pulchritudinous!")
        elif Command=="Quit":
            Commanding=False
            print("\nSorry you had to go so soon, sad face.")
            
def Bubbles(x,y,r,depth,pic):
    if depth == 0:
        return ""
    elif depth>0:
        pic.setFillColor(255,0,230)
        pic.setOutlineColor(255,0,230)
        pic.drawCircleFill(x,y,r)
        Bubbles(x-r,y-r,r//2,depth-1,pic)
        Bubbles(x+r,y-r,r//2,depth-1,pic)
        Bubbles(x-r,y+r,r//2,depth-1,pic)
        Bubbles(x+r,y+r,r//2,depth-1,pic)
    return pic

def Squares(x,y,width,depth,pic):
    if depth == 0:
        return ""
    elif depth>0:
        randX=random.randint(10,254)
        randY=random.randint(10,254)
        randZ=random.randint(10,254)
        pic.setFillColor(randX,randY,randZ)
        pic.setOutlineColor(255,255,255)
        pic.drawRectFill(x+width,y+width,width,width)
        Squares(x,y,width//3,depth-1,pic)
        Squares(x,width+y,width//3,depth-1,pic)
        Squares(x,y+2*width,width//3,depth-1,pic)
        Squares(x+width,y,width//3,depth-1,pic)
        Squares(x+2*width,y,width//3,depth-1,pic)
        Squares(x+width,y+2*width,width//3,depth-1,pic)
        Squares(x+2*width,y+2*width,width//3,depth-1,pic)
        Squares(x+2*width,y+width,width//3,depth-1,pic)
    return pic

def Triangles(x,y,width,depth,pic):
    if depth == 0:
       return ""
    elif depth>0:
        randX=random.randint(10,254)
        randY=random.randint(10,254)
        randZ=random.randint(10,254)
        pic.setFillColor(randX,randY,randZ)
        pic.setOutlineColor(255,255,255)
        pic.drawPolygonFill([(x+3*width//2,y+width),(x+width,y+2*width),(x+width//2,y+width)])
        Triangles(x+width//2,y,width//2,depth-1,pic)
        Triangles(x,y+ width,width//2,depth-1,pic)
        Triangles(x+width,y+width,width//2,depth-1,pic)
    return pic

def Snowflakes(d,depth,pic):
    if depth ==0:
        return ""
    elif depth==1:
        pic.drawForward(d)
    elif depth>0:
        randX=random.randint(10,254)
        randY=random.randint(10,254)
        randZ=random.randint(10,254)
        pic.setOutlineColor(randX,randY,randZ)
        Snowflakes(d//3,depth-1,pic)
        pic.rotate(60)
        randX1=random.randint(10,254)
        randY1=random.randint(10,254)
        randZ1=random.randint(10,254)
        pic.setOutlineColor(randX1,randY1,randZ1)
        Snowflakes(d//3,depth-1,pic)
        pic.rotate(240)
        randX2=random.randint(10,254)
        randY2=random.randint(10,254)
        randZ2=random.randint(10,254)
        pic.setOutlineColor(randX2,randY2,randZ2)
        Snowflakes(d//3,depth-1,pic)
        pic.rotate(60)
        randX3=random.randint(10,254)
        randY3=random.randint(10,254)
        randZ3=random.randint(10,254)
        pic.setOutlineColor(randX3,randY3,randZ3)
        Snowflakes(d//3,depth-1,pic)
    return pic

main()
















