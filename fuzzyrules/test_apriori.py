""" this is the implementation for modified apriori algorithm (kuok's algorithm) 
minsupport and minconfidence are assumed  
"""
from copy import deepcopy
from fuzzysubset import *

minsupport=0.4 # minimum support required to obtain fuzzy rules
minconfidence=0.8 # minimum confidence required to obtain fuzzy rules

#data is in the format of [{1:2, 2:4 , 3:4.5 , 4: 1.2 }]
# attributeinfo gives the relevant information about the attribute format is {1:[low1 , medium1 ], 2:[low, high, medium] }.etc

Large_set=[]

candidate_set=[]

candidate_set_count=[]

number_records=0 

#attributeinfo={0:['tcp','udp','icmp'],1: ['low1', 'medium1', 'high1'], 2: ['low2', 'high2'], 3: ['low3', 'medium3', 'high3'], 4: ['low4', 'medium4', 'high4'], 5: ['low5', 'medium5', 'high5'], 6: ['low6', 'medium6', 'high6'], 7: ['low7', 'medium7', 'high7'], 8: ['low8', 'medium8', 'high8'], 9: ['low9', 'medium9', 'high9'], 10: ['low10', 'medium10', 'high10'], 11: ['low11', 'medium11', 'high11'], 12: ['low12', 'medium12', 'high12'], 13: ['low13', 'medium13', 'high13'], 14: ['low14', 'medium14', 'high14'], 15: ['low15', 'medium15', 'high15'], 16: ['low16', 'medium16', 'high16'], 17: ['low17', 'medium17', 'high17'], 18: ['low18', 'medium18', 'high18'], 19: ['low19', 'medium19', 'high19'], 20: ['low20', 'medium20', 'high20'], 21: ['low21', 'medium21', 'high21'], 22: ['low22', 'medium22', 'high22'], 23: ['low23', 'medium23', 'high23'], 24: ['low24', 'medium24', 'high24'], 25: ['low25', 'medium25', 'high25'], 26: ['low26', 'medium26', 'high26'], 27: ['low27', 'medium27', 'high27'], 28: ['dos','r2l','u2r','probe','normal']}

attributeinfo={0:['tcp','udp','icmp'],1: ['low1', 'medium1', 'high1'], 2: ['low2', 'high2'], 3: ['low3', 'medium3', 'high3'],4: ['low4', 'medium4', 'high4'], 27: ['low27', 'medium27', 'high27'], 28: ['dos','r2l','u2r','probe','normal'] }

data=[]

def AprioriAlgo(data):
	print "Entering AprioriAlgo"
	Large_set.append(initialize(data))
	k=1
	candidate_set.append([])  # there is no candidate key for 1st generation 
	candidate_set_count.append([]) # there is no candidate key for 1st generation 
	while(len(Large_set[k-1])!=0):
		candidate_set.append(Apriori_gen(Large_set[k-1]))
		candidate_set_count.append([0 for i in range(len(candidate_set[k]))])
 		for transaction in data:
 			i=0
 			for ele in candidate_set[k]:
 				count=1
 				for c in ele:
 					if type(transaction[c])!=str:
						func=str(ele[c])+"("+str(transaction[c])+")"
					else:
						func=str(ele[c])+"("+"\""+str(transaction[c])+"\""+")"
			#print eval(func)
					if eval(func)==None:
						print "Error Message ....."
						print ele[c], transaction[c]	
					else:	
						count=count*(eval(func))

				candidate_set_count[k][i]+=count
				i+=1

		Large_set.append([])
		i=0
		for c in candidate_set[k]:
			if float(candidate_set_count[k][i])/float(number_records)>=minsupport:
				Large_set[k].append(c)
			i+=1
		
		print Large_set[k]						
		k+=1
	return Large_set	


# Large_gen is a list of dictionaries of the form [{item1: low, item2:veryhigh}, {item3: low, item4 :medium}]

def Apriori_gen(Large_gen):
	print "Entering Apriori_gen "
	candidate=[]
	reduced_candidates=[]
	length=len(Large_gen[0]) # Weak point 
	for X in Large_gen:
		for Y in Large_gen:
			new_dict={}
			if X!=Y:
				x=X.items()
				y=Y.items()
				flag=0
				for i in range(0,length-1):
					if x[i]!=y[i]:
						flag=1

				if max(X)>=max(Y):
					flag=1
				if flag==0:	
					new_dict=deepcopy(X)
					new_dict[max(Y)]=Y[max(Y)]
					#print new_dict,"--",X	
					candidate.append(new_dict)

	#print "Printing Candidates ",candidate
	
	for ele in candidate:
		flag=0
		for c in ele:
			Z=deepcopy(ele)
			Z.pop(c)
			try:
				Large_gen.index(Z)
			except:
				flag=1	
		if flag==0:
			reduced_candidates.append(ele)
					
	#print "Printing reduced candidates",reduced_candidates
	print "Exiting Apriori_gen"
	return reduced_candidates		



def initialize(data):
	global number_records,attributeinfo

	candidate=[]
	candidate_count=[]
	number_records=len(data)
	Large_init=[]
	for c in attributeinfo:
		for ele in attributeinfo[c]:
			new_dict={}
			new_dict[c]=ele
			candidate.append(new_dict)
			candidate_count.append(0)

	#print candidate
	#print candidate_count,low1(2)		
	for transaction in data:
		i=0
		for ele in candidate:
			c=min(ele)
			if type(transaction[c])!=str:
				func=str(ele[c])+"("+str(transaction[c])+")"

			else:
				func=str(ele[c])+"("+"\""+str(transaction[c])+"\""+")"
			#print eval(func)
			if eval(func)==None:
				print "Error Message ....."
				print ele[c], transaction[c]	
			else:	
				candidate_count[i]+=(eval(func))
			i+=1
									
	i=0		
	for ele in candidate:				
		if float(candidate_count[i])/float(number_records)>=minsupport:
			Large_init.append(ele)
		i+=1	

	print "Exiting initialization ", Large_init	

	return Large_init



def main():
	global n 
#	record=open('spu_result','r')
	print "Entering  main...."
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
