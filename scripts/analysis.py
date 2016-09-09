#! /usr/bin/env python

''' Results are encoded into length-4 vectors in the following order:
False Positives, False Negatives, True Positives and True Negatives
Additionally, a "Spoof" image is given the label "1" in the data'''

import numpy as np

def analyze(l,o1,o2,o3):
	length = len(l)
	results = dict()
	for gate in ['o1','o2','o3']:
		results[gate] = np.zeros(4)
	#fix labels
	for gate,vect in zip(['o1','o2','o3'],[o1,o2,o3]):
		for i,label in enumerate(l):
			if label == 1 and vect[i] == 0:
				results[gate][0] +=1
			elif label == 0 and vect[i] == 1:
				results[gate][1] +=1
			elif label == 0 and vect[i] == 0:
				results[gate][2] +=1
			elif label == 1 and vect[i] == 1:
				results[gate][3] +=1
			else:
				print label
				print vect[i]
		results[gate] = results[gate]
	return results	
		


labels = np.load('./results/labels.npy')
out1 = np.load('./results/out1.npy')
out2 = np.load('./results/out2.npy')
out3 = np.load('./results/out3.npy')

assert labels.shape == out1.shape == out2.shape == out3.shape
LENGTH = len(labels[0])
TRIALS = labels.shape[0]

all_results=[]


for j in range(labels.shape[0]):
	all_results.append(analyze(labels[j],out1[j],out2[j],out3[j]))

out1ave = np.zeros(4); out2ave = np.zeros(4); out3ave = np.zeros(4)

for result in all_results:
	out1ave += result['o1']
	out2ave += result['o2']
	out3ave += result['o3']

print LENGTH, TRIALS

print "Out 1: " + str(out1ave/TRIALS)
print "Out 2: " + str(out2ave/TRIALS)
print "Out 3: " + str(out3ave/TRIALS)
print '--------\nAcc:\n'
print "Out 1: " + str((out1ave[2]/((len(labels[0])-np.sum(labels[0])))+(out1ave[3]/np.sum(labels[0])))/20)
print "Out 2: " + str((out2ave[2]/((len(labels[1])-np.sum(labels[1])))+(out2ave[3]/np.sum(labels[1])))/20)
print "Out 3: " + str((out3ave[2]/((len(labels[2])-np.sum(labels[2])))+(out3ave[3]/np.sum(labels[2])))/20)

