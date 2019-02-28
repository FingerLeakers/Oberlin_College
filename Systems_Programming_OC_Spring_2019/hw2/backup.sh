#!/bin/sh                                                                                             

#Author: Trevor Martin                                                                                
#Date of Completion: ? February 2019                                                                  
#Language: Shell                                                                                      
#Class: CSCI241 | Systems Programming | Oberlin College                                               
#Homework#: 2, backup.sh                                                                              
#================================================================                                     
#DESCRIPTION                                                                                          
#================================================================                                     
#Takes directory as argument and copies files, inputting them to                                      
#the directory.                                                                                       
#================================================================                                     

#We want to read files and a directory from the command line.                                         
#So, really, there are multiple lines to read. We read these using                                    
#a for loop and $@, the latter of which takes in $1, $2, etc..                                        

for command in $@; do

    #Next we want to see whether command is a file or a directory.                                    

    #For a directory, -d returns true if the command is a file and a                                  
    #directory. If we get true then we want to store our directory                                    
    #command in a variable, here backup_directory. We use a break to                                  
    #exist the conditional and cease looping; we are only looking for                                 
    #one directory and once we've found it we can stop.                                               

    if [ -d $command ]; then

        backup_directory=$command

        break

    fi

done

#We now want to test if our directory is empty. -z is true if the length                              
#of a string is equal to 0                                                                            

#if [ -z $our_directory ]; then                                                                       
#if [ "$(ls -A $backup_directory)" ]; then                                                            
   # echo This directory is empty.                                                                    

    #If the directory is not empty, we want to check (1) whether or not the                           
    #files we are backing up are already exist in the backup and (2) the                              
    #timestamp of the file to see whether or not it should be copied, if the                          
    #timestamp of the file we are copying is earlier than the file inside, we                         
    #should not copy it in.                                                                           

#else                                                                                                 
    #From Wikipedia: "In Unix-like and some other operating systems, the pwd                          
    #command (print working directory) writes the full pathname of the current                        
#working directory to the standard output."

existing_directory=$(pwd)

#We want to go through the rest of our commands, which we know are files,                             
#and begin the process of backing them up                                                             
for this_file in $@; do

    #Just to be safe, we don't actually know these are files, so the -f                               
    #tests whether or not the commands is actually a file.                                            
    if [ -f $this_file ]; then

        #From Wikipedia: "cd by itself or cd ~ will always put                                        
        #you in your home directory."                                                                 

        cd ~

        #We want to check if the file is in our backup_directory so we first                          
        #use -e to see if the file is the directory.                                                  

        if [ -e $backup_directory/$this_file ]; then

#After reading the test man pages we can see that -nt or -ot goes returns                 
            #true respectively for FILE1 -(older than) FILE2 and FILE1 -(newer than)                  
            #FILE2.                                                                                   

            if [ $existing_directory/$this_file -nt $backup_directory/$this_file ]; then

                #cp stands for copy, and will copy the first input into the second input.             
                #The -f overwrites the file (since the one in the current directory is                
                #newer (from the preceding if statement).                                             
                cp -f "$existing_directory"/"$this_file" "$backup_directory"/"$this_file"

            fi

        #From the if statement with the -e we now know that the file does not already exist           
        # in the backup and we can simply copy it over from the current directory to the              
        #backup                                                                                       

        else
            cp -f "$existing_directory"/"$this_file" "$backup_directory"/"$this_file"

        fi
    fi
done

