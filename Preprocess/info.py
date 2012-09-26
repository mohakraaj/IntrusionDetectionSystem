from attributes import * 


N=6000	#Number of training elements in the new reduced data set
Data_set=open('../kddcup.data','r')
Reduced_set=open('Reduced_kddcup.data','w') # The new reduced data set 

# counts 
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

# Attacks categorized to 4 type 
dos=["back","land","neptune","pod","smurf","teardrop"] #type 1 attack
r2l=["ftp_write","guess_passwd","imap","multihop","phf","spy","warezclient","warezmaster"] # type 2  
u2r=["buffer_overflow","loadmodule","perl","rootkit"] #type 3 
probe=["nmap","satan","ipsweep","portsweep"] # type 4


def Info_quantify():
	i=1
	for line in Data_set:
			info=line.split(",")
			classi=info[41][:-2] # -2 bcoz there is a '.\n' after the class name 
			try:
				info[1]=eval(info[1])
			except:
				info[1]=0
			try:
				info[2]=eval(info[2])
			except:
				info[2]=0	
			try:
				info[3]=eval(info[3])
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

	print Max
	print Min				
""" After Calling Info_quantify Max and Minimum Values are found """

#comment the below lines if you are calling Info_quantify
#Max=[58329.0, 3.0, 70.0, 11.0, 1379963888.0, 1309937401.0, 1.0, 3.0, 14.0, 77.0, 5.0, 1.0, 7479.0, 1.0, 2.0, 7468.0, 43.0, 2.0, 9.0, 0.0, 1.0, 1.0, 511.0, 511.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 255.0, 255.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1]
#Min=[0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100000]
def Info_Normalize():
	i=1
	Data_set=open('../kddcup.data','r')
	for line in Data_set:
		if i<N:
			info=line.split(",")
			classi=info[41][:-1] # -1 bcoz there is a '.' after the class name 
			try:
				info[1]=eval(info[1])
			except:
				info[1]=0
			try:
				info[2]=eval(info[2])
			except:
				info[2]=0	
			try:
				info[3]=eval(info[3])
			except:
				info[3]=0	
			for j in range(41):
				if(Min[j]!=Max[j]):	
					info[j]=(float(info[j])-Min[j])/(Max[j]-Min[j])
				else:
					info[j]=0	
			info[41]=info[41][:-2]		
			Reduced_set.write(str(info))
			Reduced_set.write('\n')	
			i+=1
		else:
			return 	

Info_quantify()
Info_Normalize()
print "count_normal",count_normal
print "count_dos",count_dos
print "count_u2r",count_u2r
print "count_r2l",count_r2l
print "count_probe",count_probe


