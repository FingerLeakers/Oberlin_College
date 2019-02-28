#!/bin/sh                                                                       

#Author: Trevor Martin                                                          
#Date of Completion: ? February 2019                                            
#Language: Shell                                                                
#Class: CSCI241 | Systems Programming | Oberlin College                         
#Homework#: 2, diskhog.sh                                                       
#================================================================               
#DESCRIPTION                                                                    
#================================================================               
#Lists the 5 largest items in the current directory in decreasing               
#magnitude of size.                                                             
#================================================================               

#du will go through the file recursively and -h is to shows us the files        
#in a "human readable" format. The ./* goes through all files in the current    
#directory. We pipe this to sort the files based on -r which stands for reverse
#and -h which stands for human numeric sort. We use head to print the first 10  
#lines of the header and use -n, or --lines to get all but the last n (5) lines
#of the file                                                                    

IFS=":"

for this_file in $(du -h ./* | sort -h -r | head -n 5); do
    #We have got it, now show the file                                          
    echo $this_file
done

