# Author: Trevor Martin
# Date of Completion: 17 February 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 1, fancy.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program greets someone with their last name, middle name, and first name.
#===================================================================================================

name = str(input("Enter your name: "))

nickname = str(input("Enter your nickname: "))

lastname = str(input("Enter your lastname: "))

print("Welcome back, ",name,' "{}" '.format(nickname),lastname,"!",sep="")
