# Author: Trevor Martin
# Date of Completion: -----
# Language: Python3
# Class: MATH995 | Recommender Systems | Oberlin College
# Instructor: Colin Dawson
#=======================================================================================================
# DESCRIPTION:
#=======================================================================================================
# This is the first recommender system trial I have been working on. It follows a tutorial on
# recommender systems; the code in this problem is largely used from this tutorial. Some personal
# notes on the content of the tutorial are present. I have begun testing using different datasets
# and different recommender system architectures. These are my own and use some of the same functions
# presented in this tutorial. Here is the link
# https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-recommendation-engine-python/
#=======================================================================================================
# ISSUES:
#=======================================================================================================
# None
#=======================================================================================================
# DEPENDENCIES:
#=======================================================================================================
import pandas 
import matplotlib
import matplotlib.pyplot
import numpy

from sklearn.metrics.pairwise import pairwise_distances 
#=======================================================================================================
# DATA COLLECTION AND STORAGE
#=======================================================================================================
user_columns = ['user_id','age','sex','occupation','zip_code']
users = pandas.read_csv('/Users/astrabrauer/Documents/MasterFolder/Inbox/ml-100k/u.user',
				    sep = '|', names = user_columns, encoding = 'latin-1')

rating_columns = ['user_id','movie_id','rating','unix_timestamp']
ratings = pandas.read_csv('/Users/astrabrauer/Documents/MasterFolder/Inbox/ml-100k/u.data',
					 sep = '\t', names = rating_columns, encoding = 'latin-1')

movie_columns = ['movie id','movie title','release date','video release date','IMDb URL','unknown',
	    'Action','Adventure','Animation','Children\'s','Comedy','Crime','Documentary','Drama',
	    'Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War',
	    'Western']
movies = pandas.read_csv('/Users/astrabrauer/Documents/MasterFolder/Inbox/ml-100k/u.item', sep = '|',
					names = movie_columns, encoding = 'latin-1')
#=======================================================================================================
# COLLABORATIVE FILTERING
#=======================================================================================================
number_of_users = ratings.user_id.unique().shape[0]
number_of_movies = ratings.movie_id.unique().shape[0]

#calculating similarity
user_movie_data_matrix = numpy.zeros((number_of_users, number_of_movies))
for line in ratings.itertuples():
	user_movie_data_matrix[line[1]-1, line[2]-1] = line[3]

#to calculate cosine similarity, use pairwise distance function
user_user_similarity = pairwise_distances(user_movie_data_matrix, metric = 'cosine')
item_item_similarity = pairwise_distances(user_movie_data_matrix.T, metric = 'cosine')

#make predictions based on the similiarities
def make_prediction_based_on(ratings, similarity, type = 'user'):
	if type == 'user':
		mean_user_rating = ratings.mean(axis = 1)
		ratings_difference = (ratings - mean_user_rating[:,numpy.newaxis])
		prediction = mean_user_rating[:,numpy.newaxis] + similarity.dot(ratings_difference)/numpy.array([numpy.abs(similarity).sum(axis=1)]).T
	elif type == 'item':
		prediction = ratings.dot(similarity)/numpy.array([numpy.abs(similarity).sum(axis=1)])
	return prediction
	
user_user_prediction = predict(user_movie_data_matrix, user_user_similarity, type = 'user')
item_item_prediction = predict(user_movie_data_matrix, item_item_similarity, type = 'item')
print(user_user_prediction)
print(item_item_prediction)
#=======================================================================================================
# NOTES
# Recommendation systems sift user data to find which items are most relevant or important.
# 	The system then recommends items to the users based on their preferences. The behavior of
#	the user must be recorded in order to maximize the likelihood that the user will return to
#    the site(have a positive experience) and continue to purchase goods. How does the company
#    go about making the most money? Well, it could recommend expensive products or recommend best
#    selling products. Usually the best approach is to appeal to user interests and foster loyalty.
# 
# Users can be clustered under different features or the most popular items can be recommended to
#	the majority of users. These both are not the best approaches, and oftentimes better approaches
#	will be necessary.
#
# Data is implicitly or explicitly collected. The former refers to logging user history, such as
#	searches or clicks, and the latter refers to user ratings such as an Amazon review. More data
#	means greater predictive power.
#
# Following data collection, there are different methods of filtering the data.
#	Content based filtering recommends similar things to what the user consumed in the past.
#		Its algorithm goes as follows: sim(A,B) = cos(theta) = (A * B)/(||A||||B||)
#		The similarity between profile A and item B can be found by calculating the above.
#		The cosine value will be between 1 and -1, a probability. From here a Top n approach
#		can be used where the top n movies are recommended to the user or a rating scale a
#		approach can be used, where all the movies above a certain threshold are recommended.

#		Two other algorithms that can be used are Euclidean's Distance, where the distances
#		between similar items (new ones and ones that user has purchased or attended to) is
#		calculated and the closest ones are recommended math.sqrt((x1-y1)**2+...+(xN-yN)**2)),
#		and Pearson's Correlation, which tells us how correlated two items are through

#		sim(u,v) = math.summation((r(sub u,i) - r(bar sub u))(r(sub v,i) - r(bar sub v))/
#				 (math.sqrt.summation((r(sub u,i) - r(bar sub u))**2)*
#				 math.sqrt.summation(r(sub v,i) - r(bar sub v))**2))

#		This approach, Pearson's correlation fails to predict new things that user will like and
#		essentially is trapped in only recommeding similar things to what the user has done in the
#		past.
#
#	Collaborative filtering finds similarities between users and then recommends the differences to the
#		each of the users, still try to make sure the different items share some similarity to the items
#		that where similar between the users.
#
#		User-User collaborative filtering finds similarities between users based on their data and then
#		recommends items between the users. This is good if the number of users is small.
#		P (sub u,i) = math.summation(sub v)((r (sub v,i) * s (sub u,v))/
#				    math.summation(sub v)(s (sub u,v))
#		Where P is a prediction for a user u of the summation of ratings by others users of item i
#		r (sub v,i) is the rating by a user v for item i and s (sub u,v) is the similarity between users.
#		So, for this prediction we need Pearson's Correlation for s (sub u,v). Based on the ratings between
#		two users, we find the similarity between those two users.
#
#		A problem is that you have to make a prediction for each correlation value. So instead of doing that
#		for all similarities it is between to find just a few neighbors. Some ways to get neighbors are to
#		(1) select a threshold of similarity, (2) randomly select the users, (3) choose the Top n neighbors in
#		similarity, or (4) use clustering to choose neighbors.
#
#		Item-Item collaborative filtering is another type of collaborative filtering. This is very similar to
#		user-user collaborative filtering but instead it takes the weighted sum of ratings of item neighbors not
#		of uesrs neighbors. Here is the equation for a prediction
#		P (sub u,i) = math.summation(sub N)((s (sub i,N) * R (sub u,N))/
#				    math.summation(sub N)(|s (sub i,N)|)
#		And here is the equation for similarity
#		sim(i,j) = cos(i-> * j->) = (i-> * j->)/(||i->||**2 * ||j->||**2)
#		
#		What occurs when a new user or new item is visible to the dataset?
#		For this there are Visitor or Prodcut Cold Starts. No preferences for the user are known, so for Visitor Cold
#		Start the most populat items are recommended to the user until their preferences are known. Content
#		based filtering allows a product to be integrated into the system before the user actions determine its
#		popularity; this is for Product Cold Start.
#=======================================================================================================