#! /usr/bin/env python

import os
import random

training = os.listdir('./data/LivDet-Iris-2015-Warsaw-Training/PNG')
testing = os.listdir('./data/LivDet-Iris-2015-Warsaw-Testing/PNG')

traindata = open('./divison/warsaw_train_all.txt','w+')
testdata = open('./division/warsaw_test_all.txt','w+')

for img in training:
	if img.split('_')[1] == 'PRNT':
		traindata.write('./data/LivDet-Iris-2015-Warsaw-Training/PNG/'+img + ' 1\n')
	elif img.split('_')[1] == 'REAL':
		traindata.write('./data/LivDet-Iris-2015-Warsaw-Training/PNG/'+img + ' 0\n')
	else:
		if img != '.DS_Store':
			print('Error reading data')
			exit(1)
for img in testing:
	if img.split('_')[1] == 'PRNT':
		testdata.write('./data/LivDet-Iris-2015-Warsaw-Testing/PNG/'+img + ' 1\n')
	elif img.split('_')[1] == 'REAL':
		testdata.write('./data/LivDet-Iris-2015-Warsaw-Testing/PNG/'+img + ' 0\n')
	else:
		if img != '.DS_Store':
			print('Error reading data')
			exit(1)
traindata.close()
testdata.close()
