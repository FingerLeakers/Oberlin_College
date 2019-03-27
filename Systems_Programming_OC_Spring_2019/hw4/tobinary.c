// Author: Trevor Martin
// Date of Completion: 18 March 2019
// Language: C
// Class: CSCI241 | Systems Programming | Oberlin College
// Homework#: 4, tobinary.c
//===================================================================================================
// DESCRIPTION
//===================================================================================================
// Outputs a signed integer value in binary format with a leading 0b
//===================================================================================================    

// this is a file in our directory so it gets " " and not < >, getnum.c calls tobinary.c so we must
// include it here to be visible
#include "getnum.c"
  
int main()
{
  // where did we get user_specified_input! I thought that was exclusive to getnum.c! Well no,
  // user_specified_input is visible to tobinary.c because we did #include "getnum.c". Also,
  // we will be able to use our functions in getnum.c such as getnum(), which converts the
  // integer to a long (I have yet to write this) but for now all that you need to know is
  // its functionality. There will be errors in formats inputted, so the variable
  // number_of_returned_errors will hold that in 
  while (user_specified_input != EOF)
  {
    // store the user specified inputted converted to a long in the variable number
    long number = getnum();
    // if there are no errors
    if (!(number_of_returned_errors > 0))
    {
      // we have a variable that determines the negative_status. If there is a negative status,
      // the value of negative will be 1, which is greater than 0 and this beckons us to print
      // a "-" before we print our binary number 
      if (negative_sign > 0)
      {
	// convert the number to binary format preceeded by a negative sign
	printf("%c",'-');
	convert_to_binary(number);
      }
      // if there was no negative flag
      else
      {
	// convert the number to binary format without a negative sign
	convert_to_binary(number);
      }
    }
    else
    {
      // tell the user that they've enter a poorly formatted input value
      printf("\n%s\n","ERROR");
    }
  }
  return 0;
}
