### MATH995H | Recommender Systems | Oberlin College

Here I document my coursework for the half course private reading called Recommender Systems. I have edited the projects and practice to remove any imperfections in the code, though there still may exist some poor design decisions. I may occassionally update this work to improve the code and add comments. If there are any faults that you see please contact me: tmartin2@oberlin.edu

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
#				      math.summation(sub N)(|s (sub i,N)|)
#		And here is the equation for similarity
#		sim(i,j) = cos(i-> * j->) = (i-> * j->)/(||i->||**2 * ||j->||**2)
#		
#		What occurs when a new user or new item is visible to the dataset?
#		For this there are Visitor or Product Cold Starts. No preferences for the user are known, so for Visitor Cold
#		Start the most popular items are recommended to the user until their preferences are known. Content
#		based filtering allows a product to be integrated into the system before the user actions determine its
#		popularity; this is for Product Cold Start.
#=======================================================================================================


