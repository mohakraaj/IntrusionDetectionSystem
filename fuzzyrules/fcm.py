import random
from numpy import * 
import peach as P 
maxe=100000 # this is the number of records for the training data 
#attributes_list=[1,4,6,8,10,12,16,17,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
attributes_list=[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
#quantitative_attributes=[0, 4, 5, 7, 8, 9, 10, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
number_attributes=len(attributes_list)# considering only quantitative data
#number_attributes=2
centers=[[] for j in range(number_attributes)] # array of centers of each attribute 

membership_matrix=[]

data=[[] for i in range(number_attributes)]

fcm=[[] for i in range(number_attributes)] # stores fcm objects

m=1.25 # fuzziness constant 


##
# files for bullshit 
center_file=open('center_file','w')
membership_matrix_file=open('membership_matrix_file','w')

##
def main():
	records=open('spu_result','r')
	number_records=0
	for transaction in records:
		transaction=eval(transaction)
		i=0
		for e in attributes_list:
			data[i].append(transaction[e])
			i+=1
		number_records+=1	
	#for i in range(number_attributes):
		#print array(data[i])
	#number_records=
	for i in range(number_attributes):
		membership_matrix.append([])
		for j in range(number_records):
			membership_matrix[i].append([])
			for k in range(3):
				membership_matrix[i][j].append(random.random())
	#membership_matrix=[[[random.random() for i in range(3)] for j in range(number_records)] for k in range(number_attributes)]
	print number_records,"---", len(membership_matrix[0]),"--"
	for i in range(number_attributes):
		x=array(data[i])
		mu=array(membership_matrix[i])
		fcm[i]=P.FuzzyCMeans(x,mu,m)
		centers[i]=fcm[i].c
		membership_matrix[i]=fcm[i].mu
		center_file.write(str(centers[i]))
		center_file.write('\n')
		membership_matrix_file.write(str(membership_matrix[i]))	
		membership_matrix_file.write('\n')
	print membership_matrix[0][12345][2]	
	records.close()


if __name__ == '__main__':
	main()
	center_file.close()
	membership_matrix_file.close()
