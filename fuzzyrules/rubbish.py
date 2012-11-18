Attributes=[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

def code_generator(i):
	stre="""def low"""+str(i)+"""(x):
 	if x<centers["""+str(i)+"""][0]:
 		return 1
 	if x>centers["""+str(i)+"""][0] and x<centers["""+str(i)+"""][1]:
 		return ((x-centers["""+str(i)+"""][1])/(centers["""+str(i)+"""][0]-centers["""+str(i)+"""][1]))
 	if 	x>centers["""+str(i)+"""][1]:
 		return 0	
 			
def medium"""+str(i)+"""(x):
 	if x<centers["""+str(i)+"""][0]:
 		return 0
 	if x==centers["""+str(i)+"""][1]:
 		return 1	
 	if x>centers["""+str(i)+"""][0] and x<centers["""+str(i)+"""][1]:
 		return ((x-centers["""+str(i)+"""][1])/(centers["""+str(i)+"""][1]-centers["""+str(i)+"""][0]))
 	if x>centers["""+str(i)+"""][1] and x<centers["""+str(i)+"""][2]:
 		return ((x-centers["""+str(i)+"""][2])/(centers["""+str(i)+"""][1]-centers["""+str(i)+"""][2]))
 
 	if 	x>centers["""+str(i)+"""][2]:
 		return 0	

def high"""+str(i)+"""(x):
 	if x<centers["""+str(i)+"""][2]:
 		return 0
 	if x>centers["""+str(i)+"""][1] and x<centers["""+str(i)+"""][2]:
 		return ((x-centers["""+str(i)+"""][1])/(centers["""+str(i)+"""][2]-centers["""+str(i)+"""][1]))
 	if 	x>centers["""+str(i)+"""][2]:
 		return 1	"""
 	print stre	

def main():	
	for i in Attributes:
		code_generator(i)
 

if __name__ == '__main__':
 	main()			

