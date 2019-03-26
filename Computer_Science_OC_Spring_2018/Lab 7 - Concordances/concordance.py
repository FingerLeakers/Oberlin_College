# Author: Trevor Martin
# Date of Completion: 10 April 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 7, concordance.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# Creates a concordance (sorted alphabetically) of a given text.
#===================================================================================================

def main():
    while True:
        try:
            concordance={}
            number_of_lines = 0
            file_name =input("Please provide a file of your liking comrade: ")
            file_contents=open(file_name,"r")
            lines=file_contents.readlines()
            user_command =input("Would you like the text you are going to have concorded by displayed? Enter YES or NO: ")
            if user_command == "YES":
                display_file_contents(file_name,lines)
            for line in lines:
                split_lines=line.split()
                if len(split_lines) > 0:
                    number_of_lines+=1
                split_lines = remove_punctuation(split_lines)
                for word in split_lines:
                    add_word_to_concordance(word, number_of_lines, concordance)
            print_concordance(concordance)
            print("I have found",number_of_lines,"lines containing",len(concordance),"unique words.")
            file_contents.close()
        except FileNotFoundError:
            print("\nIt's okay, do not worry, please enter a valid file today, and you won't be sorry! ")
        
def display_file_contents(file_name,lines):
    print(file_name, "contains:\n")
    for line in lines:
        print(line,end="")

def remove_punctuation(split_lines):
    punctuation = "~!@#$%^&*()_+`-=[]{}\|:;'<>,.?/\""
    new_split_lines=[]
    for word in split_lines:
        new_word = word.strip(punctuation)
        lowercase_new_word = new_word.lower()
        new_split_lines.append(lowercase_new_word)
    return new_split_lines
    
def add_word_to_concordance(a_word,number_of_lines,concordance):
    if len(a_word) > 0:
        if a_word in concordance.keys():
            concordance[a_word].append(number_of_lines)
        else:
            concordance[a_word]=[number_of_lines]

def print_concordance(concordance):
    keys=list(concordance.keys())
    keys.sort()
    for word in keys:
        # the "*" prints the list without the brackets
        print(word,":",*concordance[word],sep=" ")
    
main()
