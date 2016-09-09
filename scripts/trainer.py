#! /usr/bin/env python

import os
#os.environ['GLOG_minloglevel'] = '2' 

import caffe

import sys
import os

import numpy as np
from numpy import zeros


## Constants, yo ##

label = ''
MAX_ITER = 1501
TEST_INTERVAL = 4000
NUMTRIALS = 1


## Argument Handling ##

if len(sys.argv) > 1:
	caffe.set_device(int(sys.argv[1]))
	caffe.set_mode_gpu()
else:
	caffe.set_mode_cpu()

if len(sys.argv) > 2:
	NUMTRIALS = int(sys.argv[2])

solverPATH = 'solver/googlenet_solver.proto'

labell = []
out1l = []
out2l = []
out3l = []

def train():

    # Instantiate a solver object load the prototxt
    solver = caffe.get_solver(solverPATH)

    solver.max_iter = MAX_ITER
    solver.test_iter = 92
    solver.test_bs = 64
    solver.test_interval = TEST_INTERVAL



    # the main solver loop
    for it in range(1,solver.max_iter+1):
        
        #train the next batch
        solver.step(1)

	#Test if the right interval
        if it % solver.test_interval == 0 :
            print 'Iteration', it, 'testing'

            acc = 0
            loss = 0
	    label = []
	    out1 = []
	    out2= []
	    out3 = []


            for test_it in range(solver.test_iter):

            	#Run the test data through the network
                solver.test_nets[0].forward()
		label = np.concatenate((label,solver.test_nets[0].blobs['label'].data),axis=0)

		out1 = np.concatenate((out1,solver.test_nets[0].blobs['loss1/classifier_transfer'].data.argmax(1)),axis=0)
		out2 = np.concatenate((out2,solver.test_nets[0].blobs['loss2/classifier_transfer'].data.argmax(1)),axis=0)
		out3 = np.concatenate((out3,solver.test_nets[0].blobs['loss3/classifier_transfer'].data.argmax(1)),axis=0)

#            	loss += solver.test_nets[0].blobs['loss'].data
#            	acc += solver.test_nets[0].blobs['accuracy'].data

	# Record the test data
#            print float(loss)  / solver.test_iter
#            print float(acc) / solver.test_iter
	    

	    labell.append(label)
	    out1l.append(out1)
	    out2l.append(out2)
	    out3l.append(out3)
	    return

for _ in range(NUMTRIALS):
	print "------------------------"
	train()	

np.save('./results/labels',labell)
np.save('./results/out1',out1l)
np.save('./results/out2',out2l)
np.save('./results/out3',out3l)



