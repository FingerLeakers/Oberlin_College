#!/bin/sh                                                                                              

#Author: Trevor Martin                                                                                 
#Date of Completion: ? February 2019                                                                   
#Language: Shell                                                                                       
#Class: CSCI241 | Systems Programming | Oberlin College                                                
#Homework#: 2, gradeit.sh                                                                              
#================================================================                                      
#DESCRIPTION                                                                                           
#================================================================                                      
#Tests for differences between two files; grades diamond.c and                                         
#rot128.c, which are stored ~rhoyle/pub/cs241/hw01                                                     
#================================================================                                      

diamond_testing_value=0

#This first echo with nothing printed prints a new space                                               
echo
echo We will now begin testing your diamond.c program.

#Use seq to go through a sequence (makes sense), with the 0 value for the                              
#lower bounds and the 9 for the upper bounds                                                           

for iterative_test in $(seq 0 9); do

    # ">" redirects command output to a file                                                           
    echo $iteration > program_testing_file

    #Here we access the ideal output for the diamond program                                           
    ~rhoyle/pub/cs241/hw01/diamond < program_testing_file > rhoyle_result

    grep -E "^\s+\*" rhoyle_result > ideal_result

    #Compile diamond.c                                                                                 
    gccx diamond.c -o diamond

 #Use the output from diamond and put it into the testing file as                                   
    ./diamond < program_testing_file > student_result

    grep -E "^\s+\*" student_result > result

    #The difference between these two outputs is found with diff                                       
    deviation=$(diff result ideal_result)

    #In the case that there is deviation, set the value for diamond to 1                               
    if [ -n "$deviation" ]; then

        diamond_testing_value=1

        break

    fi

done

#Show the user if they were successful in their endeavors

if [ $diamond_testing_value = 0 ]; then
    echo
    echo SUCCESS: The output of diamond.c matched the ideal output
else
    echo
    echo ERROR: The output of diamond.c did not match the ideal output
fi


testing_diamond_again=0

echo "trial_file" > input
echo "trial_file_2" > input_2

./diamond < input > student_result

#return value of lasted executed command                                                               
returned=$?

if [ $returned != 0 ]; then

    testing_diamond_again=1
fi

./diamond < input_2 > student_result

#Get the value last executed by the command                                                            
returned_2=$?

if [ $returned_2 != 0 ]; then

    testing_diamond_again=1
fi

if [ $testing_diamond_again = 0 ]; then

    echo
    echo SUCCESS: The input of diamond.c matched the ideal input

else

    echo
    echo ERROR: The input of diamond.c did not match the ideal input
fi

echo
echo We will now begin testing your rot.cprogram.

testing_rot=0

to_encrypt="Encrypt me, I dare you."

echo $to_encrypt > input

gccx rot128.c -o rot128

./rot128 < input > student_result


returned=$?

if [ $returned != 0 ]; then

    testing_rot=1

fi

if [ $testing_rot = 0 ]; then

    echo
    echo SUCCESS: rot128.c ran without issue

else

    echo
    echo ERROR: rot128.c did not run properly
fi

testing_rot_again=0


~rhoyle/pub/cs241/hw01/rot128 < program_testing_file > ideal_result

deviation=$(diff student_result ideal_result)

if [ -n "$deviation" ]; then

    testing_rot_again=1

fi

if [ $testing_rot_again = 0 ]; then

    echo
    echo SUCCESS: The output of rot128.c matched the ideal output

else
    echo
    echo ERROR: The output of rot128.c did not match the ideal output
    echo
fi

#Let's get rid of that crap                                                                            
rm program_testing_file ideal_result diamond rot128 rhoyle_result student_result input input_2 result


