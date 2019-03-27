// Author: Trevor Martin
// Date of Completion: 17 March 2019
// Language: C
// Class: CSCI241 | Systems Programming | Oberlin College
// Homework#: 4, getnum.c
//===================================================================================================
// DESCRIPTION
//===================================================================================================
// This single file stores the function that is used by toBinary, toDecimal, toOctal, and toHex. It
// reads in a signed integer and returns the result in a long integer. Generally, this program calls
// functions to read in integers and return them in one of 4 formats {Binary, Octal, Decimal, Hexadecimal}.
//===================================================================================================

// we need stdio.h to read from standard in and print to standard out
// this also allows us to use ungetc which, according to TutorialPoint "int ungetc(int char, FILE *stream)
// pushes the character char (an unsigned char) onto the specified stream so that the this is available for
// the next read operation"
#include <stdio.h>
// we need limits.h to define different limits macroscopically; different variables will use the same values
// so we define that value once here
#include <limits.h>
// here we will want to return errors if there are errors in formatting. In limits.h we can find the value
// LONG_MAX (the maximum value of a long) which we will store in ERR
#define ERR LONG_MAX
// define binary length maximum
#define BINARY_LENGTH 45
// we will define the length of the hexidecimal and octal numbers, the value chosen for this is explained
// in tobinary.c, where I did a similar thing
#define OCTAL_LENGTH 45
#define HEXIDECIMAL_LENGTH 45
// to exit some loop or functions we need the exit() function, which can be found in stdlib.h
#include <stdlib.h>
// we need ctype.h to get the isspace() for when we are skipping leading whitespaces - a more thorough
// description of isspace() is given when it appears
#include <ctype.h>

// we make this header file at the end and call it here, to get the functions we made
// getnum.h is not <getnum.h> but rather is "getnum.h" because getnum.h is the name of our filename in our
// current directory
#include "getnum.h"

// this is a declaration for the user's specified input 
int user_specified_input;
// skip leading whitespace does something but does not return any value, hence the use of "void"
// which signifies no return value 
void skip_leading_whitespace()
{
  // we want to keep reading if the EOF is not reached AND the input is a space
  // there is nothing inside the while loop because the only thing we want to do is continue reading
  // isspace() returns an integer (non-zero value if the input is a whitespace character and zero
  // if the input is a whitespace) 
  while (EOF != (user_specified_input = getchar()) && isspace(user_specified_input))
  {
  }
  // if the EOF (End Of File) is reached then we want to exit. 
  if (user_specified_input == EOF)
  {
    // found in stdlib.h, this function takes a "status value". Oftentimes the value of 0 signifies
    // a correct or successful operation whereas the value of 1 signifies something wrong and acts
    // as a flag
    exit(0);
  }
}

// instantiate minus_sign for when the next character read is a "-"
int negative_sign = 0;
void negative_status()
{
  // if the character input is a minus sign
  if (user_specified_input == '-')
  {
    // set the minus_sign to be a 1. In the other programs, such as tobinary.c, a negative sign will
    // be read and say if negative_sign > 0, then the negative will be printed printf("%c","-")
    negative_sign = 1;
  }
  else
  {
    // if the input is anything other than a negative sign, we want to continue on our way - ungetc
    // does just this. A more detailed description of ungetc was given earlier. Also, remember that
    // "stdin" is not a variable but is the stream that the input is being read from. This stream is
    // actually just called stdin in the C
    ungetc(user_specified_input, stdin);
  }
}

// this function goes the next word in the sequence if there is an error found in the formatting
void skip_to_next_word()
{
  while(EOF != (user_specified_input = getchar()) && !isspace(user_specified_input))
  {
    // this is empty because all we want to do is go to the next value in the formatted input that
    // is not a space
  }
}

// this variable stores the number of returned errors that may occur with reading a formatted value
int number_of_returned_errors = 0;
// this function parses decimal numbers and returns a long, hence the "long" designation
long parse_decimal_number()
{
  long decimal_number = 0;
  // we want to keep reading until EOF reached AND the input is not a space 
  while (EOF != (user_specified_input = getchar()) && !isspace(user_specified_input))
  {
    // if the user_specified_input is noy between 0 and 9, which are the acceptible decimal
    // number inputs, then we want to return an error
    if (!(user_specified_input >= '0' && user_specified_input <= '9'))
    {
      // the number of errors in now greater than 0 and we have returned ERR since the character
      // we just read was not a digit between 0 and 9
      number_of_returned_errors = 1;
      return ERR;
    }
    // if everything worked successfully with the formatting
    else
    {
      // then we want to update the decimal number value 
      decimal_number = decimal_number * 10 + (user_specified_input - '0');
    }
  }
  return decimal_number;
}

long parse_binary_number()  
{
  // get the next character and store it in our trustworthy variable user_specified_input
  // we are just reading the 1st character here so we don't need the while loop, that will come later
  user_specified_input = getchar();
  if (isspace(user_specified_input) || user_specified_input == EOF)
  {
    // we want to check if this character is a space, which is an invalid character to read,
    // or if we have reached the end of the file. For both cases we want to return an error
    // This space " " or EOF will follow the '0b' designation, which is where we begin checking.
    number_of_returned_errors = 1;
    return ERR;
  }
  // our character was on point, so we want to read the rest of the characters now.
  else
  {
    // we store our binary number in a variable called binary number
    int binary_value = 0;
    // we capture the input starting with the first character following '0b' from the rest of our
    // stdin stream using ungetc
    user_specified_input = ungetc(user_specified_input, stdin);
    // now we use our while loop to go through the characters and possibly return errors if there
    // are any
    while ((user_specified_input = getchar()) != EOF && !isspace(user_specified_input))
    {
      // if the character we read is a 1
      if (user_specified_input == '1')
      {
	// update the binary number accordingly. Remember binary is in base 2
	binary_value = binary_value * 2 + 1;
      }
      // we will have three options here, the character is a 0 or 1 (binary number) or is neither,
      // in which case we want to return an error. "else if" allows us to use another option
      else if(user_specified_input == '0')
      {
	// base 2
	binary_value = binary_value * 2;
      }
      else
      {
	// the digits was not a zero or one, so there was an error
	number_of_returned_errors = 1;
	return ERR;
      }
    }
    return binary_value;
  }
}

// I WILL ADD IN MORE COMMENTS IF I HAVE THE TIME AT THE END
long parse_octal_number()
{
  int octal_value = 0;
  while ((user_specified_input = getchar()) != EOF && !isspace(user_specified_input))
  {
    if (user_specified_input >= '0' && user_specified_input <= '7')
    {
      octal_value = octal_value * 8 + (user_specified_input - '0');
    }
    else
    {
      number_of_returned_errors = 1;
      return ERR;
    }
  }
  return octal_value;
}

long parse_hexidecimal_number()
{
  user_specified_input = getchar();
  if (isspace(user_specified_input) || user_specified_input == EOF)
  {
    number_of_returned_errors = 1;
    return ERR;
  }
  else
  {
    user_specified_input = ungetc(user_specified_input, stdin);
    int hexidecimal_value = 0;
    while ((user_specified_input = getchar()) != EOF && !isspace(user_specified_input))
    {
      if (user_specified_input >= '0' && user_specified_input <= '9')
      {
	hexidecimal_value = hexidecimal_value * 16 + (user_specified_input - '0');
      }
      // extra credit
      else if ((user_specified_input >= 'A' && user_specified_input <= 'F') || (user_specified_input >= 'a' && user_specified_input <= 'f')) 
      {
	if (user_specified_input >= 'a' && user_specified_input <= 'f')
	  {
	    
	
	    hexidecimal_value = hexidecimal_value * 16 + (user_specified_input - 87);
	  }
	else
	  {
	    hexidecimal_value = hexidecimal_value * 16 + (user_specified_input - 55);
	  }
      }
      else 
      {
	number_of_returned_errors = 1;
	return ERR;
      }
    }
    return hexidecimal_value;
  }
}

long parse_aggregate()
{
  // get the first character
  user_specified_input = getchar();
  // if that character is not EOF
  if (user_specified_input != EOF)
  {
    // if it is a digit between 0 and 9
    if (user_specified_input >= '0' && user_specified_input <= '9')
    {
      // if it is 0
      if (user_specified_input == '0')
      {
	// get the next character
	user_specified_input = getchar();
	if (user_specified_input != 'b' && !(user_specified_input <= '7' && user_specified_input >= '0') && user_specified_input != 'x')
	{
	  if (isspace(user_specified_input) || user_specified_input == EOF)
	  {
	    if (negative_sign > 0)
	    {
	      number_of_returned_errors = 1;
	      return ERR;
	    }
	    else
	    {
	      return 0;
	    }
	  }
	  else
	  {
	    number_of_returned_errors = 1;
	    return ERR;
	  }
	}
	// if the specified input is not a space or the EOF
	else
	{
	  if (user_specified_input == 'b')
	  {
	    return parse_binary_number();
	  }
	  else if (user_specified_input == 'x')
	  {
	    return parse_hexidecimal_number();
	  }
	  else
	  {
	    ungetc(user_specified_input, stdin);
	    return parse_octal_number();
	  }
        }
      }
      else
      {
	ungetc(user_specified_input, stdin);
	return parse_decimal_number();
      }
    }
    else
    {
      number_of_returned_errors = 1;
      return ERR;
    }
  }
  else
  {
    number_of_returned_errors = 1;
    return ERR;
  }
}

long getnum()
{
  number_of_returned_errors = 0;
  negative_sign = 0;
  skip_leading_whitespace();
  negative_status();
  long number = parse_aggregate();
  if (number_of_returned_errors > 0)
  {
    if (user_specified_input == EOF)
    {
      printf("%s","ERROR");
      exit(0);
    }
    else
    {
      skip_to_next_word();
    }
  }
  return number;
}

// when we get a decimal number, a long integer, we want to convert it to binary here, adding the
// converted numbers into a binary array which we will eventually print. To convert to binary we
// need to break up all of the numbers into powers of two (get it "binary" means 2). For example,
// take 42. The largest power of 2 <= 42 is 2**5, which is 32. 42 - 32 is 10, which is the number
// left. Now what is the greatest power of 2 that is <= 10. Well, that is 3, 2**3 is 8.  10 - 8 is 2
// which can be had by 2**1. So, we have 2**5, 2**3, 2**1. So 42, can be seen as one "32", one "8",
// and one "2". In binary there is the one's place, two's place, four's place, eight's place, etc..
// You can have 0 or 1 of a place. Also, remember that the one's place is all the way on the left
//    1       0       1       0       1       0          Hence, the binary format of 42 is 101010
// _______ _______ _______ _______ _______ _______       To be complete we need the header 0b101010
// 32's p  16's p  8's p   4's p   2's p   1's p
// In this for loop, we decrement from the starting length, checking for remainders and then reducing
// numbers to their binary places, which was the 32, 8, and 2 we got in the example

void convert_to_binary(long number)
{
  // we instantiate a new binary array of BINARY_LENGTH that will hold the signed long value formatted
  // in binary
  char binary_array[BINARY_LENGTH];
  // this will be used to find how many binary numbers have been added to our binary array and will
  // be useful for printing out the binary numbers
  int binary_size = 0;
  int position1;
  for (position1 = BINARY_LENGTH; position1 >= 0; position1--)
  {
    // find the remainder from the input modulus 2
    int modulus_remainder = number % 2;
    // cut the inputted number in half
    number = number/2;
    binary_array[position1] = modulus_remainder + '0';
    if (number != 0)
    {
      binary_size++;
    }
    else
    {
      break;
    }
  }
  printf("0b");
  // this must go at the front of all binary formatted outputs
  int position2;
  for (position2 = BINARY_LENGTH - binary_size; position2 <= BINARY_LENGTH; position2++)
  {
    printf("%c",binary_array[position2]);
  }
  printf("/n");
}

void convert_to_octal(long number)
{
  char octal_array[OCTAL_LENGTH];
  int octal_size = 0;
  int position1;
  for (position1 = OCTAL_LENGTH - 1; position1 >= 0; position1--)
  {
    int modulus_remainder = number % 8;
    number = number / 8;
    octal_array[position1] = modulus_remainder;
    if (number == 0)
    {
      break;
    }
    else
    {
      octal_size++;
    }
  }
  int position2;
  for (position2 = OCTAL_LENGTH - octal_size - 1; position2 < OCTAL_LENGTH; position2++)
  {
    printf("%d", octal_array[position2]);
  }
  printf("\n");
}
// print long
void convert_to_hexidecimal(long number)
{
  char hexidecimal_array[HEXIDECIMAL_LENGTH];
  long hexidecimal_size = 0;
  int position1;
  for (position1 = HEXIDECIMAL_LENGTH - 1; position1 >= 0; position1--)
  {
    int modulus_remainder = number % 16;
    number = number / 16;
    hexidecimal_array[position1] = modulus_remainder;
    if (number != 0)
    {
      hexidecimal_size++;
    }
    else
    {
      break;
    }
  }
  int position2;
  for (position2 = HEXIDECIMAL_LENGTH - hexidecimal_size - 1; position2 < HEXIDECIMAL_LENGTH; position2++)
  {
    printf("%X", hexidecimal_array[position2]);
  }
  printf("\n");
}
