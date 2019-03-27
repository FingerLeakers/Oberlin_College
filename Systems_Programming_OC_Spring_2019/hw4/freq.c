// Author: Trevor Martin
// Date of Completion: 17 March 2019
// Language: C
// Class: CSCI241 | Systems Programming | Oberlin College
// Homework#: 4, freq.c
//======================================================================
// DESCRIPTION
//======================================================================
// This is a program where an array of all possible lowercase characters
// is created. Then, it reads in a file from standard in and counts the
// frequency of each of the respective lowercase characters. Also, this
// program prints out the most frequent and least frequent letters.
//======================================================================

// we need this to read from standard in and print to standard out
#include <stdio.h>
// we want an array of characters and must specify the length not as a
// variable but as something that is evaluated during compile time. Hence,
// we use "define" "name" "what name is equal to" which is 26 here since
// there are 26 letters in the alphabet
#define ALPHABET 26

int main()
{
  // declare what the user's input will be
  int user_specified_input;
  // initialize one of the arrays, whose notation it is to use "{}" for the contents
  // this array is for the frequency of lowercase letters
  int lowercase_frequency[ALPHABET] = {0};
  // this array is for the frequency of uppercase letters
  int uppercase_frequency[ALPHABET] = {0};
  // to find percentages later, we need to record the total number of letters
  // here we make a variable total_letters to do this
  double total_letters = 0;

  // this line gets each character in the file one character at a time
  // according to TutorialsPoint, getchar() "returns the character read as
  // an unsigned char cast to an int or EOF on end of file or error"
  // getchar(), then must be cast as an int in this case through (int) 
  while (EOF != (user_specified_input = getchar()))
  {
    // why less than/equal to 122 and greater than/equal to 97?
    // this occurs because of the ASCII Codes for the letters, with "a" starting
    // at 097 and "z" ending with 122. We want everything inclusive between
    // 122 and 97. 
    if ((int)user_specified_input <= 122 && (int)user_specified_input >= 97)
    {
      // "a" has position 0 in the array, so its ASCII code - 97 gets 0
      // for the other letter position we just substract 97 to get the position
      // in the array. "++" afterwards returns the old variable before
      // incrementing 
      lowercase_frequency[(int)user_specified_input - 97]++;
      // a letter in the 26 lowercase letters has occured some we increment
      // the total letters by one too
      total_letters++;
    }
    // the ASCII Code for uppercase letters is from 065 to 090, we perform a
    // nearly identical operation
    if ((int)user_specified_input <= 90 && (int)user_specified_input >= 65)
    {
      uppercase_frequency[(int)user_specified_input - 65]++;
      // this is case insensitive, so again we increment total letter
      total_letters++;
    }
  }
  
  // header, format in the way as seen on the assignment webpage
  // \t stands for Tab (Unicode 0x0009) and equals four presses of the spacebar
  // \n (you should really know this) means print a new line
  printf("char\t\tFrequencies\t\tPercentage\n\n");

  // this will come in use for finding the most frequently occuring character
  int most_frequent = 0;
  // this will come in use only if there are multiple letters that occur the most frequently
  // it is an array of size 26 that is instantiated with {" "} that stores the most
  // frequently occuring characters by there ASCII Codes
  char maximum[27] = {" "};
  // this will come in use for finding the least frequently occuring character 
  int least_frequent = 101;
  // this will come in use only if there is are multiple minimally occuring characters
  char minimum[27] = {" "};
  // this will help getting the maximum ascii code stored positions
  int max_position = 0;
  // this will help getting the minimum ascii code stored positions
  int min_position = 0;
  // for minimum position we have to check if the value of occurence for the letter is 0
  int zero = 0; 
   
  // to find how often a letter occurs given the total letters
  float percentage_of_total = 0;
  // instantiate the letter_position variable for use in the for loop
  int letter_position;
  // read as "ascii code for lowercase letters"
  // REALLY IMPORTANT, we do not use the ascii codes for uppercase letters in this code to find the most frequent or least frequent
  // letters because every instance of an uppercase letter will count towards the corresponding lowercase letter. For example,
  // AaAa is 4 of the lowercase letter "a" 
  int low_ascii_code = 0;
  //int upp_ascii_code;
  for (letter_position = 0; letter_position < ALPHABET; letter_position++)
  {
    low_ascii_code = letter_position + 97;
    //upp_ascii_code = letter_position + 65;
    // percentage = occurences of lowercase and uppercase letters / total occurences of letters
    percentage_of_total = ((float)(lowercase_frequency[letter_position]+uppercase_frequency[letter_position])/total_letters)*100;
    // print the occurences, %c means printing for a character
    printf("%c:\t\t%d\t\t\t%f\n",(char)low_ascii_code,lowercase_frequency[letter_position],percentage_of_total);
    // if the given letter occurs more than the most frequently occuring letter
    if ((lowercase_frequency[letter_position]+uppercase_frequency[letter_position]) > most_frequent)
    {
      // set this letter to be the new most frequently occuring letter
      most_frequent = lowercase_frequency[letter_position] + uppercase_frequency[letter_position];
      // get max position 0 
      max_position = 0;
      // and set this new most frequent letter to have its ascii_code at position 0
      maximum[max_position] = low_ascii_code;
    }
    // if the given letter is the most frequent now AND the current ascii_code is not its ascii_code
    if (((lowercase_frequency[letter_position] + uppercase_frequency[letter_position]) == most_frequent) && (maximum[max_position] != low_ascii_code))
    {
      // enter a new position 
      max_position++;
      // and set that position to be its ascii_code
      maximum[max_position] = low_ascii_code;
    }
    

    // if the given letter occurs less than the least frequently occuring letter
    if (((lowercase_frequency[letter_position]+uppercase_frequency[letter_position]) < least_frequent) && ((lowercase_frequency[letter_position] + uppercase_frequency[letter_position]) != zero))
    {
      // set this letter to be the new least frequently occuring letter
      least_frequent = lowercase_frequency[letter_position] + uppercase_frequency[letter_position];
      // and set this new least frequent letter to have its ascii_code at current min position
      minimum[min_position] = low_ascii_code;
    }
    // if the given letter is the most frequent now AND the current ascii_code is not its ascii_code
      if (((lowercase_frequency[letter_position]+uppercase_frequency[letter_position]) == least_frequent) && (minimum[min_position] != low_ascii_code))
    {
     // enter a new minimum position
     min_position++;
     // and set that position to be its ascii_code
     minimum[min_position] = low_ascii_code;
    }
  }
  
  printf("Maximum character(s): ");
  // go through all of the ascii_codes in the maximum list up to the number of maximum letters (max_position)
  int max_character;
  for (max_character = 0; max_character <= max_position; max_character++)
  {
    // if there is a character at a given index, print it out
    if (max_character == max_position)
    {
      // we subtract 32 here since we want to print the capital letter, and for each ascii_code for a
      // lowercase letter, the ascii_code of its corresponding capital letter will be 32 less
      printf("%c ", (int)maximum[max_character]-32);
    }
    else
    {
      // otherwise print the following letters
      printf("%c, ",(int)maximum[max_character]-32);
    }
  }
  // the instructions for printing minimum characters is identical to printing maximum characters save for the fact
  // that it prints the minimum characters
  printf("\nMinimum character(s): ");
  int min_character;
  for (min_character = 0; min_character <= min_position; min_character++)
  {
    if (min_character == min_position)
    {
      printf("%c ", (int)minimum[min_character]-32);
    }
    else
    {
      printf("%c, ", (int)minimum[min_character]-32);
    }
  }
  // just print a new line and give main() a return value
  printf("\n");
  return 0; 
}
