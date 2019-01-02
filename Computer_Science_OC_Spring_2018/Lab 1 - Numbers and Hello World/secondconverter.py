#Author: Trevor Martin
#Date of Completion: 17 February 2018
#Data of Edits: 1 January 2019
#Language: Python 3
#Difficulty: Very Easy

print("I hope you are having a nice day, here I created a program.","\n","\n", "This program converts a number of seconds into hours, minutes under 60, and remaining seconds under 60.","\n",sep="")
sec=int(input("Please enter the number of seconds:"))
s=sec%60
m=sec%3600//60 
h=sec//3600   
print("\n","That ", sec, " seconds is equal to ", h, " hours, ", m, " minutes, and ", s, " seconds.", "\n" ,"That's it, you can continue enjoying your day now.", sep="", end="")




