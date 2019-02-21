#User: Trevor Martin
#Date of Completion: 16 February 2019
#Book: Grokking Deep Learning, Author: Andrew W. Trask
#Language: Python 3

#==================================================================================================
#MEMORIZING CODE FOR NEURAL NETWORKS | Page 70
#==================================================================================================

# weight = 0.5
# goal_pred = 0.8
# _input = 2
# alpha = 0.1
# 
# for iteration in range(1000):
# 	print("-------------------\nWeight:",str(weight))
# 	pred = _input * weight
# 	error = (pred - goal_pred)**2 #mean squared error
# 	delta = pred - goal_pred
# 	derivative = _input * delta
# 	weight = weight - (alpha * derivative)
# 	print("Error:",str(error),"Prediction:",pred)
	
	
# goal_prediction = 1.9
# _input = 0.1
# weight = 0.5
# alpha = 1
# 
# for iteration in range(1000):
# 	prediction = _input * weight
# 	ms_error = (prediction - goal_prediction)**2
# 	derivative = (_input * (prediction - goal_prediction))
# 	weight = weight - (alpha * derivative)
# 	print("Error:",str(ms_error),"Prediction:",str(prediction))
	
# weight = 0.5
# goal_prediction = 100
# starting_input = 3
# alpha = 0.1
# 
# for iteration in range(100):
# 	prediction = starting_input * weight
# 	ms_error = (prediction - goal_prediction)**2
# 	derivative = (starting_input * (prediction - goal_prediction))
# 	weight = weight - (alpha * derivative)
# 	print("Error:",str(ms_error),"Prediction:",prediction)

# weight = 0.5
# goal_prediction = 543
# starting_input = 1
# alpha = 0.1
# 
# for iteration in range(1000):
# 	prediction = starting_input * weight
# 	ms_error = (prediction - goal_prediction)
# 	derivative = (starting_input * (prediction - goal_prediction))
# 	weight = weight - (alpha * derivative)
# 	print("Error:",str(ms_error),"Prediction:",str(prediction))
	
# weight = 0.75
# goal_pred = 234
# starting_input = 1
# alpha = 0.1
# 
# for iteration in range(1000):
# 	prediction = starting_input * weight
# 	ms_error = (prediction - goal_pred)**2
# 	derivative = (starting_input * (prediction - goal_pred))
# 	weight = weight - (alpha * derivative)
# 	print("Error:",str(ms_error),"Prediction:",str(prediction))
		
weight = 0.5
goal_prediction = 456
starting_input = 1
alpha = 0.1

for iteration in range(1000):
	prediction = (starting_input * weight)
	ms_error = (prediction - goal_prediction)**2
	derivative = (starting_input * (prediction - goal_prediction))
	weight = weight - (alpha * derivative)
	print("Error:",str(ms_error),"Prediction:",str(prediction))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	









	
	