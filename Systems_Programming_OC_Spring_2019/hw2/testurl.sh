#!/bin/sh                                                                                             

#Author: Trevor Martin                                                                                
#Date of Completion: 23 February 2019                                                                 
#Language: Shell                                                                                      
#Class: CSCI241 | Systems Programming | Oberlin College                                               
#Homework#: 2, testurl.sh                                                                             
#================================================================                                     
#DESCRIPTION                                                                                          
#================================================================                                     
#Finds out whether each url leads to an active website.                                               
#================================================================                                     

#Here we set the variable "URLS" equal to the concatination of whatever                               
#is inside the first commandline argument ($1), which is a file in this case.                         
#The quotations are entered because the user may input a file that does not                           
#have anything in it, which would throw an error.                                                     
URLS="$(cat $1)"

#Here we want to check if the concatinated contents of the file are equal to                          
#length 0; the -z string test returns true if this is the case. Now view the output,                  
#given back to the user by the echo command.                                                          
if [ -z "$URLS" ]; then
    echo I am sorry user but your file was found to be empty at the hands of my
    echo -z command, please enter a file with urls inside it this time.

#Since a user can either provide a urls list or not, and since we now know they                       
#have, courtesy of the if statement above, we use an else block to begin                              
#testing whether or not these urls work.                                                              
else
    for url in $URLS; do
        #COURTESY OF MAN PAGES...the curl commands is good for transfering a url                      
        #..."a tool to transfer data from or to a server"...Also, using -s or                         
        #--silent suppresses the output, which can be annoying. Using -I or --head                    
        #gets "the headers only!" and when used with a file, "curl displays the                       
        #file size." Bingo!

        #COURTESY OF MAN PAGES...the tail command goes as follows:                                    
        #tail [OPTION] ... [FILE], -n or --lines can get you the last number of                       
        #lines, "-n +NUM to output starting with line NUM"                                            

        #UPDATE: rather than use tail and get a certain number of last lines in use                   
        #for the file I am going to use the head command and --lines to get the first lst             
        #line of the file and then use grep to check if the file gets a server error.                 

        #Silently pipe the header of the url (via curl) into the n=1 (1st) line of head               
        #and then pipe that to grep, which tests if it gets an error with the server.                 

        this_url_doesnt_work=$(curl -s -I $url | head --lines 1 | egrep "HTTP/1.[01] [23]..")

        #Use our -z string test to see if grep return nothing and then output the bad url             
        if [ -z "$this_url_doesnt_work" ]; then
            echo This url leads nowhere: $url
        fi
    done
fi

#UPDATE: wget was mentioned and I want to try to utilize this over grep which seems tedious.          
#$URLS=$(cat $1)                                                                                      
#<Do the same conditional to test if the file is working>                                             

#for url in $URLS; do                                                                                 
 #   if [[ $(wget $url -q -O -) ]]; then                                                              
#       continue                                                                                      
 #   else                                                                                             
#       echo This url is trash: $url                                                                  
 #   fi                                                                                               
#done                                                                                                 



#use "chmod u+x testurl.sh" to make the program executable 
