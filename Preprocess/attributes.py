# this file gives crisp numerical values to all the non-numerical values in the data set 

# Attacks categorized to 4 type 
dos=["back","land","neptune","pod","smurf","teardrop","snmpgetattack"] #type 1 attack
r2l=["ftp_write","guess_passwd","imap","multihop","phf","spy","warezclient","warezmaster"] # type 2  
u2r=["buffer_overflow","loadmodule","perl","rootkit"] #type 3 
probe=["nmap","satan","ipsweep","portsweep"] # type 4


# List of protocols used 
Protocols=["tcp","udp","icmp"]

# List of Services used  
Services=["IRC","X11","Z39_50","aol","auth","bgp","courier","csnet_ns","ctf","daytime","discard","domain","domain_u","echo ","eco_i ","ecr_i ","efs ","finger","ftp","ftp_data","gopher","harvest","hostnames","http","http_2784","http_443","http_8001","imap4","iso_tsap","klogin","kshell","ldap","link","login","mtp","name","netbios_dgm","netbios_ns","netbios_ssn","netstat","nnsp","nntp","ntp_u","other","pm_dump","pop_2"
"pop_3","printer","private","red_i","remote_job","rje","shell","smtp","sql_net","ssh","sunrpc","supdup","systat","telnet","tftp_u","tim_i","time","urh_i","urp_i","uucp","uucp_path","exec","vmnet","whois"]

# List of Flags used  
Flag=["OTH","REJ","RSTO","RSTOS0","RSTR","S0","S1","S2","S3","SF ","SH "]

#Attribute list after Feature selection 
#Features=[1,10,12,16,17,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,4,40,41,6,8]

#Attribute list With out Feature selection
Features=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

count_normal=0
count_dos=0
count_r2l=0
count_u2r=0
count_probe=0
