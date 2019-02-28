//Author: Trevor Martin                                                 
//Date of Completion: 16 February 2019                                  
//Language: C                                                           
//Class: CSCI241 | Systems Programming | Oberlin College                
//Homework#: 1, rot128.c                                                
//================================================================      
//DESCRIPTION                                                           
//================================================================      
//Encrypts text by rotating it n times, as specified by the user.       
//================================================================      

#include <stdio.h>
#include <limits.h>

//HALF_ALLOWED_CHARACTER_RANGE                                          
#define HACR ((UCHAR_MAX + 1)/2)

//EXTRA CREDIT DESCRIPTION                                              
//use arg                                                               

int main()
{
  //input from a file                                                   
  int input_from_file;

  //EOF = "End of File", we are also reading in # btwn 0-255            

  //getchar() returns next inputted character as int.                   

  //We need while loop because each iteration of getchar() only         
  //reads in one character at a time                                    

  //putchar() displays the character inputted with its transformation,  
  //(UCHAR_MAX+1)/2                                                     

  while(EOF != (input_from_file = getchar()))
  {
    putchar(((char) input_from_file) + HACR);
  }

}

