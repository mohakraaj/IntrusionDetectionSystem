from classifier import fcm 

def main():
	data=open("data_classifier","r")
	records=[]
	for line in data:
		records.append(float(line))
	#records.sort()
	fcm(records)	



if __name__ == '__main__':
	main()


