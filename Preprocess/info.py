from attributes import * 
import sys


N=6000	#Number of training elements in the new reduced data set

# counts of each class 
count_normal=0
count_dos=0
count_r2l=0
count_u2r=0
count_probe=0
Max=[]
Min=[]

#initialsize Max and Min 
for i in range(42):
	Max.append(-1)

for i in range(42):
	Min.append(100000)


def Info_quantify():
	i=1
	global count_normal,count_dos,count_probe,count_u2r,count_r2l
	for line in Data_set:
			info=line.split(",")
			classi=info[41][:-2] # -2 bcoz there is a '.\n' after the class name 
			try:
				info[1]=Protocol.index(info[1])+1
			except:
				info[1]=0
			try:
				info[2]=Service.index(info[2])+1
			except:
				info[2]=0	
			try:
				info[3]=Flag.index(info[3])+1
			except:
				info[3]=0	
			for j in range(41):
				if float(info[j])>Max[j]:
					Max[j]=float(info[j])
				if float(info[j])<Min[j]:
					Min[j]=float(info[j])
			

			if (classi=='normal'):
				count_normal+=1
			elif(dos.count(classi)!=0):
				count_dos+=1

			elif(u2r.count(classi)!=0):
				count_u2r+=1	
			
			elif(r2l.count(classi)!=0):
				count_r2l+=1

			elif(probe.count(classi)!=0):
				count_probe+=1	

#	print Max
#	print Min				
""" After Calling Info_quantify Max and Minimum Values are found """

#comment the below lines if you are calling Info_quantify
#Max=[58329.0, 0.0, 0.0, 9.0, 693375640.0, 5155468.0, 1.0, 3.0, 3.0, 30.0, 5.0, 1.0, 884.0, 1.0, 2.0, 993.0, 28.0, 2.0, 8.0, 0.0, 0.0, 1.0, 511.0, 511.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 255.0, 255.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1]
#Min=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100000]

def Info_Normalize():
	global name
	Data_set=open(name,'r')
	for line in Data_set:
	
		info=line.split(",")
		classi=info[41][:-1] # -1 bcoz there is a '.' after the class name 
		try:
			info[1]=Protocol.index(info[1])+1
		except:
			info[1]=0
		try:
			info[2]=Service.index(info[2])+1
		except:
			info[2]=0	
		try:
			info[3]=Flag.index(info[3])+1
		except:
			info[3]=0	
		for j in range(41):
			if(Min[j]!=Max[j]):	
				info[j]=(float(info[j])-Min[j])/(Max[j]-Min[j])
			else:
				info[j]=0	

		classi=info[41][:-2] #this is to remove that the '.\n

		if (classi=='normal'):
			info[41]=0
		elif(dos.count(classi)!=0):
			info[41]=1

		elif(u2r.count(classi)!=0):
			info[41]=2	
		
		elif(r2l.count(classi)!=0):
			info[41]=3

		elif(probe.count(classi)!=0):
			info[41]=4	

		# writing output in a SVM format 
		Reduced_set.write(str(info[41])+" ")

		for j in range(41):
			if (Features.count(j+1)!=0):
				Reduced_set.write(str(j+1)+":"+str(info[j])+" ")

		Reduced_set.write('\n')	
	else:
		return 									
				
if __name__=='__main__':
	if len(sys.argv)<2:
		print "Damn...Few Arguments missing"
		exit(0) 
	name=sys.argv[1]	
	Data_set=open(name,'r')
	Reduced_set=open('Reduced_'+name,'w') # The new reduced data set 
	
	Info_quantify()
	Info_Normalize()
	print "The Features Set Used is : "
	print "------------------------------------"
	print str(Features)

