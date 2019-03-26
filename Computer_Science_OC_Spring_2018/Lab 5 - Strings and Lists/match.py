# Author: Trevor Martin and Justin Bank
# Date of Completion: 16 March 2018
# Language: Python3
# Class: CSCI 150 | Introductory Computer Science | Oberlin College
# Homework#: 5, match.py
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# A program that compares two sequences and finds the one with the positions with the fewest
# mismatches between the two
#===================================================================================================

# find matches function
def find_matches(first_sequence,sequences):
	most_matches = 0
	position_of_most_matches = 0
	# loop through the 
	for first_seq in range (len(first_sequence) - len(sequences) + 1):
		matches = 0
		# loop through the length of the smaller sequence
		for sequence in range (len(sequences)):
			# store the subsequence index
			seq_index = sequence
			# and store the larger sequence index
			first_index = first_seq + sequence
			# if they match matches increases
			if first_sequence[first_index] == sequences[seq_index]:
				matches += 1
		# we find where the most matches are and get the position
		if matches > most_matches:
			most_matches = matches
			position_of_most_matches = first_seq
	# the difference between the matches and length is the mismatches
	mismatches = len(sequences) - most_matches
	return mismatches, position_of_most_matches

def eliminate_newline_character_at_EOL(line):
	removed_newline_char = line[:-1]
	return removed_newline_char

def main():	
	done = False
	while not done:
		try:
			# get user file
			user_file = input("What file would you like to use?: ")
			reading_file = open(user_file,"r")
			done = True
		except(FileNotFoundError):
			print("Enter a good file.")
	
	# create list to store the sequences	
	sequences = []
	# find the number of lines
	num_lines = 0
	for line in reading_file:
		num_lines += 1
	# we will find the number of mismatches and the index for each of many sequences
	sequence_error_value = [0]* (num_lines - 1)
	sequence_index = [0]* (num_lines - 1)
	# set cursor back to the beginning of the line
	reading_file.seek(0)
	# read the first line because that has the first sequence we compare everything to
	first_sequence = reading_file.readline()
	first_sequence = eliminate_newline_character_at_EOL(first_sequence)
	
	# each line in the file is a sequence, so we store each one in sequences
	for sequence in reading_file:
		sequences.append(eliminate_newline_character_at_EOL(sequence))
	# find where the lowest mismatches are and where their corresponding positions are
	for index in range(len(sequences)):
		sequence_error_value[index], sequence_index[index] = find_matches(first_sequence, sequences[index])
	# print out the message with the number of mismatches and position
	for iteration in range (len(sequence_index)):
		print("Sequence ",iteration+1," has ",sequence_error_value[iteration], " mismatches at position ",
			  sequence_index[iteration],".",sep ="")

main()

























