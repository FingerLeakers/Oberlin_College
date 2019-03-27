// Author: Trevor Martin
// Date of Completion: 20 March 2019
// Language: C
// Class: CSCI 241 | Systems Programming | Oberlin College
// Homework#: 4, todecimal.c
//===================================================================================================
// DESCRIPTION
//===================================================================================================
// Outputs the signed value in base 10 with no leading 0 characters.
//===================================================================================================

// to access variables and values in getnum.c that will be used for todecimal we must include "getnum.c"            
#include "getnum.c"

int main()
{
  // user_specified_input, number_of_returned_errors, and negative_status were specified in getnum.c
  // getnum() is a function specified in getnum.c
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
	// remember %c is for a character, and the character we are using is a "-" for minus
	// also, l is (not a one) is for (according to tutorial point) "The argument is interpreted
	// as a long int or unsigned long int for integer specifiers (i, d, o, u, x and X), and as
	// a wide character or wide character string for specifiers c and s" and the u is for
	// (again according to TutorialPoint) an "unsigned decimal integer"
	// So, briefly, the l is for long and the u is for unsigned decimal integer
	printf("%c%lu\n",'-',number);
      }
      else
      {
	// not minus sign so no %c here
	printf("%lu\n",number);
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
