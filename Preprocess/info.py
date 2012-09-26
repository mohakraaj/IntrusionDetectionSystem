from attributes import * 


N=3000	#Number of training elements in the new reduced data set
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


# Numercial values to Protocols 
tcp=1
udp=2
icmp=3


# Numerical values to Services
IRC = 1
X11 = 2
Z39_50 = 3
aol = 4
auth = 5
bgp = 6
courier = 7
csnet_ns = 8
ctf = 9
daytime = 10
discard = 11
domain = 12
domain_u = 13
echo = 14
eco_i = 15
ecr_i = 16
efs = 17
finger = 19
ftp = 20
ftp_data = 21
gopher = 22
harvest = 23
hostnames = 24
http = 25
http_2784 = 26
http_443 = 27
http_8001 = 28
imap4 = 29
iso_tsap = 30
klogin = 31
kshell = 32
ldap = 33
link = 34
login = 35
mtp = 36
name = 37
netbios_dgm = 38
netbios_ns = 39
netbios_ssn = 40
netstat = 41
nnsp = 42
nntp = 43
ntp_u = 44
other = 45
pm_dump = 46
pop_2 = 47
pop_3 = 48
printer = 49
private = 50
red_i = 51
remote_job = 52
rje = 53
shell = 54
smtp = 55
sql_net = 56
ssh = 57
sunrpc = 58
supdup = 59
systat = 60
telnet = 61
tftp_u = 62
tim_i = 63
time = 64
urh_i = 65
urp_i = 66
uucp = 67
uucp_path = 68
vmnet = 69
whois = 70

# Numerical Values to Flag 
OTH = 1
REJ = 2
RSTO = 3
RSTOS0 = 4
RSTR = 5
S0 = 6
S1 = 7
S2 = 8
S3 = 9
SF = 10
SH = 11

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
		if i<6000:
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


