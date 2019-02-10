//Author: Trevor Martin
//Date of Completion: ?
//Language: C
//Homework #: 1, hello.c
//Class: CSCI241 | Systems Programming | Oberlin College 
//==========================================================
//DESCRIPTION
//==========================================================
//Prints a formatted amalgam of strings and floating point numbers
//==========================================================

#include <stdio.h>
#include <math.h>

int main()
{
  int this_year = 2013 + 6;
  int amount_of_money_wanted =  2019 + 500000;
  double division = (double) 85 / 95;
  double multiplication = (double) 0.88888888 * 0.999999999;
  float addition = (float) 0.25 + 0.25;
  float subtraction = (float) 0.75 - 0.25;
  float exponential = pow((float) 0.25, 0.10);
  printf("%d\n%-13d\n%13d\n%f\n%2.3f\n%.9f\n",this_year,amount_of_money_wanted,amount_of_money_wanted,addition,subtraction,exponential);
  
}

// %Xd means signed decimal number, which is a 
