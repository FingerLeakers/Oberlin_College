// Author: Trevor Martin
// Date of Completion: 17 March 2019
// Language: C
// Class: CSCI 241 | Systems Programming | Oberlin College
// Homework#: 4, getnum.h
//===================================================================================================
// DESCRIPTION
//===================================================================================================
// Houses all of the functionality for getnum.c
//===================================================================================================  

#ifndef BITS
#define BITS

void skip_leading_whitespace();
void negative_status();
void skip_to_next_word();
long parse_decimal_number();
long parse_hexidecimal_number();
long parse_octal_number();
long parse_binary_number();
long parse_aggregate();
long getnum();
void convert_to_octal(long number);
void convert_to_binary(long number);
void convert_to_hexidecimal(long number);

#endif
