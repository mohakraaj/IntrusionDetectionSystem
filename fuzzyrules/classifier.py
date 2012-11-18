import random
import sys
import math 
""" work left 
Singularity not taken care :P 
how to obtain values for constants 
	fuzziness and epsilon"""

#intialize the variables 

N=2000 # number of data records
C=3 # number of clusters
max_iter=100 # maximum number of iterations 
m= 3 # fuzzyness
epsilon=0.05 # epsilon for termintation of the loop 
iterations=0 # number of iterations 
membership=[] # matrix of membership function 
#new_mu[N][C] # matrix for updating member ship funciton 
data=[] # data records 
centers=[] # list of centroids of data records 
old_obj=0
new_obj=0
def fcm(records):
	""" returns centers- list of centers , membership-membership relation matrix """

   	global data, membership, iterations, centers	
   	error=epsilon+1
   	data=records 
   	max_iter=int(sys.argv[1]) #remove
   	#print max_iter 
	initialize()
	new_obj=objective_func(membership)
	while(error>epsilon and iterations<max_iter):
		update_centers()
		iterations+=1
		error=update_matrix()
	#	print "error-",error

	update_centers()

	print max_iter,"--",iterations

	print_matrix([centers])
	return 0 

def update_matrix():
	""" this function updates the membership matrix for each iterations based on the centers
	     return the change in the previous and updated matrix """
	
	global data, membership, iterations, centers, old_obj, new_obj

	old_obj=new_obj	
	for i in range(N):
		for j in range(C):
			newU=0
			for k in range(C):
				newU+=(distance(data[i],centers[j])/distance(data[i],centers[k]))**(2/m-1)	

			newU=1.0/newU	

			membership[i][j]=(newU)
	new_obj=objective_func(membership)		
	square_difference=distance(old_obj,new_obj)

	#print square_difference		
	return square_difference					

def objective_func(member):
	"This is the objective function"
	global data,centers
	sumf=0
	for i in range(N):
		for j in range(C):
			sumf+=(member[i][j]**m)*((data[i]-centers[j])**2)
	#print "\n","-",sumf,"--"
	return sumf		

def update_centers():
	""" this function updates the centroid list based on the membership function """
	global data, membership, iterations, centers

	for j in range(C):
		numerator=0
		denomiator=0
		for i in range(N):
			numerator+=(membership[i][j]**m)*data[i]
			denomiator+=(membership[i][j]**m)
		centers[j]=numerator/denomiator
	#print len(centers),"---->",
	print_matrix([centers])

def initialize():
	"""this function initializes the membership matrix for the zero'th iteration and sets the number of clusters required """

	global data, membership, iterations, centers,m

	# initialize data structures 
	membership=[ [] for i in range(N) ]
	for i in range(N):
		for j in range(C):
			membership[i].append(random.random())

	for i in range(C):
		centers.append(0)

"""
trying to change on the basis of matlab code :P 
# this function gives the euclidean distance between two points 
def dist(list1, list2 ): 
	sume=0
	for i in range(len(len1)):
		sume+=(list1[i]-list2[i])**2
	return (sume**(0.5))	

# this function finds the rate of change in the data obtained 
def obj_function():
"""



def distance(a,b):
	diff=0.0
	diff=a-b
	return abs(diff)

def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print matrix[i][j],
#		print '\n'	


