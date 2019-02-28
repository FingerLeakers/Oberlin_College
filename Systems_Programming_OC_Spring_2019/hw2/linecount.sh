#!/bin/sh                                                                                              

#Author: Trevor Martin                                                                                 
#Date of Completion: ? February 2019                                                                   
#Language: Shell                                                                                       
#Class: CSCI241 | Systems Programming | Oberlin College                                                
#Homework#: 2, linecount.sh                                                                            
#================================================================                                      
#DESCRIPTION                                                                                           
#================================================================                                      
#Recursively counts all the lines in all the file of a current                                         
#directory.                                                                                            
#================================================================                                      

#We use the same approach from backup.sh to get our current directory.                                 

existing_directory="$(pwd)"

#In the existing_directory, find a file of type (-type) file (f) and                                   
#execute finding the newline count (wc -l) (that is a lowcase L not a 1)                               
#{} "runs the specified command on the selected files" - find manpages,                                
#and the "\;" escapes the execution of the commands. These newlines                                    
#counted words are then piped into awk, which allows for straighforward                                
#printing behaviours.                                                                                  

echo Total number of lines are:

find $existing_directory -type f -exec wc -l {} \; | awk '{total_lines += $1} END{print total_lines}'

