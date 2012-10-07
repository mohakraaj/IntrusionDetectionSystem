import sys 
import random
from random import randrange

Data_set=[]
max_idx=5000

def Randomize(data):
	size = len(data)
	for i in range(size):
		ri = randrange(0, size-i)
		tmp = data[ri]
		data[ri] = data[size-i-1]
		data[size-i-1] = tmp
	return data	

if __name__=='__main__':
	if len(sys.argv)<2:
		print "Damn .. Few arguments missing"
		exit(0)
	else :
		file_name=sys.argv[1]
		
	file_p=open(file_name,'r')			
	new_file=open('randata.data','w')
	for line in file_p:
		Data_set.append(line)
	file_p.close()

	Data_set=Randomize(Data_set)

	for ele in Data_set:
		if(max_idx>0):
			new_file.write(ele)
		else:
			break	
		max_idx-=1	
