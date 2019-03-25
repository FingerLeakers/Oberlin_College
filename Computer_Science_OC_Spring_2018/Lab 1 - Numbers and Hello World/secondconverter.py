# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 1, secondconverter.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program converts a number of seconds into hours, minutes under 60, and remaining seconds under 60.
#===================================================================================================

seconds = int(input("Please enter the number of seconds:"))
number_of_seconds_left = seconds % 60
number_of_minutes = seconds % 3600 // 60 
number_of_hours = seconds // 3600   

print(seconds, "seconds is equal to ",number_of_hours,"hours, ",number_of_minutes,"minutes, and ",
	 number_of_seconds_left," seconds.",sep = " ", end = " ")



