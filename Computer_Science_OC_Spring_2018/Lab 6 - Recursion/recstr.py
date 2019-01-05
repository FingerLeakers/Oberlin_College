#Author: Trevor Martin
#Date of Completion: 28 March 2018
#Data of Edits: 5 January 2019
#Language: Python 3
#Difficulty: Easy

def main():
    string1=str(input("Please provide a string1:"))
    string2=str(input("Please provide a string2:"))
    print("The string",string1,"backwards is",Backwards(string1),".") 
    if Palindrome(string1) == True:
        print("The string",string1,"is a Palindrome.")
    elif Palindrome(string1) == False:
        print("The string",string1,"is not a Palindrome.")
    if IsSequenceOf(string1, string2) == True:
        print(string2,"is a Sequence of",string1)
    elif IsSequenceOf(string1,string2) == False:
        print(string2,"is not a Sequence of",string1)
   
#This function takes a string and reverses the order of its letters.
def Backwards(string):
    if len(string)==0:
        return ""
    elif len(string)>0:
        LastLetter=string[-1]
        return LastLetter + Backwards(string[:-1])
                     
    #return Backwards(letters[:,-1])
    #return Backwards(len(string)-string[string-1])

#This function finds if a string is read the same fowards as backwards.
def Palindrome(string):
    if len(string)==0 or len(string)==1:
        return True
    elif string[0]==string[-1] and Palindrome(string[1:-1]):
        return True
    else:
        return False

#This finds whether or not string2 is a sequence of string1.
def IsSequenceOf(string1, string2):
    if len(string2)==0:
        return True
    elif len(string2)>len(string1):
        return False
    elif string1[0]==string2[0] and IsSequenceOf(string1[1:], string2[1:]):
        return True
    elif string1[0]!=string2[0] and IsSequenceOf(string1[1:], string2):
        return True
    
main()
