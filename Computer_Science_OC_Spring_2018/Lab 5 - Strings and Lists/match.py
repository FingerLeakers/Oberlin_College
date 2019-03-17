#match.py
#finds some matches in some sequences
#
#Justin Bank & Trevor Martin
#March 16, 2018
def findMatch(fullLine,sequences):
	maxMatches = 0
	pos = 0
	for i in range (len(fullLine)-len(sequences)+1):
		matches = 0
		for j in range (len(sequences)):
			seqIndex = j
			fullIndex = i+j
			if fullLine[fullIndex] == sequences[seqIndex]:
				matches +=1
		if matches > maxMatches:
			maxMatches = matches
			pos = i
	diff = len(sequences)-maxMatches
	return diff, pos

def noBreak(line):
	line = line[:-1]
	return line

def main():	
	done = False
	while not done:
		try:
			file = input("What file would you like to use? ")
			inputFile = open(file,"r")
			done = True
		except(FileNotFoundError):
			print("Enter an extant file!")
	sequences = []
	lineCount = 0
	for i in inputFile:
		lineCount += 1
	error = [None]* (lineCount-1)
	index = [None]* (lineCount-1)
	inputFile.seek(0)
	fullLine = inputFile.readline()
	fullLine = noBreak(fullLine)
	
	for i in inputFile:
		sequences.append(noBreak(i))
		
	for i in range(len(sequences)):
		error[i], index[i] = findMatch(fullLine, sequences[i])
		
	print(error)
	print(index)
	for i in range (len(index)):
		print("Sequence ", i+1, " has ", error[i], " errors at position ", index[i], ".", sep ='')

main()


