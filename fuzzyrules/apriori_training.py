""" this is the implementation for modified apriori algorithm (kuok's algorithm) 
minsupport and minconfidence are assumed  
"""
from copy import deepcopy
from fuzzysubset import *

minsupport=0.3 # minimum support required to obtain fuzzy rules
minconfidence=0.4 # minimum confidence required to obtain fuzzy rules
#data is in the format of [{1:2, 2:4 , 3:4.5 , 4: 1.2 }]
# attributeinfo gives the relevant information about the attribute format is {1:[low1 , medium1 ], 2:[low, high, medium] }.etc
Large_set=[]
candidate_set=[]
candidate_count=[]
n= len(data)
def AprioriAlgo(data,attributeinfo):

	Large_set.append(initialize(data,attributeinfo))
	k=0
	while len(Large_set[k])!=0:
		candidate_set.append(apriori_gen(Large_set[k],attributeinfo,k+1))	
		candidate_count.append([0 for i in range(len(candidate_set[k]))])
		for transaction in data:
			i=0
			count =1
			for ele in candidate_set[k]:
				for c in ele:	
					func=str(ele[c])+"("+transaction[c]+")"
					count+=min(count,eval(func))				

			candidate_count[k][i]+=count				
				i=i+1

		Large_set.append([])
		k+=1
		i=0
		for c in candidate_set[k]:
			if candidate_count[k][i]/n>minsupport:
				Large_set[k].extend(c)

	return Large_set
	
# record is a list of dictionaries of the form [{item1: low, item2:veryhigh}, {item3: low, item4 :medium}]


def apriori_gen(record,attributeinfo,k):
	candidate=[]
	for X in record:
		for Y in record:
			new_dict={}
			if (X != Y):
				i=1
				flag=1
				for e in X:
					try:
						if (X[e]!=Y[e] and i!=k):
							flag=0
					except:
						i+=1
						continue 
					i+=1					
				if(flag==1 and e<max(Y)):
					new_dict.extend(X)
					new_dict[max(Y)]=Y[max(Y)]

			candidate.append(new_dict)

	reduced_candidates=[]	
	for ele in candidate:
		for c in ele: 
			Z=deepcopy(ele)
			Z.pop(c)
			flag=0
			for X in record:
				if(Z==X):
					flag=1
					break 
			if flag==1:
				reduced_candidates.append(ele)		
	return reduced_candidates			

						

							
def initialize(data,attributeinfo):
	""" Atribute info is a dictionary of list {1:["low","medium","high"], 2:["medium",""]} """

	candidate=[]
	count=[] 
	for c in attributeinfo:
		for k in attributeinfo[c]:
			new_dict={}
			new_dict[c]=k
			candidate.append(new_dict)		


	for transaction in data:
		for ele in candidate:
			c=min(ele)
			func=str(ele[c])+"("+transaction[c]+")"
			count.append(eval(func))				


	Large_init=[]		
	i=0
	for c in candidate:
		if count[i]>minsupport:
				Large_init.extend(c)		

		i+=1
	return Large_init			

			