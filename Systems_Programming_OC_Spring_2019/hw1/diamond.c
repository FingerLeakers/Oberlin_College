//Author: Trevor Martin                                                      
//Date of Completion: 16 February 2019                                       
//Language: C                                                                  
//Class: CSCI241 | Systems Programming | Oberlin College                   
//Homework#: 1, diamond.c                                                     
//================================================================             
//DESCRIPTION                                                                 
//================================================================            
//The user enters a size for a "diamond" and such a diamond is printed.       
//For example, ./diamond with a size of 2 will return                        
// *                                                                     
//***                                                                           
// *                                                              
//================================================================             
#include <stdio.h>
#include <ctype.h> //from man pages, gets you isdigit()                         
//declare getdigit() function                                                   
int getdigit()
int getdigit()
{
  //while the end of the file is not reached and while the                      
  //character is not a digit                                                         
  int character = -1;

  while (EOF != (character = getchar()) && !isdigit((char) character))
  {
    //empty, this is just conditions for running getdigit()                     
  }

  if (character == EOF)
  {
    return -1;
  }
  //checks for digit between 0 and 9 inclusive                                       
  else //this has to be else and not if(isdigit(character)) because             
       //the function needs a return value                                      
  {
    //not sure yet if this works                                                
    //-----> return character;                                                  
    //okay, so the internet says to use " - '0' " to convert a char to int      
    //this (below) works, so I am going to use it                             
    //just returns one character as int because you only want the first number  
    return character - '0';
  }
}

int main()
{
  //ask user for specifications                                                
  printf("\n%s\n","The size of the diamond is the distance from the first or last point to the center.");

  printf("\n%s","Please specify a size (1-9) for your diamond:");

  //gets the first digit input                                     
  int user_size = getdigit();
  //FIRST HALF OF DIAMOND                                            
  for (int iteration = 1; iteration <= user_size; iteration++)
  {
    for (int space = 1; space <= (user_size - iteration); space++)
    {
      printf("%s"," ");
    }

    for (int asterick = 1; asterick <= ((iteration*2)-1); asterick++)
    {
      printf("%s","*");
    }
  }
  //SECOND HALF OF DIAMOND                                          
  for(int iteration = (user_size - 1); iteration >= 1; iteration--)
  {
    for(int space = 1; space <= (user_size - iteration); space++)
    {
      printf("%s"," ");
    }

    for(int asterick = 1; asterick <= ((iteration*2)-1); asterick++)
    {
      printf("%s","*");
    }

    printf("%s","\n");
  }
}

  

