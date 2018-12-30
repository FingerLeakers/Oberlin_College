# secondconverter.py
# Translate seconds into a more readable hours, minutes, and seconds.
#
# Trevor Martin
# 17 February 2018

# Explain on the terminal (via the print function) what this program does.


# Prompt the user to enter a number of seconds, store in a variable.


# Compute hours, mins, and seconds for this input.


# Print the results.

print("I hope you are having a nice day, here I created a program.","\n","\n", "This program converts a number of seconds into hours, minutes under 60, and remaining seconds under 60.","\n",sep="")
sec=int(input("Please enter the number of seconds:"))
s=sec%60
m=sec%3600//60 
h=sec//3600   
print("\n","That ", sec, " seconds is equal to ", h, " hours, ", m, " minutes, and ", s, " seconds.", "\n" ,"That's it, you can continue enjoying your day now.", sep="", end="")




