#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn.svm import SVC

sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#clf = SVC(kernel='linear')
clf = SVC(kernel = 'rbf')

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predict time:", round(time() - t1, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
#acc = clf.score(features_test, labels_test)

print 'accuracy:', acc


print '------Test for different C------'
cl = [10, 100, 1000, 10000]

for c in cl:
	clf = SVC(kernel = 'rbf', C = c)
	clf.fit(features_train, labels_train)
	pred = clf.predict(features_test)
	acc = accuracy_score(pred, labels_test)
	print 'accuracy with C is ', c, ': ',acc


print '------Use kernel rbf, C 10000, and all data------'
features_train, features_test, labels_train, labels_test = preprocess()

clf = SVC(kernel = 'rbf', C = 10000)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predict time:", round(time() - t1, 3), "s"

acc = accuracy_score(pred, labels_test)

print 'accuracy with rbf kernel and 10000 C : ', acc

print '------Use the clf predict the class------'
print pred[10], pred[26], pred[50]

print '------the num of class 1------'
num_1 = 0
for x in pred:
	if x == 1:
		num_1 = num_1 + 1

print "the num of class 1: ", num_1

#########################################################


