# Author: Trevor Martin
# Date of Completion: 17 April 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 8, distill.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# This program takes text and removes the most common words from it.
#===================================================================================================

def main():
    finished = False
    while not finished:
        try:
            dictionary_of_words = {}
            common_words_to_replace=[]
            words_and_commonality_list=[]
            # have the user enter a file and the num of common words to eliminate
            file_name=input("Please provide a file of your liking to be distilled: ")
            num_of_common_words_to_replace=int(input("Word eradication time! Please provide a number of most common words you want removed: "))
            # begin reading the file and lines
            file_contents=open(file_name,"r")
            lines=file_contents.readlines()
            # for each line in the file
            for line in lines:
                # split the line into a list of words
                word_list=line.split()
                # for each word in the word_list 
                for word in word_list:
                    # remove leading and trailing characters
                    word_stripped = word.strip()
                    # remove punctuation
                    string = remove_punctuation(word_stripped)
                    
                    # if the word already has occurred in the dictionary 
                    if string in dictionary_of_words.keys():
                        # increase its occurrences
                        dictionary_of_words[string]+=1
                    else:
                        # if the word has not occurred before, give it one to start
                        dictionary_of_words[string] = 1
                
            for word in dictionary_of_words.keys():
                # create a tuple that has a word and its count
                word_and_its_count=(word,dictionary_of_words[word])
                # add this to the list 
                words_and_commonality_list.append(word_and_its_count)
            for pair_index in range(len(words_and_commonality_list)):
                index_for_most_common = pair_index
                for j in range(pair_index+1, len(words_and_commonality_list)):
                    if words_and_commonality_list[index_for_most_common][1] < words_and_commonality_list[j][1] :
                        index_for_most_common = j
                words_and_commonality_list[pair_index], words_and_commonality_list[index_for_most_common] = words_and_commonality_list[index_for_most_common], words_and_commonality_list[pair_index]
            print(words_and_commonality_list)
            for i in range(len(words_and_commonality_list)):
                if i < num_of_common_words_to_replace:
                    common_words_to_replace.append(words_and_commonality_list[i][0])
            for line in lines:
                words = line.split()
                for word in words:             
                    word_stripped=word.strip()
                    string=remove_punctuation(word_stripped)
                    if string not in common_words_to_replace:
                        print(word, end = " ")
                print()
            file_contents.close()
        except FileNotFoundError:
            print("\nIt's okay, do not fret, please enter a valid file today, and you'll be set!")

def remove_punctuation(word):
    punctuation="~!@#$%^&*()_+`-=[]{}\|:;'<>,.?/\""
    cleaned_word=""
    for letter in word:
        update_letter=letter.strip(punctuation)
        lowercase_updated_letter = update_letter.lower()
        cleaned_word+=lowercase_updated_letter
    return cleaned_word

main()








































            
            
