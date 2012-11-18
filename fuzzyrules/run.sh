array=(100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1500 2000 2400 2600 3000)
i=100

for i in ${array[@]}
do

python fcmutil.py $i >>result 

done 
