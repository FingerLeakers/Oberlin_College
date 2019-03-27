// Author: Trevor Martin
// Date of Completion: 20 March 2019
// Language: C
// Class: CSCI 241 | Systems Programming | Oberlin College
// Homework#: 4, tooctal.c
//===================================================================================================
// DESCRIPTION
//===================================================================================================
// Outputs the signed value in base 8 with a single leading 0
//=================================================================================================== 

// get the functions and variables present in getnum.c
#include "getnum.c"

// all comments below this points are the same as tohex.c, which I completed first


int main()
{
  // getnum.c gets us our negative_status, number_of_returned_errors, and user_specified_input
  // it gets us the functions getnum() and convert_to_octal()
  // below here the comments will be nearly identical to todecimal.c's
  while (user_specified_input != EOF)
  {
    // store the value returned by getnum() in a long called number
    long number = getnum();
    // we proceed if there are no errors returned in the formatting of the number
    if (!(number_of_returned_errors > 0))
    {
      // if the number is a negative number (this comes from our negative function in getnum(), where
      // a 1 is returned if a "-" is present.
      if (negative_sign > 0)
      {
	// remember %c is for a character
	printf("%c", '-');
        // have to lead the octal with "0"
	printf("%c",'0');
	convert_to_octal(number);
      }
      else
      {
	// just print the "0" and the octal
	printf("%c",'0');
	convert_to_octal(number);
      }
    }
    else
    {
      // tell the user that they've enter a poorly formatted input value as with tobinary.c
      printf("\n%s\n","ERROR");
    }
  }
  return 0;
}
