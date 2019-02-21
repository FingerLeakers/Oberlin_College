#User: Trevor Martin
#Date of Completion: 11 February 2019
#Book: Grokking Deep Learning, Author: Andrew W. Trask
#Language: Python 3

#==================================================================================================
#HOT AND COLD LEARNING, NNs AS A SEARCH PROBLEM | Page 54
#==================================================================================================

weight = 0.5
_input = 0.5
goal_prediction = 0.8

step_amount = 0.001

for iteration in range(1101):
	
	prediction = _input * weight
	error = (prediction - goal_prediction)**2
	
	print("Error:",error,"Prediction:",prediction)
	
	up_prediction = _input * (weight + step_amount)
	up_error = (goal_prediction - up_prediction)**2
	
	down_prediction = _input * (weight - step_amount)
	down_error = (goal_prediction - down_prediction)**2
	
	if(down_error < up_error):
		weight -= step_amount
		
	else:
		weight += step_amount


















