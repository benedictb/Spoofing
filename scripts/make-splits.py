#! /usr/bin/env python

from random import shuffle

with open('division/warsaw_train_all.txt') as f:
	data = [ line for line in f ]

split = int(len(data) / 2)


for i in range(10):
	shuffle(data)
	train = open('division/t' + str(i), 'w+')
	val = open('division/v' + str(i), 'w+')	
		
	for line in data[:split]:
		train.write(line)
	for line in data[split:]:
		val.write(line)
	
	train.close()
	val.close()
