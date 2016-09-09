#! /usr/bin/env python

import os
#os.environ['GLOG_minloglevel'] = '2' 

import caffe

import sys
import os

import numpy as np
from numpy import zeros


## Constants, yo ##

NUMTRIALS = 1

## Argument Handling ##

if len(sys.argv) > 1:
	caffe.set_device(int(sys.argv[1]))
	caffe.set_mode_gpu()

if len(sys.argv) > 2:
	NUMTRIALS = int(sys.argv[2])

WEIGHTSPATH = 'snapshot/googlenet_iter_4000.caffemodel'

labell = []
out1l = []
out2l = []
out3l = []

def train():

    exitCode = os.system('./scripts/transfer.job')    

    # Instantiate a net object load the prototxt
    net = caffe.Net(MODELPATH, WEIGHTSPATH, caffe.TEST)

    net.test_iter = 92
    net.test_bs = 64

#Test if the right interval

    acc = 0
    loss = 0
    label = []
    out1 = []
    out2= []
    out3 = []


    for test_it in range(net.test_iter):

            	#Run the test data through the network
        net.forward()
	label = np.concatenate((label,net.blobs['label'].data),axis=0)

	out1 = np.concatenate((out1,net.blobs['loss1/classifier_transfer'].data.argmax(1)),axis=0)
	out2 = np.concatenate((out2,net.blobs['loss2/classifier_transfer'].data.argmax(1)),axis=0)
	out3 = np.concatenate((out3,net.blobs['loss3/classifier_transfer'].data.argmax(1)),axis=0)

#            	loss += net.test_nets[0].blobs['loss'].data
#            	acc += net.test_nets[0].blobs['accuracy'].data

# Record the test data
#            print float(loss)  / net.test_iter
#            print float(acc) / net.test_iter
    

    labell.append(label)
    out1l.append(out1)
    out2l.append(out2)
    out3l.append(out3)
    return

for i in range(10):
	MODELPATH = 'model/g' + str(i)
	print "------------------------"
	train()	

np.save('./results/labels',labell)
np.save('./results/out1',out1l)
np.save('./results/out2',out2l)
np.save('./results/out3',out3l)



