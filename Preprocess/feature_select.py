#!/usr/bin/env python

import random
from random import randrange
import sys
from time import time
from datetime import datetime

whole_fsc_dict={}
whole_imp_v=[]

def cal_feat_imp(label,sample):

	print("calculating fsc...")

	score_dict=cal_Fscore(label,sample)

	score_tuples = list(score_dict.items())
	score_tuples.sort(key = value_cmpf)

	feat_v = score_tuples
	for i in range(len(feat_v)): feat_v[i]=score_tuples[i][0]
	print("fsc done")
	return score_dict,feat_v


def random_shuffle(label, sample):
	random.seed(1)  # so that result is the same every time
	size = len(label)
	for i in range(size):
		ri = randrange(0, size-i)
		tmp = label[ri]
		label[ri] = label[size-i-1]
		label[size-i-1] = tmp
		tmp = sample[ri]
		sample[ri] = sample[size-i-1]
		sample[size-i-1] = tmp

def readdata(filename):
	labels=[]
	samples=[]
	max_index=0
	#load training data
	fp = open(filename)
	line = fp.readline()

	while line:
		# added by untitled, allowing data with comments
		line=line.strip()
		elems = line.split()
		sample = {}
		for e in elems[1:]:
			points = e.split(":")
			p0 = int( points[0].strip() )
			p1 = float( points[1].strip() )
			sample[p0] = p1
			if p0 > max_index:
				max_index = p0
		labels.append(float(elems[0]))
		samples.append(sample)
		line = fp.readline()
	fp.close()

	return labels,samples,max_index

def value_cmpf(x):
	return (-x[1]);


###return a dict containing F_j
def cal_Fscore(labels,samples):

	data_num=float(len(samples))
	p_num = {} #key: label;  value: data num
	sum_f = [] #index: feat_idx;  value: sum
	sum_l_f = {} #dict of lists.  key1: label; index2: feat_idx; value: sum
	sumq_l_f = {} #dict of lists.  key1: label; index2: feat_idx; value: sum of square
	F={} #key: feat_idx;  valud: fscore
	max_idx = -1

	### pass 1: check number of each class and max index of features
	for p in range(len(samples)): # for every data point
		label=labels[p]
		point=samples[p]

		if label in p_num: p_num[label] += 1
		else: p_num[label] = 1

		for f in point.keys(): # for every feature
			if f>max_idx: max_idx=f
	### now p_num and max_idx are set

	### initialize variables
	sum_f = [0 for i in range(max_idx)]
	for la in p_num.keys():
		sum_l_f[la] = [0 for i in range(max_idx)]
		sumq_l_f[la] = [0 for i in range(max_idx)]

	### pass 2: calculate some stats of data
	for p in range(len(samples)): # for every data point
		point=samples[p]
		label=labels[p]
		for tuple in point.items(): # for every feature
			f = tuple[0]-1 # feat index
			v = tuple[1] # feat value
			sum_f[f] += v
			sum_l_f[label][f] += v
			sumq_l_f[label][f] += v**2
	### now sum_f, sum_l_f, sumq_l_f are done

	### for each feature, calculate f-score
	eps = 1e-12
	for f in range(max_idx):
		SB = 0
		for la in p_num.keys():
			SB += (p_num[la] * (sum_l_f[la][f]/p_num[la] - sum_f[f]/data_num)**2 )

		SW = eps
		for la in p_num.keys():
			SW += (sumq_l_f[la][f] - (sum_l_f[la][f]**2)/p_num[la]) 

		F[f+1] = SB / SW

	return F

if __name__ == '__main__':
	if len(sys.argv)<2:
		print "Damn ..Very few arguments "
		exit(0)
	print "Reading.."
	train_file=sys.argv[1]
	labels,samples,max_index=readdata(train_file)
	### Randomly shuffle data
	random_shuffle(labels,samples)
	whole_fsc_dict,whole_imp_v =cal_feat_imp(labels,samples)
	###write (sorted) f-score list in another file
	f_tuples = list(whole_fsc_dict.items())
	f_tuples.sort(key = value_cmpf)
	fd = open("%s.fscore"%train_file, 'w')
	fd.write("The Ranking of Attributes is \n")
	fd.write("Attributes :    Importance \n")
	fd.write("---------------------------------\n")
	for t in f_tuples:
		fd.write("%d:   \t%.6f\n"%t)
	fd.close()
