"""This file has functions for each fuzzy subset for each cluster for each attribute 

I am Maximum [-1, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1]
I am Minimum [100000, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100000]
Quantitative Attributes=[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]


Note function of center 3 and center 8 are not working as expected 
 """
centers=[[0,0,0],
[ 0.00021344,0.00018641,0.00020211],
[0,0,0],
[ 0.,  0.,  0.],
[  2.21325983e-05,   2.29170329e-05,   2.44831633e-05],
[  1.60628891e-05,   1.48007031e-05   ,8.43979602e-06],
[  3.82248404e-05 ,  3.84324996e-05   ,3.67536831e-05],
[  9.46657566e-05  , 9.32516836e-05   ,9.65646132e-05],
[ 0. , 0.  ,0.],
[ 0.65640511  ,0.65520109  ,0.65635623],
[ 0.57417817  ,0.57744169  ,0.57746369],
[ 0.17946027  ,0.18075617  ,0.1793538 ],
[ 0.17891985  ,0.17860842  ,0.17954104],
[ 0.0581702   ,0.05862064  ,0.05713478],
[ 0.05869052  ,0.05849481  ,0.05788799],
[ 0.78776742 , 0.7876067  , 0.78794943],
[ 0.02153975  ,0.02135626  ,0.02126644],
[ 0.0276449   ,0.02823056  ,0.02794282],
[ 0.91225459  ,0.91261795  ,0.91246773],
[ 0.73881214  ,0.73842295  ,0.7391723 ],
[ 0.75235378  ,0.75432081  ,0.75281704],
[ 0.03029888  ,0.03049008  ,0.03040246],
[ 0.60376995  ,0.60371358  ,0.60398595],
[ 0.00629669  ,0.00646135  ,0.00648589],
[ 0.1786191   ,0.17993746  ,0.17926898],
[ 0.1803521   ,0.17873211  ,0.17854692],
[ 0.05818192  ,0.05707678  ,0.05779972],
[ 0.05779159  ,0.05787087  ,0.05743083]
]

def tcp(x):
	if x=='tcp':
		return 1
	else :
		return 0


def udp(x):
	if x=='udp':
		return 1
	else :
		return 0

def icmp(x):
	if x=='icmp':
		return 1
	else :
		return 0
				
def low2(x):
	if x==0:
		return 1 
	return 0	


def high2(x):
	if x==1:
		return 1 	
	return 0

def low1(x):
 	if x<centers[1][0]:
 		return 1
 	if x>centers[1][0] and x<centers[1][1]:
 		return ((x-centers[1][1])/(centers[1][0]-centers[1][1]))
 	if 	x>centers[1][1]:
 		return 0	
 			
def medium1(x):
 	if x<centers[1][0]:
 		return 0
 	if x==centers[1][1]:
 		return 1	
 	if x>centers[1][0] and x<centers[1][1]:
 		return ((x-centers[1][1])/(centers[1][1]-centers[1][0]))
 	if x>centers[1][1] and x<centers[1][2]:
 		return ((x-centers[1][2])/(centers[1][1]-centers[1][2]))
 
 	if 	x>centers[1][2]:
 		return 0	

def high1(x):
 	if x<centers[1][2]:
 		return 0
 	if x>centers[1][1] and x<centers[1][2]:
 		return ((x-centers[1][1])/(centers[1][2]-centers[1][1]))
 	if 	x>centers[1][2]:
 		return 1	
def low3(x):
 	if x<centers[3][0]:
 		return 1
 	if x>centers[3][0] and x<centers[3][1]:
 		return ((x-centers[3][1])/(centers[3][0]-centers[3][1]))
 	if 	x>centers[3][1]:
 		return 0	
 	return 0		
def medium3(x):
 	if x<centers[3][0]:
 		return 0
 	if x==centers[3][1]:
 		return 1	
 	if x>centers[3][0] and x<centers[3][1]:
 		return ((x-centers[3][1])/(centers[3][1]-centers[3][0]))
 	if x>centers[3][1] and x<centers[3][2]:
 		return ((x-centers[3][2])/(centers[3][1]-centers[3][2]))
 
 	if 	x>centers[3][2]:
 		return 0	
 	return 0	
def high3(x):
 	if x<centers[3][2]:
 		return 0
 	if x>centers[3][1] and x<centers[3][2]:
 		return ((x-centers[3][1])/(centers[3][2]-centers[3][1]))
 	if 	x>centers[3][2]:
 		return 1	
 	return 0	
def low4(x):
 	if x<centers[4][0]:
 		return 1
 	if x>centers[4][0] and x<centers[4][1]:
 		return ((x-centers[4][1])/(centers[4][0]-centers[4][1]))
 	if 	x>centers[4][1]:
 		return 0	
 			
def medium4(x):
 	if x<centers[4][0]:
 		return 0
 	if x==centers[4][1]:
 		return 1	
 	if x>centers[4][0] and x<centers[4][1]:
 		return ((x-centers[4][1])/(centers[4][1]-centers[4][0]))
 	if x>centers[4][1] and x<centers[4][2]:
 		return ((x-centers[4][2])/(centers[4][1]-centers[4][2]))
 
 	if 	x>centers[4][2]:
 		return 0	

def high4(x):
 	if x<centers[4][2]:
 		return 0
 	if x>centers[4][1] and x<centers[4][2]:
 		return ((x-centers[4][1])/(centers[4][2]-centers[4][1]))
 	if 	x>centers[4][2]:
 		return 1	
def low5(x):
 	if x<centers[5][0]:
 		return 1
 	if x>centers[5][0] and x<centers[5][1]:
 		return ((x-centers[5][1])/(centers[5][0]-centers[5][1]))
 	if 	x>centers[5][1]:
 		return 0	
 			
def medium5(x):
 	if x<centers[5][0]:
 		return 0
 	if x==centers[5][1]:
 		return 1	
 	if x>centers[5][0] and x<centers[5][1]:
 		return ((x-centers[5][1])/(centers[5][1]-centers[5][0]))
 	if x>centers[5][1] and x<centers[5][2]:
 		return ((x-centers[5][2])/(centers[5][1]-centers[5][2]))
 
 	if 	x>centers[5][2]:
 		return 0	

def high5(x):
 	if x<centers[5][2]:
 		return 0
 	if x>centers[5][1] and x<centers[5][2]:
 		return ((x-centers[5][1])/(centers[5][2]-centers[5][1]))
 	if 	x>centers[5][2]:
 		return 1	
def low6(x):
 	if x<centers[6][0]:
 		return 1
 	if x>centers[6][0] and x<centers[6][1]:
 		return ((x-centers[6][1])/(centers[6][0]-centers[6][1]))
 	if 	x>centers[6][1]:
 		return 0	
 			
def medium6(x):
 	if x<centers[6][0]:
 		return 0
 	if x==centers[6][1]:
 		return 1	
 	if x>centers[6][0] and x<centers[6][1]:
 		return ((x-centers[6][1])/(centers[6][1]-centers[6][0]))
 	if x>centers[6][1] and x<centers[6][2]:
 		return ((x-centers[6][2])/(centers[6][1]-centers[6][2]))
 
 	if 	x>centers[6][2]:
 		return 0	

def high6(x):
 	if x<centers[6][2]:
 		return 0
 	if x>centers[6][1] and x<centers[6][2]:
 		return ((x-centers[6][1])/(centers[6][2]-centers[6][1]))
 	if 	x>centers[6][2]:
 		return 1	
def low7(x):
 	if x<centers[7][0]:
 		return 1
 	if x>centers[7][0] and x<centers[7][1]:
 		return ((x-centers[7][1])/(centers[7][0]-centers[7][1]))
 	if 	x>centers[7][1]:
 		return 0	
 			
def medium7(x):
 	if x<centers[7][0]:
 		return 0
 	if x==centers[7][1]:
 		return 1	
 	if x>centers[7][0] and x<centers[7][1]:
 		return ((x-centers[7][1])/(centers[7][1]-centers[7][0]))
 	if x>centers[7][1] and x<centers[7][2]:
 		return ((x-centers[7][2])/(centers[7][1]-centers[7][2]))
 
 	if 	x>centers[7][2]:
 		return 0	

def high7(x):
 	if x<centers[7][2]:
 		return 0
 	if x>centers[7][1] and x<centers[7][2]:
 		return ((x-centers[7][1])/(centers[7][2]-centers[7][1]))
 	if 	x>centers[7][2]:
 		return 1	
def low8(x):
 	if x<centers[8][0]:
 		return 1
 	if x>centers[8][0] and x<centers[8][1]:
 		return ((x-centers[8][1])/(centers[8][0]-centers[8][1]))
 	if 	x>centers[8][1]:
 		return 0	
 	return 0		
def medium8(x):
 	if x<centers[8][0]:
 		return 0
 	if x==centers[8][1]:
 		return 1	
 	if x>centers[8][0] and x<centers[8][1]:
 		return ((x-centers[8][1])/(centers[8][1]-centers[8][0]))
 	if x>centers[8][1] and x<centers[8][2]:
 		return ((x-centers[8][2])/(centers[8][1]-centers[8][2]))
 
 	if 	x>centers[8][2]:
 		return 0	
 	return 0	
def high8(x):
 	if x<centers[8][2]:
 		return 0
 	if x>centers[8][1] and x<centers[8][2]:
 		return ((x-centers[8][1])/(centers[8][2]-centers[8][1]))
 	if 	x>centers[8][2]:
 		return 1
 	return 0		
def low9(x):
 	if x<centers[9][0]:
 		return 1
 	if x>centers[9][0] and x<centers[9][1]:
 		return ((x-centers[9][1])/(centers[9][0]-centers[9][1]))
 	if 	x>centers[9][1]:
 		return 0	
 			
def medium9(x):
 	if x<centers[9][0]:
 		return 0
 	if x==centers[9][1]:
 		return 1	
 	if x>centers[9][0] and x<centers[9][1]:
 		return ((x-centers[9][1])/(centers[9][1]-centers[9][0]))
 	if x>centers[9][1] and x<centers[9][2]:
 		return ((x-centers[9][2])/(centers[9][1]-centers[9][2]))
 
 	if 	x>centers[9][2]:
 		return 0	

def high9(x):
 	if x<centers[9][2]:
 		return 0
 	if x>centers[9][1] and x<centers[9][2]:
 		return ((x-centers[9][1])/(centers[9][2]-centers[9][1]))
 	if 	x>centers[9][2]:
 		return 1	
def low10(x):
 	if x<centers[10][0]:
 		return 1
 	if x>centers[10][0] and x<centers[10][1]:
 		return ((x-centers[10][1])/(centers[10][0]-centers[10][1]))
 	if 	x>centers[10][1]:
 		return 0	
 			
def medium10(x):
 	if x<centers[10][0]:
 		return 0
 	if x==centers[10][1]:
 		return 1	
 	if x>centers[10][0] and x<centers[10][1]:
 		return ((x-centers[10][1])/(centers[10][1]-centers[10][0]))
 	if x>centers[10][1] and x<centers[10][2]:
 		return ((x-centers[10][2])/(centers[10][1]-centers[10][2]))
 
 	if 	x>centers[10][2]:
 		return 0	

def high10(x):
 	if x<centers[10][2]:
 		return 0
 	if x>centers[10][1] and x<centers[10][2]:
 		return ((x-centers[10][1])/(centers[10][2]-centers[10][1]))
 	if 	x>centers[10][2]:
 		return 1	
def low11(x):
 	if x<centers[11][0]:
 		return 1
 	if x>centers[11][0] and x<centers[11][1]:
 		return ((x-centers[11][1])/(centers[11][0]-centers[11][1]))
 	if 	x>centers[11][1]:
 		return 0	
 			
def medium11(x):
 	if x<centers[11][0]:
 		return 0
 	if x==centers[11][1]:
 		return 1	
 	if x>centers[11][0] and x<centers[11][1]:
 		return ((x-centers[11][1])/(centers[11][1]-centers[11][0]))
 	if x>centers[11][1] and x<centers[11][2]:
 		return ((x-centers[11][2])/(centers[11][1]-centers[11][2]))
 
 	if 	x>centers[11][2]:
 		return 0	

def high11(x):
 	if x<centers[11][2]:
 		return 0
 	if x>centers[11][1] and x<centers[11][2]:
 		return ((x-centers[11][1])/(centers[11][2]-centers[11][1]))
 	if 	x>centers[11][2]:
 		return 1	
def low12(x):
 	if x<centers[12][0]:
 		return 1
 	if x>centers[12][0] and x<centers[12][1]:
 		return ((x-centers[12][1])/(centers[12][0]-centers[12][1]))
 	if 	x>centers[12][1]:
 		return 0	
 			
def medium12(x):
 	if x<centers[12][0]:
 		return 0
 	if x==centers[12][1]:
 		return 1	
 	if x>centers[12][0] and x<centers[12][1]:
 		return ((x-centers[12][1])/(centers[12][1]-centers[12][0]))
 	if x>centers[12][1] and x<centers[12][2]:
 		return ((x-centers[12][2])/(centers[12][1]-centers[12][2]))
 
 	if 	x>centers[12][2]:
 		return 0	

def high12(x):
 	if x<centers[12][2]:
 		return 0
 	if x>centers[12][1] and x<centers[12][2]:
 		return ((x-centers[12][1])/(centers[12][2]-centers[12][1]))
 	if 	x>centers[12][2]:
 		return 1	
def low13(x):
 	if x<centers[13][0]:
 		return 1
 	if x>centers[13][0] and x<centers[13][1]:
 		return ((x-centers[13][1])/(centers[13][0]-centers[13][1]))
 	if 	x>centers[13][1]:
 		return 0	
 			
def medium13(x):
 	if x<centers[13][0]:
 		return 0
 	if x==centers[13][1]:
 		return 1	
 	if x>centers[13][0] and x<centers[13][1]:
 		return ((x-centers[13][1])/(centers[13][1]-centers[13][0]))
 	if x>centers[13][1] and x<centers[13][2]:
 		return ((x-centers[13][2])/(centers[13][1]-centers[13][2]))
 
 	if 	x>centers[13][2]:
 		return 0	

def high13(x):
 	if x<centers[13][2]:
 		return 0
 	if x>centers[13][1] and x<centers[13][2]:
 		return ((x-centers[13][1])/(centers[13][2]-centers[13][1]))
 	if 	x>centers[13][2]:
 		return 1	
def low14(x):
 	if x<centers[14][0]:
 		return 1
 	if x>centers[14][0] and x<centers[14][1]:
 		return ((x-centers[14][1])/(centers[14][0]-centers[14][1]))
 	if 	x>centers[14][1]:
 		return 0	
 			
def medium14(x):
 	if x<centers[14][0]:
 		return 0
 	if x==centers[14][1]:
 		return 1	
 	if x>centers[14][0] and x<centers[14][1]:
 		return ((x-centers[14][1])/(centers[14][1]-centers[14][0]))
 	if x>centers[14][1] and x<centers[14][2]:
 		return ((x-centers[14][2])/(centers[14][1]-centers[14][2]))
 
 	if 	x>centers[14][2]:
 		return 0	

def high14(x):
 	if x<centers[14][2]:
 		return 0
 	if x>centers[14][1] and x<centers[14][2]:
 		return ((x-centers[14][1])/(centers[14][2]-centers[14][1]))
 	if 	x>centers[14][2]:
 		return 1	
def low15(x):
 	if x<centers[15][0]:
 		return 1
 	if x>centers[15][0] and x<centers[15][1]:
 		return ((x-centers[15][1])/(centers[15][0]-centers[15][1]))
 	if 	x>centers[15][1]:
 		return 0	
 			
def medium15(x):
 	if x<centers[15][0]:
 		return 0
 	if x==centers[15][1]:
 		return 1	
 	if x>centers[15][0] and x<centers[15][1]:
 		return ((x-centers[15][1])/(centers[15][1]-centers[15][0]))
 	if x>centers[15][1] and x<centers[15][2]:
 		return ((x-centers[15][2])/(centers[15][1]-centers[15][2]))
 
 	if 	x>centers[15][2]:
 		return 0	

def high15(x):
 	if x<centers[15][2]:
 		return 0
 	if x>centers[15][1] and x<centers[15][2]:
 		return ((x-centers[15][1])/(centers[15][2]-centers[15][1]))
 	if 	x>centers[15][2]:
 		return 1	
def low16(x):
 	if x<centers[16][0]:
 		return 1
 	if x>centers[16][0] and x<centers[16][1]:
 		return ((x-centers[16][1])/(centers[16][0]-centers[16][1]))
 	if 	x>centers[16][1]:
 		return 0	
 			
def medium16(x):
 	if x<centers[16][0]:
 		return 0
 	if x==centers[16][1]:
 		return 1	
 	if x>centers[16][0] and x<centers[16][1]:
 		return ((x-centers[16][1])/(centers[16][1]-centers[16][0]))
 	if x>centers[16][1] and x<centers[16][2]:
 		return ((x-centers[16][2])/(centers[16][1]-centers[16][2]))
 
 	if 	x>centers[16][2]:
 		return 0	

def high16(x):
 	if x<centers[16][2]:
 		return 0
 	if x>centers[16][1] and x<centers[16][2]:
 		return ((x-centers[16][1])/(centers[16][2]-centers[16][1]))
 	if 	x>centers[16][2]:
 		return 1	
def low17(x):
 	if x<centers[17][0]:
 		return 1
 	if x>centers[17][0] and x<centers[17][1]:
 		return ((x-centers[17][1])/(centers[17][0]-centers[17][1]))
 	if 	x>centers[17][1]:
 		return 0	
 			
def medium17(x):
 	if x<centers[17][0]:
 		return 0
 	if x==centers[17][1]:
 		return 1	
 	if x>centers[17][0] and x<centers[17][1]:
 		return ((x-centers[17][1])/(centers[17][1]-centers[17][0]))
 	if x>centers[17][1] and x<centers[17][2]:
 		return ((x-centers[17][2])/(centers[17][1]-centers[17][2]))
 
 	if 	x>centers[17][2]:
 		return 0	

def high17(x):
 	if x<centers[17][2]:
 		return 0
 	if x>centers[17][1] and x<centers[17][2]:
 		return ((x-centers[17][1])/(centers[17][2]-centers[17][1]))
 	if 	x>centers[17][2]:
 		return 1	
def low18(x):
 	if x<centers[18][0]:
 		return 1
 	if x>centers[18][0] and x<centers[18][1]:
 		return ((x-centers[18][1])/(centers[18][0]-centers[18][1]))
 	if 	x>centers[18][1]:
 		return 0	
 			
def medium18(x):
 	if x<centers[18][0]:
 		return 0
 	if x==centers[18][1]:
 		return 1	
 	if x>centers[18][0] and x<centers[18][1]:
 		return ((x-centers[18][1])/(centers[18][1]-centers[18][0]))
 	if x>centers[18][1] and x<centers[18][2]:
 		return ((x-centers[18][2])/(centers[18][1]-centers[18][2]))
 
 	if 	x>centers[18][2]:
 		return 0	

def high18(x):
 	if x<centers[18][2]:
 		return 0
 	if x>centers[18][1] and x<centers[18][2]:
 		return ((x-centers[18][1])/(centers[18][2]-centers[18][1]))
 	if 	x>centers[18][2]:
 		return 1	
def low19(x):
 	if x<centers[19][0]:
 		return 1
 	if x>centers[19][0] and x<centers[19][1]:
 		return ((x-centers[19][1])/(centers[19][0]-centers[19][1]))
 	if 	x>centers[19][1]:
 		return 0	
 			
def medium19(x):
 	if x<centers[19][0]:
 		return 0
 	if x==centers[19][1]:
 		return 1	
 	if x>centers[19][0] and x<centers[19][1]:
 		return ((x-centers[19][1])/(centers[19][1]-centers[19][0]))
 	if x>centers[19][1] and x<centers[19][2]:
 		return ((x-centers[19][2])/(centers[19][1]-centers[19][2]))
 
 	if 	x>centers[19][2]:
 		return 0	

def high19(x):
 	if x<centers[19][2]:
 		return 0
 	if x>centers[19][1] and x<centers[19][2]:
 		return ((x-centers[19][1])/(centers[19][2]-centers[19][1]))
 	if 	x>centers[19][2]:
 		return 1	
def low20(x):
 	if x<centers[20][0]:
 		return 1
 	if x>centers[20][0] and x<centers[20][1]:
 		return ((x-centers[20][1])/(centers[20][0]-centers[20][1]))
 	if 	x>centers[20][1]:
 		return 0	
 			
def medium20(x):
 	if x<centers[20][0]:
 		return 0
 	if x==centers[20][1]:
 		return 1	
 	if x>centers[20][0] and x<centers[20][1]:
 		return ((x-centers[20][1])/(centers[20][1]-centers[20][0]))
 	if x>centers[20][1] and x<centers[20][2]:
 		return ((x-centers[20][2])/(centers[20][1]-centers[20][2]))
 
 	if 	x>centers[20][2]:
 		return 0	

def high20(x):
 	if x<centers[20][2]:
 		return 0
 	if x>centers[20][1] and x<centers[20][2]:
 		return ((x-centers[20][1])/(centers[20][2]-centers[20][1]))
 	if 	x>centers[20][2]:
 		return 1	
def low21(x):
 	if x<centers[21][0]:
 		return 1
 	if x>centers[21][0] and x<centers[21][1]:
 		return ((x-centers[21][1])/(centers[21][0]-centers[21][1]))
 	if 	x>centers[21][1]:
 		return 0	
 			
def medium21(x):
 	if x<centers[21][0]:
 		return 0
 	if x==centers[21][1]:
 		return 1	
 	if x>centers[21][0] and x<centers[21][1]:
 		return ((x-centers[21][1])/(centers[21][1]-centers[21][0]))
 	if x>centers[21][1] and x<centers[21][2]:
 		return ((x-centers[21][2])/(centers[21][1]-centers[21][2]))
 
 	if 	x>centers[21][2]:
 		return 0	

def high21(x):
 	if x<centers[21][2]:
 		return 0
 	if x>centers[21][1] and x<centers[21][2]:
 		return ((x-centers[21][1])/(centers[21][2]-centers[21][1]))
 	if 	x>centers[21][2]:
 		return 1	
def low22(x):
 	if x<centers[22][0]:
 		return 1
 	if x>centers[22][0] and x<centers[22][1]:
 		return ((x-centers[22][1])/(centers[22][0]-centers[22][1]))
 	if 	x>centers[22][1]:
 		return 0	
 			
def medium22(x):
 	if x<centers[22][0]:
 		return 0
 	if x==centers[22][1]:
 		return 1	
 	if x>centers[22][0] and x<centers[22][1]:
 		return ((x-centers[22][1])/(centers[22][1]-centers[22][0]))
 	if x>centers[22][1] and x<centers[22][2]:
 		return ((x-centers[22][2])/(centers[22][1]-centers[22][2]))
 
 	if 	x>centers[22][2]:
 		return 0	

def high22(x):
 	if x<centers[22][2]:
 		return 0
 	if x>centers[22][1] and x<centers[22][2]:
 		return ((x-centers[22][1])/(centers[22][2]-centers[22][1]))
 	if 	x>centers[22][2]:
 		return 1	
def low23(x):
 	if x<centers[23][0]:
 		return 1
 	if x>centers[23][0] and x<centers[23][1]:
 		return ((x-centers[23][1])/(centers[23][0]-centers[23][1]))
 	if 	x>centers[23][1]:
 		return 0	
 			
def medium23(x):
 	if x<centers[23][0]:
 		return 0
 	if x==centers[23][1]:
 		return 1	
 	if x>centers[23][0] and x<centers[23][1]:
 		return ((x-centers[23][1])/(centers[23][1]-centers[23][0]))
 	if x>centers[23][1] and x<centers[23][2]:
 		return ((x-centers[23][2])/(centers[23][1]-centers[23][2]))
 
 	if 	x>centers[23][2]:
 		return 0	

def high23(x):
 	if x<centers[23][2]:
 		return 0
 	if x>centers[23][1] and x<centers[23][2]:
 		return ((x-centers[23][1])/(centers[23][2]-centers[23][1]))
 	if 	x>centers[23][2]:
 		return 1	
def low24(x):
 	if x<centers[24][0]:
 		return 1
 	if x>centers[24][0] and x<centers[24][1]:
 		return ((x-centers[24][1])/(centers[24][0]-centers[24][1]))
 	if 	x>centers[24][1]:
 		return 0	
 			
def medium24(x):
 	if x<centers[24][0]:
 		return 0
 	if x==centers[24][1]:
 		return 1	
 	if x>centers[24][0] and x<centers[24][1]:
 		return ((x-centers[24][1])/(centers[24][1]-centers[24][0]))
 	if x>centers[24][1] and x<centers[24][2]:
 		return ((x-centers[24][2])/(centers[24][1]-centers[24][2]))
 
 	if 	x>centers[24][2]:
 		return 0	

def high24(x):
 	if x<centers[24][2]:
 		return 0
 	if x>centers[24][1] and x<centers[24][2]:
 		return ((x-centers[24][1])/(centers[24][2]-centers[24][1]))
 	if 	x>centers[24][2]:
 		return 1	
def low25(x):
 	if x<centers[25][0]:
 		return 1
 	if x>centers[25][0] and x<centers[25][1]:
 		return ((x-centers[25][1])/(centers[25][0]-centers[25][1]))
 	if 	x>centers[25][1]:
 		return 0	
 			
def medium25(x):
 	if x<centers[25][0]:
 		return 0
 	if x==centers[25][1]:
 		return 1	
 	if x>centers[25][0] and x<centers[25][1]:
 		return ((x-centers[25][1])/(centers[25][1]-centers[25][0]))
 	if x>centers[25][1] and x<centers[25][2]:
 		return ((x-centers[25][2])/(centers[25][1]-centers[25][2]))
 
 	if 	x>centers[25][2]:
 		return 0	

def high25(x):
 	if x<centers[25][2]:
 		return 0
 	if x>centers[25][1] and x<centers[25][2]:
 		return ((x-centers[25][1])/(centers[25][2]-centers[25][1]))
 	if 	x>centers[25][2]:
 		return 1	
def low26(x):
 	if x<centers[26][0]:
 		return 1
 	if x>centers[26][0] and x<centers[26][1]:
 		return ((x-centers[26][1])/(centers[26][0]-centers[26][1]))
 	if 	x>centers[26][1]:
 		return 0	
 			
def medium26(x):
 	if x<centers[26][0]:
 		return 0
 	if x==centers[26][1]:
 		return 1	
 	if x>centers[26][0] and x<centers[26][1]:
 		return ((x-centers[26][1])/(centers[26][1]-centers[26][0]))
 	if x>centers[26][1] and x<centers[26][2]:
 		return ((x-centers[26][2])/(centers[26][1]-centers[26][2]))
 
 	if 	x>centers[26][2]:
 		return 0	

def high26(x):
 	if x<centers[26][2]:
 		return 0
 	if x>centers[26][1] and x<centers[26][2]:
 		return ((x-centers[26][1])/(centers[26][2]-centers[26][1]))
 	if 	x>centers[26][2]:
 		return 1	
def low27(x):
 	if x<centers[27][0]:
 		return 1
 	if x>centers[27][0] and x<centers[27][1]:
 		return ((x-centers[27][1])/(centers[27][0]-centers[27][1]))
 	if 	x>centers[27][1]:
 		return 0	
 			
def medium27(x):
 	if x<centers[27][0]:
 		return 0
 	if x==centers[27][1]:
 		return 1	
 	if x>centers[27][0] and x<centers[27][1]:
 		return ((x-centers[27][1])/(centers[27][1]-centers[27][0]))
 	if x>centers[27][1] and x<centers[27][2]:
 		return ((x-centers[27][2])/(centers[27][1]-centers[27][2]))
 
 	if 	x>centers[27][2]:
 		return 0	

def high27(x):
 	if x<centers[27][2]:
 		return 0
 	if x>centers[27][1] and x<centers[27][2]:
 		return ((x-centers[27][1])/(centers[27][2]-centers[27][1]))
 	if 	x>centers[27][2]:
 		return 1	

def dos(x):
	dos=["back","land","neptune","pod","smurf","teardrop","snmpgetattack"] #type 1 attack
	try:
		l =dos.index(x)
		return 1
	except:
		return 0

def u2r(x):
	u2r=["buffer_overflow","loadmodule","perl","rootkit"] #type 3 
	try:
		l=u2r.index(x)
		return 1
	except:	
		return 0

def r2l(x):
	r2l=["ftp_write","guess_passwd","imap","multihop","phf","spy","warezclient","warezmaster"] # type 2  
	try:
		l=r2l.index(x)
		return 1
	except:	
		return 0


def probe(x):
	probe=["nmap","satan","ipsweep","portsweep"] # type 4

	try:
		l=probe.index(x)
		return 1
	except:	
		return 0

def normal(x):
	if x=='normal':
		return 1  		

	return 0	