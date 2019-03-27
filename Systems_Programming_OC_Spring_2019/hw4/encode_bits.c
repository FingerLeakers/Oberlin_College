// Author: Trevor Martin
// Date of Completion: 21 March 2019
// Language: C
// Class: CSCI 241 | Systems Programming | Oberlin College
// Homework#: 4, encode_bits.c
//===================================================================================================
// DESCRIPTION
//===================================================================================================
// Not yet written
//===================================================================================================  

#include "bits.c"
// look our old friend
#include "getnum.c"
#include <string.h>

int main(int argc, char** argv)
{
  char user_specified_input;
  if (argc == 2)
  {
    if (strcmp(argv[1], "-b") == 0)
    {
      while (EOF != (user_specified_input = getchar()))
      {
	display_bits(user_specified_input);
      }
    }
    else if (strcmp(argv[1], "-h") == 0)
    {
      while (EOF != (user_specified_input = getchar()))
      {  
        if (negative_sign > 0)
        {
	  printf("-");
	  convert_to_hexidecimal(user_specified_input);
        }
        else
        {
	  convert_to_hexidecimal(user_specified_input);
        }
      }
    }
    else if (strcmp(argv[1], "-o") == 0)
    {
      while ((user_specified_input = getchar()) != EOF)
      {
        if (negative_sign > 0)
        {
	  printf("-");
	  convert_to_octal(user_specified_input);
        }
        else
        {
	  convert_to_octal(user_specified_input);
        }
      }
    }
    else
    {
      printf("Sorry chief the command line arguments are: -o -b -h");
    }
  }
  else
  {
    printf("Sorry chief the command line arguments are: -o -b -h");
  }
  return 0;
