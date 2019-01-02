#Author: Trevor Martin
#Date of Completion: 8 March 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Easy

import picture2
print("Welcome fellow citizen! You can call me imageEdit.py the image editor, here at your service. \n\n Your day just got a whole lot better, prepare to have some fun!\n")

#1. Prompts user to pick a file to load in. Have exceptions for invlaid items entered.
def main():
    while True:
        
        try:
            
            FileName=input("Please provide a file of your liking comrade:")
            pic=picture2.Picture(FileName)
            
#2.Display the file image.            
            pic.display()
        except FileNotFoundError:
            print("\nIt's okay, do not grow sad, just enter a file today, then you'll be glad! ")
            
        else:
            break
#3.Offer the user a series of commands that they may use to alter their image. Trevor: Make you sure you go back and check the commands + errors and make sure that multiple edits can be made to the pictures.
    commands=[]
    loopcommands=True
    
#4.Use While loop to print a table of possible operations.
    while loopcommands:
        
        print("\nHere is your tool kit my dear friend: Copy, Grayscale, Zoom, Negate, Scroll, Blur, Flip, and Quit")
        
        Acommand=input("\nSo, what command will it be?:")
        if Acommand=="Copy":
            pic2=Copy(pic)
            pic2.display()
            pic = pic2
            commands.append(pic2)
            
            print("\nExcellent choice! Quite pulchritudinous if I do say so myself.")
            
        elif Acommand=="Flip":
            
            pic2=Flip(pic)
            pic2.display()
            pic = pic2
            commands.append(pic2)
            print("\nExcellent choice! Quite pulchritudinous if I do say so myself.")
            
        elif Acommand=="Grayscale":
            pic2=Grayscale(pic)
            pic2.display()
            pic = pic2
            commands.append(pic2)
            
            print("\nExcellent choice! Quite pulchritudinous if I do say so myself.")
            
        elif Acommand=="Zoom":
            pic2=Zoom(pic)
            pic2.display()
            pic = pic2
            commands.append(pic2)
            
            print("\nExcellent choice! Quite pulchritudinous if I do say so myself.")
            
        elif Acommand=="Negate":
            pic2=Negate(pic)
            pic2.display()
            commands.append(pic2)
            
            print("\nExcellent choice! Quite pulchritudinous if I do say so myself.")
            
        elif Acommand=="Scroll":
            pic2=Scroll(pic)
            pic2.display()
            pic = pic2
            commands.append(pic2)
            
            print("\nExcellent choice! Quite pulchritudinous if I do say so myself.")
            
        elif Acommand=="Blur":
            pic2=Blur(pic)
            pic2.display()
            pic = pic2
            commands.append(pic2)
            
            print("\nExcellent choice! Quite pulchritudinous if I do say so myself.")
            
        elif Acommand=="Quit":
            loopcommands=False
            print("\nSorry you had to leave so soon, sad face.")
          
    
#5.Make all the operations. Display image after each operation.
def Copy(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    picAlt=picture2.Picture(w,h)
    
    for x in range(0,w):
        
        for y in range(0,h):
            
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)
            picAlt.setPixelColor(x,y,r,g,b)
            
    picAlt.setTitle("Copy")
    return picAlt

def Grayscale(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    picAlt=picture2.Picture(w,h)
    
    for x in range(0,w):
        
        for y in range(0,h):
            
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)
            GScale=((r+g+b)//3)
            picAlt.setPixelRed(x,y,GScale)
            picAlt.setPixelGreen(x,y,GScale)
            picAlt.setPixelBlue(x,y,GScale)
            
    picAlt.setTitle("Grayscale")
    return picAlt

def Flip(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    picAlt=picture2.Picture(w,h)
    
    for x in range(0,w):
        
        for y in range(0,h):
            
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)
            picAlt.setPixelColor(w-x-1,y,r,g,b)
            
    picAlt.setTitle("Flip")
    return picAlt

def Zoom(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    picAlt=picture2.Picture(w,h)
    Vert=0
    Hor=0
    
    for x in range (w//4, 3*(w//4)):
        
        for y in range(h//4, 3*(h//4)):
            
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)
            for i in range(0,2):
                
                for j in range(0,2):
                    
                    picAlt.setPixelRed(Vert+i,Hor+j,r)
                    picAlt.setPixelGreen(Vert+i,Hor+j,r)
                    picAlt.setPixelBlue(Vert+i,Hor+j,r)
            Hor=Hor+2
        Vert=Vert+2
        Hor=0
    picAlt.setTitle("Zoom")
    return picAlt
        
def Negate(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    picAlt=picture2.Picture(w,h)
    
    for x in range(0,w):
        
        for y in range(0,h):
            
            r=pic.getPixelRed(x,y)
            g=pic.getPixelGreen(x,y)
            b=pic.getPixelBlue(x,y)   
            picAlt.setPixelRed(x,y,255-r)
            picAlt.setPixelGreen(x,y,255-g)
            picAlt.setPixelBlue(x,y,255-b)
            
    picAlt.setTitle("Negate")
    return picAlt

def Scroll(pic):
    
    w=pic.getWidth()
    h=pic.getHeight()
    
    while True:
        pxl=int(input("\nWant to scroll some pixels? Great! So then, how many?:"))
        
        if pxl>w:
            
            print("\nA little too many there friend, please lay off with the pixels.")
            
            print("Here, we'll try again, I'll start over.")
            
        else:
            break
        
    picAlt=picture2.Picture(w,h)
    
    for x in range(0,w):
        
        for y in range(0,h):
            
            try:
                
                r=pic.getPixelRed(x,y)
                g=pic.getPixelGreen(x,y)
                b=pic.getPixelBlue(x,y)
                picAlt.setPixelColor(x+pxl,y,r,g,b)
                
            except IndexError:
                
                r=pic.getPixelRed(x,y)
                g=pic.getPixelGreen(x,y)
                b=pic.getPixelBlue(x,y)
                picAlt.setPixelColor(x-(w-pxl),y,r,g,b)
                
    picAlt.setTitle("Scroll")
    return picAlt

def Blur(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    picAlt=picture2.Picture(w,h)
    
    for x in range(0,w):
        
        for y in range(0,h):
            
            RBlur=0
            GBlur=0
            BBlur=0
            for i in range(-2,3):
                
                for j in range(-2,3):
                    
                    if x+i>=0 and x+i<w and y + j>=0 and y+j<h:
                        
                        r=pic.getPixelRed(x+i,y+j)
                        g=pic.getPixelGreen(x+i,y+j)
                        b=pic.getPixelBlue(x+i,y+j)  
                        RBlur=RBlur+r
                        GBlur=GBlur+g
                        BBlur=BBlur+b
                    else:
                        continue
                red=RBlur//19
                green=GBlur//19
                blue=BBlur//19
                picAlt.setPixelRed(x,y,red)
                picAlt.setPixelGreen(x,y,green)
                picAlt.setPixelBlue(x,y,blue)
                
    picAlt.setTitle("Blur")
    return picAlt

main()





























