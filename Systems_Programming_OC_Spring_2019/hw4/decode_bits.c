// Author: Trevor Martin
// Date of Completion: 20 March 2019
// Language: C
// Class: CSCI 241 | Systems Programming | Oberlin College
// Homework#: 4, decode_bits.c
//===================================================================================================
// DESCRIPTION
//===================================================================================================
// Not yet written
//===================================================================================================

#include "bits.c"

int main()
{
  char user_specified_input;
  while (EOF != (user_specified_input = getchar()))
  {
    decode_bits(user_specified_input);
  }
}
