""" this is the implementation for modified apriori algorithm (kuok's algorithm) 
minsupport and minconfidence are assumed  
"""
from copy import deepcopy
from fuzzysubset import *

minsupport=0.2 # minimum support required to obtain fuzzy rules
minconfidence=0.4 # minimum confidence required to obtain fuzzy rules
#data is in the format of [{1:2, 2:4 , 3:4.5 , 4: 1.2 }]
# attributeinfo gives the relevant information about the attribute format is {1:[low1 , medium1 ], 2:[low, high, medium] }.etc

Large_set=[]

candidate_set=[]

candidate_count=[]

n=0 

#attributeinfo={0:['tcp','udp','icmp'],1: ['low1', 'medium1', 'high1'], 2: ['low2', 'high2'], 3: ['low3', 'medium3', 'high3'], 4: ['low4', 'medium4', 'high4'], 5: ['low5', 'medium5', 'high5'], 6: ['low6', 'medium6', 'high6'], 7: ['low7', 'medium7', 'high7'], 8: ['low8', 'medium8', 'high8'], 9: ['low9', 'medium9', 'high9'], 10: ['low10', 'medium10', 'high10'], 11: ['low11', 'medium11', 'high11'], 12: ['low12', 'medium12', 'high12'], 13: ['low13', 'medium13', 'high13'], 14: ['low14', 'medium14', 'high14'], 15: ['low15', 'medium15', 'high15'], 16: ['low16', 'medium16', 'high16'], 17: ['low17', 'medium17', 'high17'], 18: ['low18', 'medium18', 'high18'], 19: ['low19', 'medium19', 'high19'], 20: ['low20', 'medium20', 'high20'], 21: ['low21', 'medium21', 'high21'], 22: ['low22', 'medium22', 'high22'], 23: ['low23', 'medium23', 'high23'], 24: ['low24', 'medium24', 'high24'], 25: ['low25', 'medium25', 'high25'], 26: ['low26', 'medium26', 'high26'], 27: ['low27', 'medium27', 'high27'], 28: ['dos','r2l','u2r','probe','normal']}
attributeinfo={0:['tcp','udp','icmp'],1: ['low1', 'medium1', 'high1'], 2: ['low2', 'high2'], 3: ['low3', 'medium3', 'high3'] }
data=[]
def AprioriAlgo(data):
	print "Apriori running ...." 
	Large_set.append(initialize(data,attributeinfo))
#	Large_set.append([{0: 'tcp'}, {1: 'low1'}, {2: 'low2'}, {3: 'medium3'}, {4: 'low4'}, {5: 'low5'}, {6: 'low6'}, {7: 'low7'}, {8: 'medium8'}, {9: 'low9'}, {10: 'low10'}, {11: 'low11'}, {12: 'low12'}, {13: 'low13'}, {14: 'low14'}, {15: 'high15'}, {16: 'low16'}, {17: 'low17'}, {18: 'low18'}, {19: 'high19'}, {20: 'high20'}, {21: 'low21'}, {22: 'low22'}, {23: 'high23'}, {24: 'low24'}, {25: 'low25'}, {26: 'low26'}, {27: 'low27'}, {28: 'normal'}])
	k=0
	#print Large_set[0]
	while True:
		candidate_set.append(apriori_gen(Large_set[k],attributeinfo,k+2))	
		candidate_count.append([0 for i in range(len(candidate_set[k]))])

		for transaction in data:
			i=0
			count =1
			for ele in candidate_set[k]:
				for c in ele:	
					if type(transaction[c])!=str:
						func=str(ele[c])+"("+str(transaction[c])+")"
					else:
						func=str(ele[c])+"("+"\""+str(transaction[c])+"\""+")"	

					count+=min(count,eval(func))				

			candidate_count[k][i]+=count				
			i=i+1

		Large_set.append([])		
		i=0
		print k
		for c in candidate_set[k]:
			if candidate_count[k][i]/n>minsupport:
				Large_set[k+1].append(c)

		if len(Large_set[k+1])==0:
			break	

		k+=1	

		print "Large_set",Large_set[k]

	return Large_set
	
# record is a list of dictionaries of the form [{item1: low, item2:veryhigh}, {item3: low, item4 :medium}]


def apriori_gen(record,attributeinfo,k):
	candidate=[]
	print "apriori_gen ..."

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
						flag=0
						break
					i+=1					
				if(flag==1 and e<max(Y)):
					new_dict=X
					new_dict[max(Y)]=Y[max(Y)]

			candidate.append(new_dict)

	reduced_candidates=[]	
	print candidate
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
												
	print reduced_candidates				
	return reduced_candidates			

						

							
def initialize(data,attributeinfo):
	""" Atribute info is a dictionary of list {1:["low","medium","high"], 2:["medium",""]} """

	print "initializing .. "
	candidate=[]
	count=[] 
	for c in attributeinfo:
		for k in attributeinfo[c]:
			new_dict={}
			new_dict[c]=k
			candidate.append(new_dict)		

	print len(data)
	for transaction in data:
		for ele in candidate:
			c=min(ele)
			if type(transaction[c])!=str:
				func=str(ele[c])+"("+str(transaction[c])+")"
			else:
				func=str(ele[c])+"("+"\""+str(transaction[c])+"\""+")"	
			count.append(eval(func))				

	print "checking L0 support "
	Large_init=[]		
	i=0
	print candidate
	for c in candidate:
		if count[i]>minsupport:
				Large_init.append(c)		

		i+=1
	#print Large_init	
	print "initializing done "
	return Large_init			

def main():
	global n 
	record=open('spu_result','r')

	record=open('check','r')
	j=0
	result=[]
	for line in record:
		result=(eval(line))
		data.append({})
		for i in range(len(result)):
			data[j][i]=result[i]	
		j+=1		
	n=len(data)	
	#print data
	AprioriAlgo(data)
if __name__ == '__main__':
	main()
			