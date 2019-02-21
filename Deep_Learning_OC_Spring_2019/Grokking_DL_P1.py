#User: Trevor Martin
#Date of Completion: 4 February 2019
#Book: Grokking Deep Learning, Author: Andrew W. Trask
#Language: Python 3

#==================================================================================================
#VECTOR_MATH_CHALLENGE | Page 31
#==================================================================================================
vector_1 = [5,13,7]
vector_2 = [11,12,2]

def elementwise_multiplication(vector_1, vector_2):
	assert(len(vector_1) == len(vector_2))
	vector_3 = []
	new_element = 0 
	for element in range(len(vector_1)):
		new_element += vector_1[element] * vector_2[element]
		vector_3.append(new_element)
	return vector_3

def elementwise_addition(vector_1,vector_2):
	assert(len(vector_1) == len(vector_2))
	vector_3 = []
	new_element = 0 
	for element in range(len(vector_1)):
		new_element += vector_1[element] + vector_2[element]
		vector_3.append(new_element)
	return vector_3

def vector_sum(vector_1):
	summation = 0
	for element in range(len(vector_1)):
		summation += vector_1[element]
	return summation

def vector_average(vector_1):
	summation = 0
	for element in range(len(vector_1)):
		summation += vector_1[element]
	average = summation // len(vector_1)
	return average

def dot_product(vector_1,vector_2):
	vector_3 = elementwise_multiplication(vector_1,vector_2)
	vector_3 = vector_sum(vector_3)
	return vector_3

print(dot_product(vector_1, vector_2))
