// Author: Trevor Martin
// Date of Completion: 20 March 2019
// Language: C
// Class: CSCI 241 | Systems Programming | Oberlin College
// Homework#: 4, bits.c
//===================================================================================================
// DESCRIPTION
//===================================================================================================
// 
//===================================================================================================

// this is crunch time, comments will be added in later
#include <stdio.h>
#include <limits.h>
#include <ctype.h>
#include <stdlib.h>
#include "bits.h"

void display_bits(int character)
{
  // from limits.h
  char binary_array[CHAR_BIT + 1];
  int position;
  for (position = CHAR_BIT; position >= 0; position--)
  {
    int modulus_remainder = character % 2;
    character = character / 2;
    // ha I learned my lesson with the "0" vs '0'
    binary_array[position] = modulus_remainder + '0';
  }
  printf("%s\n",binary_array);
}

void decode_bits(int character)
{
  static char display[CHAR_BIT];
  static char* output = display;
  static int output_size = 0;
  if (!isspace(character) && !(character == '0' || character == '1'))
  {
    printf("%s\n","There was a formatting error; the digit was non-binary.");
    exit(1);
  }
  else if (!isspace(character))
  {
    *output = character;
    output++;
    output_size++;
  }
  if (output_size == CHAR_BIT)
  {
    int total_digits = 0;
    int digit_value = 1;
    int position2;
    for (position2 = CHAR_BIT - 1; position2 >= 0; position2--)
    {
      if (display[position2] == '1')
      {
	total_digits += digit_value;
      }
      digit_value = digit_value * 2;
    }
    printf("%c\n",total_digits);
    output = display;
    output_size = 0;
  }
}
